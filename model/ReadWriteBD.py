import pymysql

from config import host, user, password, db_name


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
            print("successfully connected...")
            print("#" * 20)
            data = []
            try:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `toys_in_shop`"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        data.append([row['id'], row['title_toy'], row['amount'], row['frequency']])


                    print("#" * 20)
                    return data

            finally:
                connection.close()

        except Exception as ex:
            print("Connection refused...")
            print(ex)

