NUM ?= 01
DAY := day-$(NUM)
RUNNER := cd $(DAY) &&

.PHONY: run
run:
	$(RUNNER) ls
