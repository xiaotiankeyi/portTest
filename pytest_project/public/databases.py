import pymysql
from APITest.data.data_yaml import rand_yaml_data


def mysql(sql, way):
    """
    数据库操作
    :param sql: sql语句
    :param way: 调用方法
    :return:
    """
    conn = pymysql.connect(
        host=rand_yaml_data(key='mysql', keyTwo='host'),
        port=rand_yaml_data(key='mysql', keyTwo='port'),
        user=rand_yaml_data(key='mysql', keyTwo='user'),
        passwd=rand_yaml_data(key='mysql', keyTwo='passwd'),
        db=rand_yaml_data(key='mysql', keyTwo='db')
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
