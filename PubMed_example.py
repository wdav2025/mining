"""Example of URL encoding query"""
import urllib.parse
import requests

# Example of URL encoding a query
query = "(cochlea AND utricle) OR semicircular canals"



# Example of making the full url
base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

params = {
    'db': 'pubmed',
    'term': 'cochlea AND utricle',
    'retstart': 0,
    'retmax': 60,
    'tool': 'biomed3',
    'retmode': 'json'
}

encoded_params = urllib.parse.urlencode(params)

full_url = f"{base_url}?{encoded_params}"


def green(s):
    """Make text green"""
    return "\033[32m" + s + "\033[0m"


def print_examples():
    print(green("Query: ") + query)
    print(green("URL-encoded query: ") + urllib.parse.quote(query))
    print(green("Full URL: ") + full_url)

def run_query(query_url):
    """Actually using the query from above to get data from the API"""
    response = requests.get(query_url)
    if response.stats == 200:
        return response.text


print_examples()

# print(run_query(full_url))
