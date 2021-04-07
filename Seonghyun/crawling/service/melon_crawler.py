from bs4 import BeautifulSoup
import requests

class MelonCrawler:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'}

    # melon crawling Function
    def crawl(self, *args):

        # melon chart url
        url = args[0]

        # GET request (using requests library)
        r = requests.get(url, headers=self.headers)

        if r.status_code != 200:
            return 'http request failed'
        else:
            # html string
            html = r.text

            # BeautifulSoup Constructor : BeautifulSoup(markup, parser)
            # return : BeautifulSoup Object (represents the parsed document as a whole)

            # "html.parser" : Python’s standard library
            soup = BeautifulSoup(html, 'html.parser')

            # select(selector) : returns a object ResultSet.
            # selector : css selector.

            # select song information (노래 제목은 1개, 가수는 1명 이상)
            song_info = soup.select('#frm > div > table > tbody > tr > td:nth-child(4) > div > div')

            top_list = []
            for i in range(100):
                # 노래 제목은 1개
                song = song_info[i].select('div > div.ellipsis.rank01 > span > a')[0].text
                # 가수는 1명 이상
                singer_set = song_info[i].select('div > div.ellipsis.rank02 > a')

                singerGrp = ''

                # 가수가 여러명일 경우, ',' 로 연결
                for singer in singer_set:
                    if singerGrp != '':
                        singerGrp += ', '
                    singerGrp += singer.text

                # (노래제목, 가수) 튜플 형태로 list 에 append
                top_list.append((song, singerGrp))

            return top_list
