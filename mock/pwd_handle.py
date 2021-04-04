import hashlib
import base64

def encryption(pwd):
    m = hashlib.md5()       #生成md5对象
    m.update('一行白鹭上青天'.encode('utf-8'))     #对密码进行加盐
    m.update(pwd.encode('utf-8'))
    return m.hexdigest()

def Ebase64(string):
    # return str(base64.b64encode(string.encode('utf-8')), 'utf8')  #加密返回字符串
    return base64.b32decode(string).decode('utf8')      #解密

if __name__ == "__main__":
    password = '123456'
    s = encryption(password)
    print(s)

    c = 'MTIzNDU2'
    a = Ebase64(c)
    print(a)
    
