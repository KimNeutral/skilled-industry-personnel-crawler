import requests
from bs4 import BeautifulSoup
import re

regex = r"(?<=\/)(\d+(?= 페이지))"

p = re.compile(regex)


def spider():
    page = 1
    param = {
        'al_eopjong_gbcd': '11111',
        'eopjong_gbcd_list': '11111',
        'eopjong_gbcd': '1',
        'gegyumo_cd': '',
        'eopjong_cd': '11111',
        'eopche_nm': '',
        'sido_addr': '',
        'sigungu_addr': ''
    }

    url = 'https://work.mma.go.kr/caisBYIS/search/byjjecgeomsaek.do'
    r = requests.post(url, param);
    soup = BeautifulSoup(r.text, 'lxml')
    page += 1
    max_pages = int(p.search(soup.find(class_='topics').text).group())

    while page <= max_pages:
        url = 'https://work.mma.go.kr/caisBYIS/search/byjjecgeomsaek.do?pageIndex=' + str(page)
        r = requests.post(url, param);
        soup = BeautifulSoup(r.text, 'lxml')
        page += 1
        for tr in soup.find(class_='brd_list_n').find('tbody').select('tr'):
            print(tr.find('th').text, end=' ')
            for td in tr.find_all('td'):
                print(td.text, end=' ')
            print('\n')


spider()
