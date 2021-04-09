from Service.dbsession_info import *
from Service.webcrawl import *
import datetime as date

#web-crwaling
print(result)

#Insert data into Database.
_db = databaseSession(result, date.datetime.now(), 'simji', sql)
_statusCode = _db.connection()