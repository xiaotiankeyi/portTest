import hashlib

def encryption(pwd):
    m = hashlib.md5()       #生成md5对象
    m.update('一行白鹭上青天'.encode('utf-8'))     #对密码进行加盐
    m.update(pwd.encode('utf-8'))
    return m.hexdigest()

if __name__ == "__main__":
    password = '123456'
    s = encryption(password)
    print(s)