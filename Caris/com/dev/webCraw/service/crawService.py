import requests
from com.dev.webCraw.util.contents import contents
from bs4 import BeautifulSoup
from com.dev.webCraw.service.dbSession import databaseSession
import datetime as date
from selenium import webdriver

# Wweb-Crawling-service.
class crawService:
    # init Func.
    def __init__(self, *args):
        self._site = args[0]

    # Crawling-Func.
    def crawler(self):
        # ------------ web-Crawling Start ------------ #
        try:
            results = {}
            con = contents(self._site)
            url = con.getUrl()
            html = requests.get(url, headers=contents.getHeader(self._site))

            # if google.
            if self._site == 'google':
                htmlTag = "head > title"
                _save = save(htmlTag, html)
                results = _save.toDb()
            # if naver.
            elif self._site == 'naver':
                htmlTag = "#s_content > div.section > ul > li:nth-child(1) > dl > dt > a"
                _save = save(htmlTag, html)
                results = _save.toDb()
            # if bugs musin chart.
            elif self._site == 'bugs':
                _save = save('None', html)
                results =_save.toDb()
            else:
                print(html.text)
                results = '500'
                # ------------ web-Crawling End ------------ #
        except Exception as e:
            print('[error] crawling service error..{}'.format(str(e)))
        return results

# Save DB transaction class.
class save:
    # init Func.
    def __init__(self, *args):
        self._htmlTag = args[0]
        self._html = args[1]

    # craw data save Func.
    def toDb(self):
        soup = BeautifulSoup(self._html.text, 'html.parser')
        # -------------- title namne craw -------------- #
        if self._htmlTag != 'None':
            title = soup.select_one(self._htmlTag)
            print('@@@ title : {}{}'.format(title.get_text(), ' @@@'))

            sql = """
                    INSERT INTO CRAW_BAS 
                        (CRAW_DATA, SYSTEM_DATE, DESCRIPTION) 
                      VALUES 
                       (%s, %s, %s)
                    """
            _db = databaseSession(title.get_text(), date.datetime.now(), 'Caris', sql)
            _statusCode = _db.connection()
            if _statusCode == '200':
                results = {
                    "statusCode": _statusCode,
                    "dataList": title.get_text()
                }
            else:
                results = {
                    "statusCode": _statusCode,
                    "dataList": 'error'
                }
            return results
        # -------------- bugs music hot chart -------------- #
        else:
            _title = soup.select('p.title')
            _artist = soup.select('p.artist')

            rank = {}
            for _i in range(len(_title)):
                rank[str(_i+1)+'위'] = _title[_i].get_text().strip() + ' : ' + _artist[_i].get_text().strip().replace('\n\n\r\n', '')
            print(rank)

            sql = """
                    INSERT INTO CRAW_BAS 
                        (CRAW_DATA, SYSTEM_DATE, DESCRIPTION) 
                      VALUES 
                       (%s, %s, %s)
                    """
            _db = databaseSession(str(rank), date.datetime.now(), 'Caris', sql)
            _db.connection()
            _statusCode = _db.connection()
            if _statusCode == '200':
                results = {
                    "statusCode": _statusCode,
                    "dataList": str(rank)
                }
            else:
                results = {
                    "statusCode": _statusCode,
                    "dataList": 'error'
                }
            return results
