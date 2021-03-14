import pymysql
from readconfig import *


def mysql(sql, way):

    conn = pymysql.connect(host=d_host, port=int(d_port), user=d_user, passwd=d_password, db=d_db)

    obj = conn.cursor(cursor=pymysql.cursors.DictCursor)

    obj.execute(sql)     #只显示条数
    if way == 'select':
        data = obj.fetchone()       #显示单条数据
        return data
    elif way == 'update':
        conn.commit()
    elif way == 'alter':
        conn.commit()
    elif way == 'stop':
        conn.commit()

    # test_data = obj.fetchmany(2)      #显示多条数据


if __name__ =="__main__":
    sql = "SELECT * from ds_settle_user_address WHERE user_id=4739;"
    a = mysql(sql, way='select')
    print(a, type(a))