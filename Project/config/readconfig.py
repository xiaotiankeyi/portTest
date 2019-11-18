import configparser
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(base_dir, 'configData.ini')

obj = configparser.ConfigParser()
obj.read(config_file)

#读取邮箱配置信息
e_host = obj['email']['host']
e_user = obj['email']['user']
e_password = obj['email']['password']
e_accept_user = obj['email']['send_user']


#读取数据库配置信息
d_host = obj['mysql']['host']
d_port = obj['mysql']['port']
d_user = obj['mysql']['user']
d_password = obj['mysql']['password']
d_db = obj['mysql']['db']
