import unittest
from ReadExcel import HandleExcel
from loginFunc import login

class startup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = HandleExcel()
        cls.cookies = login()

    @classmethod
    def tearDownClass(cls):
        pass