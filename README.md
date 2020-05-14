# COVID-19 Texas Panhandle

Graphing mechanisms for COVID-19 in the Texas Panhandle.

## Description

This is for the people of the Texas Panhandle. It simply just graphs the information given by the DSHS.<br>
Note: Some of the data is calculated and may be calculated incorrectly. If you find conflicting information, please just use the DSHS's data over these graphs. <br>
I don't know how fatalities goes down either. I'm just representing the data the DSHS has provided.<br>
*** WORK IN PROGRESS ***

## Dependencies

* [Python 3](https://www.python.org/)
* [cURL](https://curl.haxx.se/download.html)

## Installing

* `git clone https://github.com/davleop/COVID-19-Texas-Panhandle.git`
* `cd COVID-19-Texas-Panhandle`
* `pip install -r requirements.txt`

## Executing program

If using Windows, just use the `run.bat` file. <br>
If using Linux, use the `run.sh` file. <br>
Outputs are in the `graphs` and `png` directories.

## Screenshots

You should find all the save images in the `graphs` directory when the program is run.

![Panhandle Cases](png/PanhandleCases.png)
![Panhandle Fatalities](png/PanhandleFatalities.png)
![New Cases Aggregate](png/NewCasesAggregated.png)
![Active Aggregate](png/ActiveCasesEstimateAggregated.png)
![Cases Aggregate](png/CasesAggregated.png)
![Fatalities Aggregate](png/FatalitiesAggregated.png)
![New Cases Aggregate Bar](png/NewCasesAggregatedBar.png)
![Active Aggregate Bar](png/ActiveCasesEstimateAggregatedBar.png)
![Cases Aggregate Bar](png/CasesAggregatedBar.png)
![Fatalities Aggregate Bar](png/FatalitiesAggregatedBar.png)
![Actives](png/ActiveCasesEstimate.png)
![Cases](png/Cases.png)
![Fatalities](png/Fatalities.png)
![New Cases](png/NewCases.png)
![New Cases Bar](png/NewCasesBar.png)
![Cases Bar](png/CasesBar.png)
![Fatalities Bar](png/FatalitiesBar.png)

## Help

You can ping me through [Twitter](https://twitter.com/_D2P2_) if you need help or [Create an Issue](https://github.com/davleop/COVID-19-Texas-Panhandle/issues)

## Known Issue

Before running the program, you need to go to [this](https://tabexternal.dshs.texas.gov/t/THD/views/COVIDExternalQC/COVIDTrends?:isGuestRedirectFromVizportal=y&:embed=y) website and copy the data downlaod link, specifically the "Full data." From there you can copy and paste the URL into the `newCases` varaible in the `run` program. It should work from there. The DSHS isn't very user-friendly with that date for unknown reasons.

## Author

David Penn <br>
Twitter: [@\_D2P2\_](https://twitter.com/_D2P2_)

## License

This project is licensed under the Creative Commons Legal Code License - see the LICENSE.md file for details.
