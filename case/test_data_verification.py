"""
 - admin数据数据查询：
   1、查询bundle_id对应的项目名称 / 包名
   2、根据包名查询 --> 商品id 对应的支付名称及平台信息
"""
import sqlite3
from contextlib import contextmanager

class Test_Query_admin_data():

    @contextmanager
    def test_get_db_connection(self):
        conn = sqlite3.connect('conurs.db')
        try:
            yield conn
        finally:
            conn.close()

    def test_query_data(slef,bundle_id):
        get_db_connection = Test_Query_admin_data().get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM table")
            results = cursor.fetchall()
            return results




