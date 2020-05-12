#!/bin/bash
# TODO(David): just update the data
if [ -d "covid-19-data" ]; then
	cd covid-19-data
	git pull
	cd ..
	python3 src/panhandle.py
	python3 src/reformat.py
	python3 src/graph.py
else
	git clone https://github.com/nytimes/covid-19-data.git
	python3 src/panhandle.py
	python3 src/reformat.py
	python3 src/graph.py
fi