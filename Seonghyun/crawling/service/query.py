insert_sql = """
                INSERT INTO CRAW_BAS (CRAW_DATA, SYSTEM_DATE, DESCRIPTION) 
                VALUES (%s, %s, %s)
                """