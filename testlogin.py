# -*-coding:utf-8-*-
from selenium import webdriver
import unittest
from time import sleep
class testlogin(unittest.TestCase):
    def setUp(self):
        print 'this is first testcase!'
    def testbaidu(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com/")
        self.driver.find_element_by_id("su").send_keys("python")
        self.driver.find_element_by_id("kw").click()
        #self.title2 = u'百度一下，你就知道'
        #self.assertEquals = (self.title1,self.title2,msg=='搜索失败！')
        sleep(3)
        self.driver.quit()
    def tearDown(self):
        print "this test ending!"


if __name__=='__main__':
    unittest.main()