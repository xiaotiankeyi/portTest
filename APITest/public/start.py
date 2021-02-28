import unittest

class startup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("测试环境准备 test start")

    @classmethod
    def tearDownClass(cls):
        print("测试结束 test stop")