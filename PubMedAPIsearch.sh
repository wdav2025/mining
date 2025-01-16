# Pubmed API info: https://www.ncbi.nlm.nih.gov/books/NBK25499/#_chapter4_ESearch_

# Search boolean terms for all iner ear related papers (need to adjust total output "retmax" to by incremental ranges )
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
cochlea+OR\+semicircular+canal+OR\+basilar+papilla+OR\
+vestibular+macula+OR\
+otolith+OR\
+crista+ampullaris+OR\
+organ+of+corti+OR\
+utricle+saccule+NOT\
+prostatic\
&retstart=0\
&retmax=60\
&tool=biomed3&retmode=json"

#Return Cochlea Hits Only 
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
cochlea+OR\+basilar+papilla+OR\
+organ+of+corti+NOT\
+utricle+saccule+NOT\
+vestibular+macula+NOT\
+otolith+NOT\
+crista+ampullaris+NOT\
+semicircular+canal+NOT\
+prostatic\
&retstart=0\
&retmax=60\
&tool=biomed3&retmode=json"

#Return Vestibular Hits Only 
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
+semicircular+canal+OR\
+vestibular+macula+OR\
+otolith+OR\
+crista+ampullaris+OR\
+utricle+saccule+NOT\
+prostatic+NOT\
cochlea+NOT\
+basilar+papilla+NOT\
+organ+of+corti+NOT\
&retstart=0\
&retmax=60\
&tool=biomed3&retmode=json"

#Date ranges (not yet specified for cmd...)
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
cochlea+OR\+semicircular+canal+OR\+basilar+papilla+OR\
+vestibular+macula+OR\
+otolith+OR\
+crista+ampullaris+OR\
+organ+of+corti+OR\
+utricle+saccule+NOT\
+prostatic\
&datetype=pdat\
&mindate=1825\
&maxdate=2025\
&retstart=0\
&retmax=60\
&tool=biomed3&retmode=json"
