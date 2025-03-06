import json
import requests
import time
import sqlite3

endpoint = "https://api.reporter.nih.gov/v2/projects/search"

# make the database --------------------------------
database = sqlite3.connect("response_data.db")
with open('schema.sql', 'r') as f:
    database.executescript(f.read())
# make the database --------------------------------


query_payload = {
        "criteria": {
            "advanced_text_search": { "search_field": "terms,projecttitle", "search_text": "(cochlea OR \"basilar papilla\" OR \"organ of corti\" OR \"stria vascularis\" OR \"basilar membrane\" OR \"vestibular labyrinth\" OR \"semicircular canal\" OR \"vestibular macula\" OR otolith OR crista ampullaris OR utricle)"}
            },
        "include_fields": [
            "FiscalYear", "ProjectNum"
            ],
        "offset": 0,
        "limit": 10,
        "sort_field": "appl_id",
        "sort_order": "desc"
        }


query_payload = {
        "criteria": {
            "advanced_text_search": { "search_field": "terms,projecttitle", "search_text": "(cochlea OR \"basilar papilla\" OR \"organ of corti\" OR \"stria vascularis\" OR \"reissner membrane\" OR \"spiral ganglion\" OR \"basilar membrane\" OR \"vestibular labyrinth\" OR \"semicircular canal\" OR \"vestibular macula\" OR \"otolith\" OR \"crista ampullaris\" OR  \"utricle\" NOT \"prostatic\" NOT \"pharyngeal\")"}
            },
        "include_fields": [
            "FiscalYear", "ProjectNum", "ActivityCode","AwardType","Organization", "AwardAmount", "AbstractText"
            ],
        "offset": 0,
        "limit": 10,   # should be 500
        "sort_field": "project_start_date",
        "sort_order": "desc"
        }

def make_request(q):
    r = requests.post(endpoint, json=q)
    return r

    # print(f"STATUS CODE: {r.status_code}")

    # print(" ----- (response) -----")

    #total_results = r.json()['meta']['total']


    time.sleep(2)

#print(json.dumps(r.json()))


#for i in range(10):
total_results = 90
step = 10

#for i in range(0, ((total_results + step ) // step) * step, step ):
for i in range(1):

    query_payload['offset'] = i

    r = make_request(query_payload)
    print(json.dumps(r.json()))


 #  with open("data.json", "a+") as outfile:
 #      outfile.write(json.dumps(r.json()))
 #  time.sleep(6)
