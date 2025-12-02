import pymysql
import pytest


def sql_def(sql_query):
    conn = None
    try:
        conn = pymysql.connect(
            host='12.0.11.90',
            user='viva_prod_read',
            password='7EU9DB2HbTPjMqsRi7xxS',
            port=3306,
            charset='utf8',
        )
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            data = cursor.fetchone()
            if sql_query.strip().upper().startswith('SELECT'):
                return data
            else:
                conn.commit()
                print(data)
                return data
    except Exception as e:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()



if __name__ == '__main__':
    qq = sql_def(sql_query = "SELECT * FROM `viva`.`user` WHERE `email` = 'jillsong0221@gmail.com' LIMIT 5;")
    print(qq)

