# About

Extract asteroid data from NASA NHATS.
This project uses python3.

# Usage

Send a curl call to extract a summary of available asteroid records:
```
curl https://ssd-api.jpl.nasa.gov/sentry.api > summary.txt
```

Using parseSummary.py, convert txt file into pretty json:
```
python 
>>> from parseSummary import txtToJson
>>> txtToJson('summary.txt')
```
This makes a json file called 'prettySummary.json' containing asteroid data summaries.

Using these summaries (in particular the des identifiers), extract more data for each asteroid.

```
python
>>> from parseSummary import summaryToFullData as s2d
>>> s2d('prettySummary.json')
```
This makes another file called 'fullData.json' which contains the availale asteroid data with summaries and further data.
