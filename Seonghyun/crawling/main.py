from crawling.util.dbsession import *
import datetime as date
from crawling.service.melon_crawler import *
from crawling.service.query import *

# 1. web-crawling - melon top 100 chart.
melon_crawler = MelonCrawler()
crawl_data = melon_crawler.crawl('https://www.melon.com/chart/index.htm')

# 2. insert data into database.
_db = databaseSession(str(crawl_data), date.datetime.now(), 'Julia', insert_sql)
_db.connection()
