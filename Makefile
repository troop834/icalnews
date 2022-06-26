##
## icalnews - Makefile
##
## Copyright (C) 2022 Kian Kasad
##
## This file is made available under a modified BSD license.
## See the accompanying LICENSE file for details.
##

.PHONY: all
all: install-deps icalnews.py icalnews.spec template.html
	pyinstaller icalnews.spec

.PHONY: install-deps
install-deps: requirements.txt
	pip install -r requirements.txt
