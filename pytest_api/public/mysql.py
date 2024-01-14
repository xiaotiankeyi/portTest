import os
import sys

sys.path.append(os.path.join(os.getcwd(), "pytest_api"))

import pymysql
from config.read_operation import rand_yaml_data


def mysql(sql, way):
    """
    数据库操作
    :param sql: sql语句
    :param way: 调用方法
    :return:
    """
    path_dir = os.path.join(os.getcwd(), "pytest_api", "config", "config_data.yaml")
    config_data = rand_yaml_data(file=path_dir, key=None)
    # print(config_data)
    conn = pymysql.connect(
        host=config_data["host"],
        port=config_data["post"],
        user=config_data["user"],
        passwd=config_data["passwd"],
        db=config_data["db"],
    )

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
    # sql = "SELECT * from ds_settle_user_address WHERE user_id=4739;"
    # a = mysql(sql, way='select')
    # print(a, type(a))
    pass
