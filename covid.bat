@echo off
cd covid-19-data
git pull
cd ..
python3 src\panhandle.py
python3 src\reformat.py