from flask import Flask, render_template, request

from crawling.util.dbsession import *
import datetime as date
from crawling.service.melon_crawler import *
from crawling.service.query import *

# 모듈이름을 인자로 어플리케이션 객체 생성
app = Flask(__name__)

@app.route('/', methods=['GET'])
def webPage():
    return render_template('/webCraw.html')

@app.route('/craw', methods=['POST'])
def crawCont():
    # 1. web-crawling - melon top 100 chart.
    melon_crawler = MelonCrawler()
    crawl_data = melon_crawler.crawl('https://www.melon.com/chart/index.htm')
    crawl_data = str(crawl_data)

    # 2. insert data into database.
    _db = databaseSession(crawl_data, date.datetime.now(), 'Julia', insert_sql)
    _db.connection()

    return crawl_data


if __name__ == '__main__':
    app.run(debug=True)