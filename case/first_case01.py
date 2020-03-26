from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
class TestMethod(unittest.TestCase):

    #每次方法之前执行
    def setUp(self):
        print('每次方法之前执行')

    #每次方法之后执行
    def tearDown(self):
        print('每次方法之后执行')

    def test_01(self):
        print('测试1')

    def test_02(self):
        print('测试2')

if __name__ == '__main__':
    unittest.main()
