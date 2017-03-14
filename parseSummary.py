import json
import pdb
import requests

def txtToJson(inFile): 
    with open(inFile, 'rb') as f0:
        summary = f0.read()

    summary = json.loads(summary)
    with open('prettySummary.json', 'w') as f0:
        json.dump(summary, fp = f0, sort_keys = True,
                indent = 4, separators = (',',':'))

def summaryToFullData(summaryJSON):
    with open(summaryJSON, 'rb') as f0:
        summary = json.load(f0)
    newSummary = []
    for asteroidSummary in summary['data']:
        asteroidTmpDict = dict.fromkeys(['summary','data'])
        des = asteroidSummary['des'].lower().replace(' ','')
        r = requests.get('https://ssd-api.jpl.nasa.gov/sentry.api?des=' + des)
        rjson = json.loads(r.text)
        asteroidData = rjson['data']
        asteroidTmpDict['summary'] = asteroidSummary
        asteroidTmpDict['data'] = asteroidData
        newSummary.append(asteroidTmpDict)

    with open('fullData.json', 'w') as f0:
        json.dump(newSummary, fp = f0, sort_keys = True,
                indent = 4, separators = (',',':'))

    pdb.set_trace()

