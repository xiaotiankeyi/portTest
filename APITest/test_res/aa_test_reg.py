import requests
import unittest
import json

class TestReg(unittest.TestCase):
    headers = {
        'Connection': 'application/json',
        'User-Agent': 'PostmanRuntime/7.26.10',
    }

    url = "http://127.0.0.1:7777/reg/"

    data = {
        "username":"xiaotian2",
        "password":123456
    }
    data = json.dumps(data)

    def test_case(self):
        dome = requests.post(
            url=self.url,
            headers = self.headers,
            data = self.data,
        )
        response = dome.text
        print(response)

if __name__ == "__main__":
    # obj = TestReg
    # obj.test_case(a)
    pass