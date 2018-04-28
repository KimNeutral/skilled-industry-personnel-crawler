import requests
from bs4 import BeautifulSoup
import re

regex = r"(?<=\/)(\d+(?= 페이지))"

p = re.compile(regex)


class Company:
    def __init__(self):
        self.name = ''
        self.linkage = False
        self.provincial_office = ''
        self.is_employing = False

    def setData(self, name, linkage, provincial_office, is_employing):
        self.name = name
        if linkage == '참여':
            self.linkage = True
        self.provincial_office = provincial_office
        if is_employing == '모집중':
            self.is_employing = True


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
            company = Company()
            ls = tr.find_all('td')
            company.setData(tr.find('th').text, ls[0].text, ls[1].text, ls[2].text)

            print(f'{company.name}, {company.linkage}, {company.provincial_office}, {company.is_employing}')


spider()
