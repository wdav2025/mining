# Pubmed API info: https://www.ncbi.nlm.nih.gov/books/NBK25499/#_chapter4_ESearch_

# Search two terms using + sign
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
cochlea+AND+utricle+OR\
+semicircular+canal\
&retstart=0\
&retmax=60\
&tool=biomed3&\
retmode=json"
