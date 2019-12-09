NUM ?= 07
DAY := day-$(NUM)
RUNNER := cd $(DAY) &&

.PHONY: run
run: part1 part2

.PHONY: part1
part1:
	@echo "\nPART 1:"
	-@$(RUNNER) poetry run aoc1
	@echo "\n========================\n"

.PHONY: part2
part2:
	@echo "PART 2:"
	-@$(RUNNER) poetry run aoc2
	@echo "\n========================\n"
