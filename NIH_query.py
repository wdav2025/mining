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
    "limit": 4,
    "sort_field": "appl_id",
    "sort_order": "desc"
 }

r = requests.post(endpoint, json=query_payload)

# print(f"STATUS CODE: {r.status_code}")

# print(" ----- (response) -----")


import json

time.sleep(2)

print(json.dumps(r.json()))
