import requests
import re
from requests.cookies import RequestsCookieJar
def test():
    url = 'http://192.168.0.121/bbs/upload/forum.php'

    res = requests.get(url)
    s = re.findall('name="formhash" value="(.*)"', res.text)

    return (res.cookies, s)

def login():
    s = test()
    url = 'http://192.168.0.121/bbs/upload/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LQF1E&inajax=1'

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    data = {
        'formhash': s[1][0],
        'loginfield': 'username',
        'username': 'jack',
        'password': '123456',
        'questionid': 0,
        'answer': ''
    }

    res = requests.post(url, data, headers, cookies=s[0])
    return res

def cnblogs():
    """通过cookies跳过登录验证"""
    url = 'https://account.cnblogs.com/signin?returnUrl=https:%2F%2Fwww.cnblogs.com%2F'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    s = requests.session()
    r = s.get(url, headers=header)

    c = RequestsCookieJar()
    c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8L-rpLgFVEJMgssCVvNUAjvl6g97AtVxWdY0r6GWTszKAnZdDoV-OYeqazuwiOg0_JqcfAIGRb1ie"
                                        "DRjzQCf0e9u8r5qW_yhpttyzMKlJj3Qn3tCuh0j55sfPANvBwYfAtxL8_HEAs1h-FAHXD-B_3bdfI4ysaAgQtecJyoakssP8ppwM80F"
                                        "JwORaYJl5KgD5qXQkP6NqDMzDyT4zcQJMQSBD9hZwK-IiVvHe2mvIhnHk4ZNk_Eitytl7Ihv9UXl14-vyo7yGEo22qlIa3Z9A5"
                                        "zvaTpsda0ZNduwcOpfPQQ9aCcOE4uDEvU3wB2u5_u-xWI6J7dm5Ur55KR-s5In46aCt3Pjop2NfSXypn1Y0x5SQeYDHwzo5roM9qGnUlu_FMo"
                                        "QjZbrAehKjpDWM25vro8WKCrcZnqkkKfsnbN1W6aiwmAsSOigGD7ZexG3WY107g1fppEylW9LIQ0d71YViT3fk0zdF2cqHu41l3Iof2I0BbskW9ES"
                                        "-SnvHpA8jaQQJIyZW_F1xlpunvAAcc6FN1iuaxnvXB556dCSIhYP2sfdo6UrFSMMoVLoFuOvOw4fJQ")
    c.set(".CNBlogsCookie", "87FB9B609C0F14DFFE6705DD38C9AD6586B37AF63D0FF8F0DFD069863AD9644606C51336961878C0C0FE124C5D4C03211B053"
                            "AF276233AAE4E22FEC98A2069DD6465705331D14EA8EF6C2482C87D9F734997048F")

    s.cookies.update(c)
    print('完整cookies',s.cookies)

    url2 = "https://www.cnblogs.com/97xiaolai/"
    res = s.get(url2)
    return res.text

if __name__ == "__main__":
    # a = test()
    # print(a[0])
    # c = login()
    # print(c.cookies)
    # print(c.text)
    g = cnblogs()
    print(g)