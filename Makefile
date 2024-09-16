export PYTHONPATH = $(shell echo $PYTHONPATH):$(shell pwd)

run:
	python3 src/main.py