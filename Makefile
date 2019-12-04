NUM ?= 03
DAY := day-$(NUM)
RUNNER := cd $(DAY) &&

.PHONY: run
run:
	@echo "\nPART 1:"
	@$(RUNNER) poetry run aoc1
	@echo "\n========================\n"
	@echo "PART 2:"
	@$(RUNNER) poetry run aoc2
	@echo ""
