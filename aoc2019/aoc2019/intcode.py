import copy
import itertools
import logging


class Intcode:
    def __init__(self, name, instructions, phase_signal_pair):
        self.name = name
        self._logger = logging.getLogger(__name__)
        self._initial_instructions = instructions
        self.opcodes = {
            '01': (self._add, 4),
            '02': (self._multiply, 4),
            '03': (self._input, 2),
            '04': (self._output, 2),
            '05': (self._jump_if_true, 3),
            '06': (self._jump_if_false, 3),
            '07': (self._less_than, 4),
            '08': (self._equals, 4),
            '09': (self._relative_base_offset, 2),
        }
        self.output_history = []
        self.result = 0
        self.reset_state(phase_signal_pair)

    def add_inputs(self, inputs):
        self._phase_signal_pair.extend(inputs)

    def reset_state(self, phase_signal_pair):
        self._logger.info(f"Resetting state of Intcode {self.name}")
        # self._instructions = copy.copy(self._initial_instructions)
        self._instructions = self._create_memory_dict()
        self._phase_signal_pair = phase_signal_pair
        self._index = 0
        self._relative_offset = 0

    def _create_memory_dict(self):
        memory = dict()
        for index, ele in enumerate(self._initial_instructions):
            memory[index] = ele
        return memory

    def compute(self):
        while self._index < len(self._instructions):
            inst = self._instructions.get(self._index, 0)
            inst = str(inst).zfill(4)
            operation = inst[-2:]
            modes = inst[:-2]
            if operation == '99':
                return True
            op, inst_length = self.opcodes.get(operation, None)
            modes = modes.zfill(inst_length)

            if self._should_wait_for_input(op):
                return False
            new_index = op(modes)
            if new_index > -1:
                self._index = new_index
            else:
                self._index += inst_length

    def _add(self, modes):
        noun, verb, dest = self._get_parameter_tuple(modes, size=3, dest_index=2)
        self._logger.debug(f'Add: {noun}+{verb}=>{dest}')
        self._instructions[dest] = noun + verb
        return -1

    def _multiply(self, modes):
        noun, verb, dest = self._get_parameter_tuple(modes, size=3, dest_index=2)
        self._logger.debug(f'Multiply: {noun}*{verb}=>{dest}')
        self._instructions[dest] = noun * verb
        return -1

    def _input(self, modes):
        number = self._phase_signal_pair.pop(0)
        dest, = self._get_parameter_tuple(modes, size=1, dest_index=0)
        self._logger.debug(f'Input: {number}=>{dest}')
        self._instructions[dest] = int(number)
        return -1

    def _output(self, modes):
        res, = self._get_parameter_tuple(modes, size=1)
        self._logger.debug(f'Output: {res}')
        self.output_history.append(res)
        self.result = res
        return -1

    def _jump_if_true(self, modes):
        noun, verb = self._get_parameter_tuple(modes, size=2)
        if noun != 0:
            self._logger.debug(f'Jump If True: Jumping to {verb}')
            return verb
        self._logger.debug('Jump If True: Not Jumping')
        return -1

    def _jump_if_false(self, modes):
        noun, verb = self._get_parameter_tuple(modes, size=2)
        if noun == 0:
            self._logger.debug(f'Jump If False: Jumping to {verb}')
            return verb
        self._logger.debug('Jump If False: Not Jumping')
        return -1

    def _less_than(self, modes):
        noun, verb, dest = self._get_parameter_tuple(modes, size=3, dest_index=2)
        self._logger.debug(f'Jump If False: {verb == 0}')
        if noun < verb:
            self._instructions[dest] = 1
        else:
            self._instructions[dest] = 0
        return -1

    def _equals(self, modes):
        noun, verb, dest = self._get_parameter_tuple(modes, size=3, dest_index=2)
        self._logger.debug(f'Equals: {noun}=={verb}=>{dest}')
        if noun == verb:
            self._instructions[dest] = 1
        else:
            self._instructions[dest] = 0
        return -1

    def _relative_base_offset(self, modes):
        noun, = self._get_parameter_tuple(modes, size=1)
        self._relative_offset += noun
        self._logger.debug(f'Relative Base Offset: {noun} => {self._relative_offset}')
        return -1

    def _get_parameter_tuple(self, modes, size, dest_index=None):
        params = []
        for i in range(size):
            value = self._instructions.get(self._index+i+1, 0)
            param = self._get_value(value, modes[i*-1-1], i == dest_index)
            params.append(param)
        return tuple(params)

    def _get_value(self, value, mode, is_dest):
        if mode == "0":  # position
            if is_dest:
                return value
            return self._instructions.get(value, 0)
        if mode == "1":  # immediate
            return value
        if mode == "2":  # relative
            if is_dest:
                return value + self._relative_offset
            return self._instructions.get(value + self._relative_offset, 0)
        raise Exception(f"Invalid Mode {mode}")

    def _should_wait_for_input(self, op):
        return op == self._input and not self._phase_signal_pair
