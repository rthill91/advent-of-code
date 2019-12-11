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
        }
        self.result = 0
        self.reset_state(phase_signal_pair)

    def add_inputs(self, inputs):
        self._phase_signal_pair.extend(inputs)

    def reset_state(self, phase_signal_pair):
        self._instructions = copy.copy(self._initial_instructions)
        self._phase_signal_pair = phase_signal_pair
        self._index = 0

    def compute(self):
        while self._index < len(self._instructions):
            inst = self._instructions[self._index]
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
            if new_index > 0:
                self._index = new_index
            else:
                self._index += inst_length

    def _add(self, modes):
        noun, verb, dest = self._get_noun_verb_dest_tuple(modes)
        self._logger.debug(f'Add: {noun}+{verb}=>{dest}')
        self._instructions[dest] = noun + verb
        return 0

    def _multiply(self, modes):
        noun, verb, dest = self._get_noun_verb_dest_tuple(modes)
        self._logger.debug(f'Multiply: {noun}*{verb}=>{dest}')
        self._instructions[dest] = noun * verb
        return 0

    def _input(self, modes):
        number = self._phase_signal_pair.pop(0)
        dest = self._instructions[self._index+1]
        self._logger.debug(f'Input: {number}=>{dest}')
        self._instructions[dest] = int(number)
        return 0

    def _output(self, modes):
        output_location = self._instructions[self._index+1]
        res = self._instructions[output_location]
        self._logger.debug(f'Output: {output_location}=>{res}')
        self.result = res
        return 0

    def _jump_if_true(self, modes):
        noun, verb, _ = self._get_noun_verb_dest_tuple(modes)
        self._logger.debug(f'Jump If True: {verb > 0}')
        if noun != 0:
            return verb
        return 0

    def _jump_if_false(self, modes):
        noun, verb, _ = self._get_noun_verb_dest_tuple(modes)
        if noun == 0:
            return verb
        return 0

    def _less_than(self, modes):
        noun, verb, dest = self._get_noun_verb_dest_tuple(modes)
        self._logger.debug(f'Jump If False: {verb == 0}')
        if noun < verb:
            self._instructions[dest] = 1
        else:
            self._instructions[dest] = 0
        return 0

    def _equals(self, modes):
        noun, verb, dest = self._get_noun_verb_dest_tuple(modes)
        self._logger.debug(f'Equals: {noun}=={verb}=>{dest}')
        if noun == verb:
            self._instructions[dest] = 1
        else:
            self._instructions[dest] = 0
        return 0

    def _get_noun_verb_dest_tuple(self, modes):
        noun = self._get_value(self._instructions[self._index+1], modes[-1])
        verb = self._get_value(self._instructions[self._index+2], modes[-2])
        dest = self._instructions[self._index+3]
        return (noun, verb, dest)

    def _get_value(self, value, mode):
        if mode == "0":
            return self._instructions[value]
        return value

    def _should_wait_for_input(self, op):
        return op == self._input and not self._phase_signal_pair



def _get_input():
    with open('input') as fh:
        return [int(inst) for inst in fh.readline().split(',')]
