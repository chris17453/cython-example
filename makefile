#make file for cython example

.PHONY: all clean build install

all: clean build install

clean:
	@echo "Cleaning"
	@rm dist/*.gz -f
	@rm chello/*.c -rf
	@rm chello/*.so -rf


build:
	@echo "Building"
	@./bump.sh
	@python setup.py build_ext  sdist  


install:
	@echo "Installing"
	@pip install . --user

