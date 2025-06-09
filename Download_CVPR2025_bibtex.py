import sys
import requests
import urllib
from bs4 import BeautifulSoup
import bibtexparser

# WACV 2023网站链接
url = "https://openaccess.thecvf.com/CVPR2025?day=all"

# 发送请求获取网页内容
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html5lib')

# 查找所有文章
papers = soup.find_all(attrs={'class': 'bibref'})
print(papers)

with open("cvpr2025_bibtex.txt", "w", encoding='utf-8') as f:
    # 遍历文章并获取Bibtex
    for paper in papers:
        bib_data = bibtexparser.loads(paper.text.replace('<br>', "").strip())
        f.write(bibtexparser.dumps(bib_data))