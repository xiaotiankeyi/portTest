import json
import random

import flask
import pymysql

from mock.pwd_handle import encryption

server = flask.Flask(__name__)  # 把当前这个python文件，当做一个服务，定义Server(启动服务)


def my_db(sql):
    """
    数据库操作
    :param sql:
    :return:
    """
    coon = pymysql.connect(
        host='192.168.0.121', user='mysql', passwd='123456',
        port=3306, db='test', charset='utf8')
    cur = coon.cursor(cursor=pymysql.cursors.DictCursor)  # 建立游标,返回结果为字典

    cur.execute(sql)  # 执行sql
    if sql.strip()[:6].upper() == 'SELECT':
        res = cur.fetchall()  # 输出全部数据
    else:
        coon.commit()  # 提交到数据库
        res = 'ok'
    cur.close()  # 关闭游标对象
    coon.close()  # 关闭数据库连接
    return res


@server.route('/index/', methods=['get'])  # 接口装饰器，get请求
def index():
    res = {'msg': '这是我开发的第一个接口', 'msg_code': 0}  # 定义一个字典
    return json.dumps(res, ensure_ascii=False)  # 将字典转化成json串，ensure_ascii=False将unicode转成十进制


@server.route('/reg/', methods=['post'])
def reg():
    """
    注册接口
    参数:
        username
        password
    :return:
    """
    get_data = flask.request.get_data()
    # print(type(get_data), get_data)

    get_data = json.loads(get_data)
    print(type(get_data), get_data)

    username = get_data.get('username')
    pwd = get_data.get('password')
    # print(username, pwd, type(pwd))

    pwd = encryption(pwd=str(pwd))  # 密码加密

    if username and pwd:
        sql = 'select username from my_user where username="%s";' % username
        # res = my_db(sql)
        if my_db(sql):
            res = {'msg': '用户已存在', 'msg_code': 2001}
        else:
            tonke = ''.join(random.sample('0123456789dsjfhlkfnifsdfsdfsfugfwf', 20))  # 生成随机tonke

            insert_sql = 'insert into my_user (username,password,tonke) values ("%s","%s","%s");' % (
                username, pwd, tonke)
            my_db(insert_sql)
            res = {'msg': '注册成功！', 'msg_code': 0}
    else:
        res = {'msg': '必填字段未填，请查看接口文档！', 'msg_code': 1001}
        # 1001必填字段未填
    return json.dumps(res, ensure_ascii=False)


@server.route('/login/', methods=['post'])
def login():
    """
    登录接口
    参数:
        username
        password
    :return:
    """

    if flask.request.get_data() is None:
        res = {'msg': '参数请求为空', 'msg_code': 2001}
        return json.dumps(res, ensure_ascii=False)

    else:
        get_data = flask.request.get_data()

        get_data = json.loads(get_data)
        # print(type(get_data), get_data)

        username = get_data.get('username')
        pwd = get_data.get('password')
        pwd = encryption(pwd=str(pwd))  # 密码加密在验证

        sql = 'select username from my_user where username="%s";' % username  # 查询用户
        pwdSql = 'select password from my_user where username="%s";' % username  # 查询用户密码
        tonkeSql = 'select tonke from my_user where username="%s";' % username  # 查询用户tonke值

        if username == "":
            res = {'msg': '用户名不能为空', 'msg_code': 2001}
            return json.dumps(res, ensure_ascii=False)

        elif not my_db(sql):
            res = {'msg': '用户不存在,该用户未注册', 'msg_code': 2001}
            return json.dumps(res, ensure_ascii=False)

        elif my_db(pwdSql)[0]['password'] != pwd:
            res = {'msg': '用户密码错误,请重新输入', 'msg_code': 2001}
            return json.dumps(res, ensure_ascii=False)

        elif my_db(pwdSql)[0]['password'] == pwd:
            res = {'msg': '用户登录成功！！', 'tonke': my_db(tonkeSql)[0]['tonke'], 'msg_code': 200}
            return json.dumps(res, ensure_ascii=False)  # 把字典转化为json


@server.route('/select/', methods=['get'])
def select():
    """
    查询数据库数据
    参数:
        quantity
        tonke
    :return:
    """
    quantity = flask.request.values.get('quantity')
    tonke = flask.request.values.get('tonke')

    tonkeSql = 'select tonke from my_user;'  # 查询用户tonke值
    userSql = 'SELECT username FROM my_user LIMIT %d;' % int(quantity)  # 查询指定多少行数据

    # print(quantity, tonke)
    #
    # print(my_db(tonkeSql))

    if tonke in str(my_db(tonkeSql)):
        res = {'msg': '查询成功!', 'data': my_db(userSql), 'msg_code': 200}
    else:
        res = {'msg': '查询失败,未授权!', 'msg_code': 20001}

    return json.dumps(res, ensure_ascii=False)


server.run(port=7777, debug=True, host='127.0.0.1')
# 启动服务。debug=True，改了代码之后，不用重启它会自动帮你重启redis
# host=0.0.0.0表示别人访问的时候，用你的ip就可以访问了。

if __name__ == "__main__":
    # sql = "SELECT * FROM my_user;"
    # f = my_db(sql)
    # print(f)
    pass
