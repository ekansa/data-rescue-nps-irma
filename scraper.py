#! /usr/bin/env python3
import json
import codecs
import time
import re, os, requests
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def main(output_dir):
    """
    This is where you write your scraping scripts. Belowe are some commented
    out sections that have example scripts to get started for various types of
    situations. Just uncomment the section that you need and start coding!
    """

    """
    Eric Kansa scraping notes here:
    
    """
    search_urls = [
        # search term: 'climate' 6343 results
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=climate&Linked=false&page=1&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=climate&Linked=false&page=2&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=climate&Linked=false&page=3&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=climate&Linked=false&page=4&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=climate&Linked=false&page=5&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=climate&Linked=false&page=6&start=0&limit=1000',
        # search term: 'data' 34586 results
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=1&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=2&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=3&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=4&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=5&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=6&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=7&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=8&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=9&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=10&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=11&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=12&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=13&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=14&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=15&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=16&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=17&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=18&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=19&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=20&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=21&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=22&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=23&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=24&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=25&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=26&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=27&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=28&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=29&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=30&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=31&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=32&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=33&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=34&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=data&Linked=false&page=35&start=0&limit=1000',
        # search term: 'archaeology' (also archeology, seems to be the same) 2013 results
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=archaeology&Linked=false&page=1&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=archaeology&Linked=false&page=2&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=archaeology&Linked=false&page=3&start=0&limit=1000',
        # search term: 'endangered' 3114 results
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=endangered&Linked=false&page=1&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=endangered&Linked=false&page=2&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=endangered&Linked=false&page=3&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=endangered&Linked=false&page=4&start=0&limit=1000',
        # search term: 'oil + gas' 1206 result
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=oil+gas&Linked=false&page=1&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=oil+gas&Linked=false&page=2&start=0&limit=1000',
        # search term: 'contamination' 1030 results
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=contamination&Linked=false&page=1&start=0&limit=1000',
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=contamination&Linked=false&page=2&start=0&limit=1000',
        # search term: 'inholding' 64 results
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=inholding&Linked=false&page=1&start=0&limit=1000',
        # search term: 'enclave' 30 results
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=enclave&Linked=false&page=1&start=0&limit=1000',
        # search term: 'tribal' 261 results
        'https://irma.nps.gov/DataStore/Search/QuickSearch?Text=tribal&Linked=false&page=1&start=0&limit=1000',
    ]
    item_ids = None
    item_ids_json_file = os.path.join(output_dir, 'item_ids.json')
    if os.path.exists(item_ids_json_file):
        # we already saved a list of the items we want to save
        item_ids = json.load(codecs.open(item_ids_json_file, 'r'))
    if item_ids is None:
        item_ids = []  # ids of individual items we want to archive
        for url in search_urls:
            # slight delay between requests
            time.sleep(.5)
            print('Working on: ' + url)
            try:
                r = requests.get(url, timeout=20)
                r.raise_for_status()
                json_r = r.json()
            except:
                json_r = None
            if isinstance(json_r, dict):
                # we got results
                if 'Results' in json_r:
                    for r_item in json_r['Results']:
                        if 'Downloadability' in r_item and 'Id' in r_item:
                            if r_item['Downloadability'] == 'Public':
                                # the item is public for download
                                if r_item['Id'] not in item_ids:
                                    # no duplicates
                                    item_ids.append(r_item['Id'])
            # OK, now save the discovered IDs, URL by URL
            json_str = json.dumps(item_ids, ensure_ascii=False)
            file = codecs.open(item_ids_json_file, 'w', 'utf-8')
            file.write(json_str)
            file.close()
    else:
        # we already saved a list of the items we want to save
        item_ids = json.load(codecs.open(item_ids_json_file, 'r'))
    item_html_base_url = 'https://irma.nps.gov/DataStore/Reference/Profile/'
    files_json_base_url = 'https://irma.nps.gov/DataStore/Reference/GetHoldings?referenceId='
    if isinstance(item_ids, list):
        # we successfully have a list of items to archive
        print('Process ' + str(len(item_ids)) + ' items.')
        item_ids = sorted(item_ids)
        for id in item_ids:
            item_dir = os.path.join(output_dir, str(id))
            if not os.path.exists(item_dir):
                os.makedirs(item_dir)
            if os.path.exists(item_dir):
                # ok to download and get stuff
                # 1. file for the HTML of the item profile / description
                json_item_file = os.path.join(item_dir, (str(id) + '-meta-profile.json'))
                html_file = os.path.join(item_dir, (str(id) + '-profile.html'))
                if not os.path.exists(json_item_file):
                    if not os.path.exists(html_file):
                        html_str = None
                        # slight delay between requests
                        time.sleep(.5)
                        try:
                            item_html_url = item_html_base_url + str(id)
                            print('Get HTML Item profile: ' + item_html_url)
                            r = requests.get(item_html_url, timeout=20)
                            r.raise_for_status()
                            html_str = r.text
                        except:
                            html_str = None
                        if html_str is not None:
                            # save the HTML profile / description for the item
                            print('Saving HTML profile file.')
                            file = codecs.open(html_file, 'w', 'utf-8')
                            file.write(html_str)
                            file.close()
                    if os.path.exists(html_file):
                        content = None
                        with codecs.open(html_file, 'r', 'utf-8') as f:
                            content = f.readlines()
                        if content is not None:
                            if len(content) > 146:
                                json_ln = content[145].strip()
                                json_prof = json_ln.replace('var pageModel = NPSDataStoreReferenceCoreModel.modelSerialize(',
                                                            '')
                                last_json_prof = len(json_prof) - 2
                                json_prof = json_prof[0:last_json_prof]
                                # print(json_prof)
                                profile_dict = json.loads(json_prof)
                                if isinstance(profile_dict, dict):
                                    print('Saving JSON item profile for: ' + str(id))
                                    json_str = json.dumps(profile_dict, indent=4, ensure_ascii=False)
                                    file = codecs.open(json_item_file, 'w', 'utf-8')
                                    file.write(json_str)
                                    file.close()
                                    # delete the HTML file, don't need it
                                    os.remove(html_file)
                # 2. file for the JSON file manifest
                files_list_file = os.path.join(item_dir, (str(id) + '-files.json'))
                if not os.path.exists(files_list_file):
                    # we don't have the files manifest json
                    # slight delay between requests
                    json_r = None
                    files_json_url = files_json_base_url + str(id)
                    # slight delay between requests
                    time.sleep(.5)
                    try:
                        print('Get JSON file manifest: ' + files_json_url)
                        r = requests.get(files_json_url, timeout=20)
                        r.raise_for_status()
                        json_r = r.json()
                    except:
                        json_r = None
                    if json_r is not None:
                        # save the JSON file manifest
                        print('Saving JSON file manifest.')
                        json_str = json.dumps(json_r, indent=4, ensure_ascii=False)
                        file = codecs.open(files_list_file, 'w', 'utf-8')
                        file.write(json_str)
                        file.close()
                # if we have the files_list, open it as JSON
                do_files = False
                if os.path.exists(files_list_file) and do_files:
                    item_files = json.load(codecs.open(files_list_file, 'r'))
                    print('Checking downloads of ' + str(len(item_files)) + ' files')
                    for file_dict in item_files:
                        file_name = None
                        if 'FileDescription' in file_dict:
                            # file name provided for the resource
                            file_name = file_dict['FileDescription']
                        else:
                            # no file name, so make one from its id
                            file_name = 'file-id-' + str(file_dict['Id'])
                        if not isinstance(file_name, str):
                            # no file name, so make one from its id
                            file_name = 'file-id-' + str(file_dict['Id'])
                        file_path_name = os.path.join(item_dir, file_name)
                        if not os.path.exists(file_path_name):
                            # we don't have the file, so download it
                            # slight delay between requests
                            time.sleep(.25)
                            file_url = file_dict['Url']
                            url_ok = None
                            try:
                                # send a head request first
                                r = requests.head(file_url, timeout=20)
                                if r.status_code == 200:
                                    url_ok = True
                                else:
                                    url_ok = False
                            except:
                                # some sort of problem
                                url_ok = False
                            if url_ok:
                                # OK! we're good to try to get the file
                                # we should stream the request, some of these
                                # are really big
                                # slight delay between requests
                                time.sleep(.5) 
                                r = requests.get(file_url, stream=True)
                                if r.status_code == 200:
                                    with open(file_path_name, 'wb') as f:
                                        for chunk in r.iter_content(1024):
                                            f.write(chunk)
                                    f.close()
    print("Done!")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="""
This is diafygi's scraping script for the 2017 DataRescueSFBay event.
Example Usage: python3 scraper.py --output ../data/
""")
    parser.add_argument('--output', required=True, help='output directory')
    args = parser.parse_args()
    main(args.output)

