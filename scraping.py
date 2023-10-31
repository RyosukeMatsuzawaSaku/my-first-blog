import requests
from bs4 import BeautifulSoup
import re

# 対象のサイトのダウンロード
url = 'https://news.yahoo.co.jp'
res = requests.get(url)

# 扱える形に変換
soup = BeautifulSoup(res.text, "html.parser")
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

for elem in elems:
    print(elem.contents[0])
    print(elem.attrs['href'])