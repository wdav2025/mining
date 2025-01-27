# Pubmed API info: https://www.ncbi.nlm.nih.gov/books/NBK25499/#_chapter4_ESearch_

#Pull UIDs for all anatomical terms relating to the inner ear from 1825 to 2025, and exclude non-ear related terms like protstatic utricle and laryngeal saccule (63611 hits)
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
cochlea+OR\+basilar+papilla+OR\+organ+of+corti+OR\+stria+vascularis+OR\+basilar+membrane+OR\+reissner's+membrane+OR\+spiral+ganglion+OR\
\vestibular+labyrinth+OR\+semicircular+canal+OR\+vestibular+macula+OR\+otolith+OR\+crista+ampullaris+OR\+utricle+OR\+saccule+NOT\
+prostatic+NOT\+laryngeal\
&datetype=pdat\
&mindate=1825\
&maxdate=2025\
&retstart=0\
&retmax=60\
&tool=biomed3&retmode=json"

#Return Cochlear/Auditory hits only, but exclude all vestibular (34,320 hits)
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
cochlea+OR\+basilar+papilla+OR\+organ+of+corti+OR\+stria+vascularis+OR\+basilar+membrane+OR\+reissner's+membrane+OR\+spiral+ganglion+NOT\
\vestibular+labyrinth+NOT\+semicircular+canal+NOT\+vestibular+macula+NOT\+otolith+NOT\+crista+ampullaris+NOT\+utricle+NOT\+saccule+NOT\
+prostatic+NOT\+laryngeal\
&datetype=pdat\
&mindate=1825\
&maxdate=2025\
&retstart=0\
&retmax=60\
&tool=biomed3&retmode=json"

#Return Vestibular Hits Only (27,282 hits)
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
\vestibular+labyrinth+OR\+semicircular+canal+OR\+vestibular+macula+OR\+otolith+OR\+crista+ampullaris+OR\+utricle+OR\+saccule+NOT\
cochlea+NOT\+basilar+papilla+NOT\+organ+of+corti+NOT\+stria+vascularis+NOT\+basilar+membrane+NOT\+reissner's+membrane+NOT\+spiral+ganglion+NOT\
\+prostatic+NOT\+laryngeal\
&datetype=pdat\
&mindate=1825\
&maxdate=2025\
&retstart=0\
&retmax=60\
&tool=biomed3&retmode=json"

#Pull UIDs for all auditory/Cochlear AND vestibular terms 1825 to 2025, and exclude non-ear related terms like protstatic utricle and laryngeal saccule (17514 hits)
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=\
cochlea+OR\+basilar+papilla+OR\+organ+of+corti+OR\+stria+vascularis+OR\+basilar+membrane+OR\+reissner's+membrane+OR\+spiral+ganglion+AND\
\vestibular+labyrinth+OR\+semicircular+canal+OR\+vestibular+macula+OR\+otolith+OR\+crista+ampullaris+OR\+utricle+OR\+saccule+NOT\
+prostatic+NOT\+laryngeal\
&datetype=pdat\
&mindate=1825\
&maxdate=2025\
&retstart=0\
&retmax=60\
&tool=biomed3&retmode=json"

