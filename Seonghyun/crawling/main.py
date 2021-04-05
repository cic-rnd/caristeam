from crawling.util.dbsession import *
import datetime as date
from crawling.service.melon_crawler import *
from crawling.service.query import *

crawl_data = MelonCrawler().crawl('https://www.melon.com/chart/index.htm')

_db = databaseSession(str(crawl_data), date.datetime.now(), 'Julia', insert_sql)
_statusCode = _db.connection()
