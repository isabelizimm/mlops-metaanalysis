.PHONY: clean-pyc clean-build clean docs
UNAME := $(shell uname)


ifeq ($(UNAME), Darwin)
    BROWSER := open
else
    BROWSER := python -mwebbrowser
endif

help:
	@echo "get-topics-mlops - get all repos tagged mlops from GitHub REST API"


# TODO: make this iterate through everything to set up repo data and dump into new file
get-topics-mlops: 
	gh api \
	-H "Accept: application/vnd.github+json" \
	"/search/repositories?q=topic:mlops" > data/repositories.json
