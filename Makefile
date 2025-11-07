#
# A Makefile for Homework 3 - STAT 259
#

# environment
.PHONY : env
env: environment.yml
	conda env update --file environment.yml

# html
.PHONY : html
html:
	myst build --html

# cleaning
.PHONY : clean
clean : 
	rm -rf figures/* audio/* _build/*