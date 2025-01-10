import requests
"""This downloads the example paper in BioC format to a file called output.json



Instructions

https://www.ncbi.nlm.nih.gov/research/bionlp/APIs/BioC-PMC/

>  PubMed Central Open Access in BioC format (click here for accessing PubMed articles)
>    
>  All the PubMed Central (PMC) Open Access articles are available in the BioC format. This provides a large number of full text research articles for text mining and information retrieval research. BioC is a simple format designed for straightforward text processing. These articles are available in BioC XML or BioC JSON, in Unicode or ASCII, and via PubMed ID or PMC ID.
>  
>  If you use this resource, please cite:
>  
>  Comeau DC, Wei CH, Islamaj Doğan R, and Lu Z. PMC text mining subset in BioC: about 3 million full text articles and growing, Bioinformatics, btz070, 2019.


"""

url = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC1790863/unicode"

url = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC39718472/unicode"

response = requests.get(url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    with open('output.json', 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

