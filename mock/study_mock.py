import unittest
from unittest import mock

import requests


class testmoudle(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:5555/login"
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
        self.data = {
            "username": "admin",
            "password": "admin",
            "roleID": "22"
        }

    def test_C(self):
        res = requests.post(url=self.url, json=self.data, headers=self.header)
        res = res.json()
        print(res)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
