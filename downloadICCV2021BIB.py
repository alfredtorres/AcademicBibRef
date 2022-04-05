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

def get_context(url):
    web_context = requests.get(url)
    return web_context.text
url = 'http://openaccess.thecvf.com/ICCV2021?day=all'
web_context = get_context(url)

data = BeautifulSoup(web_context, "html5lib")
jar_bib = data.find_all(attrs={'class': 'bibref'})
print(jar_bib)
with open('ICCV2021.bib', 'w', encoding='utf-8') as f:
    for bib_data in jar_bib:
        # Get bib
        bib_data = bibtexparser.loads(bib_data.text.replace('<br>', "").strip())
        f.write(bibtexparser.dumps(bib_data))
        #tqdm.write(paper_url.a.text)
'''
link_list = re.findall(r"(?<=href=\").+?pdf(?=\">pdf)|(?<=href=\').+?pdf(?=\">pdf)",web_context)
name_list = re.findall(r"(?<=2021_paper.html\">).+(?=</a>)",web_context)
local_dir = 'D:\\Papers\\ICCV_2021\\'
if not os.path.exists(local_dir):
    os.makedirs(local_dir)
cnt = 0
while cnt < len(link_list):
    file_name = name_list[cnt]
    download_url = link_list[cnt]
#    download_url = re.sub('[:\?/]+',"_",file_name).replace(' ','_')
    #为了可以保存为文件名，将标点符号和空格替换为'_'
    file_name = re.sub('[:\?/]+',"_",file_name).replace('"','')
    file_path = local_dir + file_name + '.pdf'
    if os.path.exists(file_path):
        print('['+str(cnt)+'/'+str(len(link_list)) +']')
        cnt += 1
        continue
    else:
        #download
        print('['+str(cnt)+'/'+str(len(link_list))+'] Downloading' + file_path)
        try:
            urllib.request.urlretrieve("http://openaccess.thecvf.com/" + download_url, file_path)
        except Exception:
            print ('download Fail: ' + file_path)
        cnt += 1
print('Finished')
'''