@echo off
REM TODO(David): change to just update data
IF EXIST covid-19-data (
cd covid-19-data
git pull
cd ..
python3 src\panhandle.py
python3 src\reformat.py
python3 src\graph.py
) ELSE (
python3 src\panhandle.py
python3 src\reformat.py
python3 src\graph.py
)