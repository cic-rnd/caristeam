import pymysql

# MariaDB Connection Func.
class databaseSession:
    # init Func.
    def __init__(self, *args):
        self._title = args[0]
        self._date = args[1]
        self._descp = args[2]
        self._sql = args[3]

    # MariaDB connection info.
    def connection(self):
        # --------------- DB Connection --------------- #
        conn = pymysql.connect(
            host='192.168.19.234',
            user='root',
            password='cic_study!@',
            db='cic_study',
            charset='utf8',
            port=40022)
        # --------------- DB Connection --------------- #

        # DB transaction.
        try:
            cur = conn.cursor()
            cur.execute(self._sql, (self._title, self._date, self._descp))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print('[DB ERROR] ::'.format(str(e)))
        finally:
            conn.close()