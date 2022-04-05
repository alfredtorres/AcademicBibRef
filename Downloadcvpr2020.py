# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:10:59 2020

@author: zzy
"""

import os
import re
import tqdm
import urllib
import requests
from bs4 import BeautifulSoup
import bibtexparser
from argparse import ArgumentParser


def get_context(url):
        web_context = requests.get(url)
        return web_context.text
        
def main(args):
    #url = os.path.join('http://openaccess.thecvf.com/', args.name + args.year + '?day=all')
    BASE_URL = 'https://openaccess.thecvf.com'
    url = 'http://openaccess.thecvf.com/CVPR2020'
    web_context = get_context(url)
    data = BeautifulSoup(web_context, "html5lib")
    sub_pages = data.find_all("a", text=lambda x: x and x.startswith("Day"))
    url_list = []
    for sub_url in sub_pages:
        url_list.append((f"{BASE_URL}/{sub_url['href']}", os.path.join(sub_url['href'] + ".html")))
    
    with open(args.name + args.year + '.bib', 'w', encoding='utf-8') as f:
        for item in url_list:
            web_context = get_context(item[0])
            data = BeautifulSoup(web_context, "html5lib")
            jar_bib = data.find_all(attrs={'class': 'bibref'})
            print(jar_bib)
            for bib_data in jar_bib:
                bib_data = bibtexparser.loads(bib_data.text.replace('<br>', "").strip())
                f.write(bibtexparser.dumps(bib_data))


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('name', type=str, help='Name')
    parser.add_argument('year', type=str, help='Year')
    return parser.parse_args()


if "__main__" == __name__:
    args = parse_args()
    main(args)