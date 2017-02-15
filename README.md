README
======



Data Rescue: Metadata and File Manifests for the United States National Parks Service (NPS) IRMA Database
---------------------------------------------------------------------------------------------------------
The IRMA database is a publicly accessible repository of "items" published by the National Park Service (NPS). Each IRMA item has some metadata (especially title, description, suggested citation), and a manifest that provides metadata and URLs to download files. The files associated with IRMA items vary in format (many PDFs, but also XLS, various types of GIS files, and more). Many of the files have URLs belonging to IRMA itself, but some are URLs to resources elsewhere on the Web. In some causes the URLs to non-IRMA resources point to Web pages.

This repository is intended to facilitate download and archiving of IRMA data that needs safeguarding in this "Data Rescue" effort: 
http://www.archivers.space/urls/58EEC326-2A3D-495E-9B7C-E7CD6A70D6A9


scrapper.py
-----------
The scrapper.py file has the code used to:

1. Search IRMA with keywords to identifiy content that maybe at risk. These keywords include: "climate", "data", "archaeology", "endangered", "oil gas", "contamination", "inholding", "enclave" and "tribal". Each keword search resulted in a paged JSON formated response from IRMA. The code iterates through the search responses to get identifiers for items that are publicly accessible. The code also de-duplicates the results of these multiple searches.

2. Create directories for each IRMA item. The directories are named with the numeric IRMA ID assigned to each item identified in the searches described above.

3. Create metadata profile information for each IRMA item. The metadata for each IRMA item came from an HTML page included some javascript. The code downloaded these HTML metadata profile pages for each IRMA item. In the javascript of these HTML pages, a JSON formated string expressed item metadata. The code extracted this JSON text and saved the JSON formatted metadata as a file according to the following convention: "{id}-meta-profile.json"

4. Create file manifests for each IRMA item. IRMA provides a JSON formated manifest describing files associated with each item, including download URLs. The code requested these JSON file manifests and saved them as JSON files with the following naming convention: "{id}-files.json"


data.zip
-----------
The data.zip file contains the compressed results of the scapper.py code. It has 25,912 folders, one for each IRMA item identified with the keyword searches described above. Each IRMA item directory has a JSON formatted metadata profile file (named: "{id}-meta-profile.json"), and a JSON formatted file manifest (named: "{id}-files.json").


      


