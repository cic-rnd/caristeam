from dbsession import *
import datetime as date
from Service.webcrawl import *
sql = """
            INSERT INTO CRAW_BAS 
                (CRAW_DATA, SYSTEM_DATE, DESCRIPTION) 
                VALUES 
                (%s, %s, %s)
            """
_db = databaseSession(result, date.datetime.now(), 'simji', sql)
_statusCode = _db.connection()

print(_statusCode)