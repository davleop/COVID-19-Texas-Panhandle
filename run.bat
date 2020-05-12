@echo off
IF EXIST covid-19-data (
cd covid-19-data
git pull
cd ..
python3 src\panhandle.py
python3 src\reformat.py
python3 src\graph.py
) ELSE (
git clone https://github.com/nytimes/covid-19-data.git
python3 src\panhandle.py
python3 src\reformat.py
python3 src\graph.py
)