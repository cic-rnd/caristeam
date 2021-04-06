import requests
from bs4 import BeautifulSoup
import pandas as pd

from com.dev.webCraw.service.crawService import crawService
from com.dev.webCraw.service.dbSession import databaseSession

# web-Crawler Func.
# def getSite(site):
#     craw = crawService(site)
#     craw.crawler()

def getBugs():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'
    }
    html = requests.get('https://music.bugs.co.kr/chart', headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    _title = soup.select('p.title')
    _artist = soup.select('p.artist')

    # titleList = []
    # artistLsit = []
    #
    # for _i in range(len(_title)):
    #     titleList.append(str(_i+1) + "위 : " + _title[_i].get_text().strip())
    # for _i in range(len(_artist)):
    #     artistLsit.append(titleList[_i] + ": " + _artist[_i].get_text().strip().replace('\n\n\r\n', '|'))
    #
    # print(artistLsit)

    test = {}
    for _i in range(len(_title)):
        test[str(_i+1)+'위'] = _title[_i].get_text().strip() + ' / ' + _artist[_i].get_text().strip().replace('\n\n\r\n', '')
    print(test['2위'])

    for v in test.values():
        print(v)

    #


    # print(_title[0].get_text().strip())
    # print(_artist[0].get_text().strip())
    # total_List = {
    #     'title': '',
    #     'artist': ''
    # }
    #
    # for _i in range(len(_title)):
    #     total_List['title'] += str(_title[_i].get_text().strip())
    #     total_List['artist'] += str(_artist[_i].get_text().strip().replace('\n\n\r\n', '|'))
    #     if _i != len(_title)-1:
    #         total_List['title'] += '|'
    #         total_List['artist'] += '|'
    #     else:
    #         total_List['title'] += ''
    #         total_List['artist'] += ''
    # print(total_List)
    # return total_List

def pandasTest():
    df = pd.read_csv('/Users/seunghapark/Downloads/creditcard.csv')
    print(df)


# Test-Main Func.
if __name__ == '__main__':
    # getSite('google')
    getBugs()
    # pandasTest()
