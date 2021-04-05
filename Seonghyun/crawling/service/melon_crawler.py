from bs4 import BeautifulSoup
import requests

class MelonCrawler:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'}

    def crawl(self, *args):
        url = args[0]
        r = requests.get(url, headers=self.headers)

        if r.status_code != 200:
            return 'http request failed'
        else:
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            song_info = soup.select('#frm > div > table > tbody > tr > td:nth-child(4) > div > div')

            top_list = []
            for i in range(100):
                song = song_info[i].select('div > div.ellipsis.rank01 > span > a')[0].text
                singer_set = song_info[i].select('div > div.ellipsis.rank02 > a')

                singerGrp = ''

                for singer in singer_set:
                    if singerGrp != '':
                        singerGrp += ', '
                    singerGrp += singer.text

                top_list.append((song, singerGrp))

            return top_list
