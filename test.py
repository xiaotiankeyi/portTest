a = "Httpapidome/.env"
b = "C:\\Users\jack\PycharmProjects\portTest\Httpapidome\.env"

f = {
    "errcode": 0,
    "errmsg": "ok",
    "taglist": [
        {
            "tagid": 12,
            "tagname": "UI部门"
        }
    ]
}
print(f["taglist"][0]['tagname'])

g = {
    "errcode": 0,
    "errmsg": "ok",
    "department": [
        {
            "id": 1,
            "name": "\u594b\u8fdb\u6587\u5316\u4f20\u7164\u6709\u9650\u516c\u53f8",
            "parentid": 0,
            "order": 100000000
        }]
}
print(g["department"][0]['id'])
