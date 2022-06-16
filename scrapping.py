import requests
# 스크래핑용 모듈
from bs4 import BeautifulSoup
import json
import os
import sys

# 파이썬 파일 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('스크래핑 시작')

req = requests.get('https://www.yna.co.kr/theme/headlines-history')
req.encoding = None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
# 가져올 Web JS Tag 경로
datas = soup.select(
    '#container > div > div:nth-child(2) > section > div > ul > li > div > div.news-con > a.tit-wrap'
)
res = {}
print(datas)
for title in datas:
    # 태그.text, tag의 href 가져오기
    name = title.text
    url = 'http:' + title['href']
    res[name] = url

# json 저장
with open(os.path.join(BASE_DIR, 'news.json'), 'w+', encoding='utf-8') as json_file:
    json.dump(res, json_file, ensure_ascii = False, indent='\t')

print('스크래핑 끝')