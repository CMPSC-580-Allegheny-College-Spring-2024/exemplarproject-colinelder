# This directory is to store the data necessary for the project.

This directory contains a small amount of data that is pulled from the large corpus that this artifact parses through. This data consists of a large number of scholarly articles that pertain to all things science related. This provides a comprehensive and credible sources to check the inputted facts against. In order to obtain and set up this data, it will first need to be downloaded from PubMed. PubMed contains a large corpus of scientifically reviewed articles. The user can also download the information through this link:
https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/xml/oa_noncomm_xml.PMC001xxxxxx.baseline.2023-12-18.tar.gz

Since this is such a large corpus of data, it does not all fit into the github repository. For this reason the user needs to designate a path to it from the code. To adjust the path so that it reaches the data and connects it to the project, adjust this line of code based on where it is located in your computer.
```data_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Jsem_Data')```
 It is recommended that the data and the repository are located next to each other in the same folder, rather than the data being located in the repository itself.






