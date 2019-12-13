YEAR = 2019
DAY ?= 10
RUNNER := cd "aoc$(YEAR)" &&
POETRY_RUNNER := $(RUNNER) poetry run

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


.PHONY: tests
tests:
	$(POETRY_RUNNER) pytest -vv
