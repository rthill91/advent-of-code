YEAR = 2019
DAY ?= 11
RUNNER := cd "aoc$(YEAR)" &&
POETRY_RUNNER := $(RUNNER) poetry run
INTCODE_DAYS = "day02 or day05 or day07 or day09"

.PHONY: run
run: part1 part2

.PHONY: part1
part1:
	@echo "\nPART 1:"
	-@$(POETRY_RUNNER) day${DAY}p1
	@echo "\n========================\n"

.PHONY: part2
part2:
	@echo "PART 2:"
	-@$(POETRY_RUNNER) day${DAY}p2
	@echo "\n========================\n"


.PHONY: test
test:
	@$(POETRY_RUNNER) pytest -vv -k day${DAY}


.PHONY: test-all
test-all:
	@$(POETRY_RUNNER) pytest -vv


.PHONY: tests
tests: test


.PHONY: test-intcode
test-intcode:
	@$(POETRY_RUNNER) pytest -vv -k ${INTCODE_DAYS}
