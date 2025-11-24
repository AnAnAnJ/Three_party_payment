
from contextlib import contextmanager
import pymysql as pymysql
import json
import requests

class Test_Query_admin_data():

    def read_mysql(db,sql):
        try:
            connect = pymysql.connect()  #host='11', port="11",user='1',passwd='', charset='utf8', db=db
        except Exception as e:
            print('连接数据库错误，错误是%s' % e)
        else:
            cur = connect.cursor()
            if 'select'.upper() in sql:
                try:
                    cur.execute(sql)
                except Exception as e:
                    print('执行sql语句失败，错误是%s' % e)
                else:
                    res = cur.fetchall()
                    connect.close()
                    cur.close()
                    print(sql)
                    print(res)
                    return res
            else:
                try:
                    cur.execute(sql)
                except Exception as e:
                    print('执行sql语句失败，错误是%s' % e)
                else:
                    # 提交数据至数据库
                    connect.commit()
                    connect.close()
                    cur.close()
                print(sql)
                print('数据库操作成功', end='\n')



