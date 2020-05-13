@echo off
set casesOverTime=https://www.dshs.state.tx.us/coronavirus/TexasCOVID19DailyCountyCaseCountData.xlsx
set fatalOverTime=https://www.dshs.state.tx.us/coronavirus/TexasCOVID19DailyCountyFatalityCountData.xlsx
set activeOverTime=https://www.dshs.state.tx.us/coronavirus/TexasCOVID-19ActiveCaseDatabyCounty.xlsx
set cumulativeTest=https://www.dshs.state.tx.us/coronavirus/COVID-19CumulativeTestTotalsbyCounty.xlsx

cd Texas
curl %casesOverTime% --output CaseCountData.xlsx -s
curl %fatalOverTime% --output FatalityCountData.xlsx -s
curl %activeOverTime% --output ActiveCaseData.xlsx -s 
curl %cumulativeTest% --output CumulativeTestTotals.xlsx -s 
cd ..

python3 src_dshs\panhandle.py