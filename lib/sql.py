import pymysql
import pytest


def sql_def(sql_query):
    conn = None
    try:
        conn = pymysql.connect(
            host='12.0.11.90',
            user='songjiao_qa_wolkflow_read',
            password='iABqNaam4p4pCwnHXVCwnHX',
            port=3306,
            charset='utf8',
        )
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            data = cursor.fetchall()
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
    qq = sql_def(sql_query = f"SELECT app_project_name,bundle_id,name FROM `joymeet`.`app_package` WHERE `bundle_id`  LIKE  '%com.blaze.chatjoin%';")
    print(qq)



