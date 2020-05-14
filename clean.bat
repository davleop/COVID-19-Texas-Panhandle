@echo off

REM clean up graphs, Texas, and Panhandle directories

rmdir /S /Q graphs
rmdir /S /Q Panhandle
rmdir /S /Q Texas
del /f temp.csv

echo Done.