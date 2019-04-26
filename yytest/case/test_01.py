#coding=utf-8
import unittest
from common.retoken import get_token
class test_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token=get_token()
        print '获取当前token值：%s'%cls.token
    def test_01(self):
        body1={
            'a':11111,
            'b':22222,
            'token':self.token
        }
        print '用例1body：%s'%body1

if __name__=="__main__":
    unittest.main()