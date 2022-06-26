.PHONY: all
all: install-deps icalnews.py icalnews.spec template.html
	pyinstaller icalnews.spec

.PHONY: install-deps
install-deps: requirements.txt
	pip install -r requirements.txt
