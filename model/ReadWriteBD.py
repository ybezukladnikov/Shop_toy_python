import pymysql

from config import host, user, password, db_name
from model.Exception import ExceptionReqDB, ExceptionConnectToDB


class ReadWriteBD:
    def read_bd(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            data = []
            try:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `toys_in_shop`"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        data.append([row['id'], row['title_toy'], row['amount'], row['frequency']])
            except Exception:
                raise ExceptionReqDB()

            finally:
                connection.close()
            return data
        except ExceptionReqDB:
            print(ExceptionReqDB.description)
            exit()
        except Exception:
            raise ExceptionConnectToDB("Error connecting to the database")




