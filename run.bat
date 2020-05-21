@echo off
set casesOverTime=https://www.dshs.state.tx.us/coronavirus/TexasCOVID19DailyCountyCaseCountData.xlsx
set fatalOverTime=https://www.dshs.state.tx.us/coronavirus/TexasCOVID19DailyCountyFatalityCountData.xlsx
set activeOverTime=https://www.dshs.state.tx.us/coronavirus/TexasCOVID-19ActiveCaseDatabyCounty.xlsx
set cumulativeTest=https://www.dshs.state.tx.us/coronavirus/COVID-19CumulativeTestTotalsbyCounty.xlsx
set CaseFatalCount=https://dshs.texas.gov/coronavirus/TexasCOVID19CaseCountData.xlsx
set newCases="https://tabexternal.dshs.texas.gov/vizql/t/THD/w/COVIDExternalQC/v/COVIDTrends/vud/sessions/D038F192EF174137BCD91F97DD9432B9-1:0/views/7020163219168008686_7295805493000846711?csv=true"

if not exist "Texas" (
	mkdir Texas
)

if not exist "Panhandle" (
	mkdir Panhandle
)

if not exist "graphs" (
	mkdir graphs
)

echo Collecting data...
cd Texas
curl %casesOverTime% --output CaseCountData.xlsx -s
curl %fatalOverTime% --output FatalityCountData.xlsx -s
curl %activeOverTime% --output ActiveCaseData.xlsx -s 
curl %cumulativeTest% --output CumulativeTestTotals.xlsx -s 
curl %CaseFatalCount% --output CaseFatalCount.xlsx -s
curl %newCases% --output NewCases.csv
cd ..

echo Reformatting data...
python3 src_dshs\panhandle.py
python3 src_dshs\reformat.py

echo Saving graphs to graphs directory...
python3 src_dshs\graph.py

echo Done.