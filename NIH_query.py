import json
import requests
import time

endpoint = "https://api.reporter.nih.gov/v2/projects/search"

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

def make_request(q):
    r = requests.post(endpoint, json=q)
    return r

    # print(f"STATUS CODE: {r.status_code}")

    # print(" ----- (response) -----")

    #total_results = r.json()['meta']['total']


    #time.sleep(2)

#print(json.dumps(r.json()))


#for i in range(10):
total_results = 90
step = 10

for i in range(0, ((total_results + step ) // step) * step, step ):

    query_payload['offset'] = i
    print(query_payload['offset'])

    r = make_request(query_payload)


    with open("data.json", "a+") as outfile:
        outfile.write(json.dumps(r.json()))
    time.sleep(6)
