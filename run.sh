#!/bin/bash

casesOverTime="https://www.dshs.state.tx.us/coronavirus/TexasCOVID19DailyCountyCaseCountData.xlsx"
fatalOverTime="https://www.dshs.state.tx.us/coronavirus/TexasCOVID19DailyCountyFatalityCountData.xlsx"
activeOverTime="https://www.dshs.state.tx.us/coronavirus/TexasCOVID-19ActiveCaseDatabyCounty.xlsx"
cumulativeTest="https://www.dshs.state.tx.us/coronavirus/COVID-19CumulativeTestTotalsbyCounty.xlsx"

mkdir -p Texas
mkdir -p Panhandle

cd Texas
curl $casesOverTime --output CaseCountData.xlsx -s
curl $fatalOverTime --output FatalityCountData.xlsx -s
curl $activeOverTime --output ActiveCaseData.xlsx -s
curl $cumulativeTest --output CumulativeTestTotals.xlsx -s
cd ..

python3 src_dshs/panhandle.py
python3 src_dshs/reformat.py