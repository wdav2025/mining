# Pubmed API info: https://www.ncbi.nlm.nih.gov/books/NBK25499/#_chapter4_ESearch_

# Search boolean terms
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
cochlea+OR+utricle\
&datetype=pdat\
&mindate=1800/01/01\
&maxdate=3000/01/01\
&dbfrom=pubmed\
&tool=biomed3&\
&retmode=json"


# # Search boolean terms
# curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
# +covid19\
# &datetype=edat\
# &mindate=1880\
# &maxdate=2015\
# &tool=biomed3&\
# &retmode=json"
