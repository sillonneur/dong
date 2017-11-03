# -*-coding:utf-8-*-
from selenium import webdriver
import unittest
from time import sleep
class testindex(unittest.TestCase):
    def setUp(self):
        print "this sencoend test case!"
    def testindex(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.baidu.com/")
        self.title=self.driver.title
        self.title2=u"百度一下，你就知道"
        self.assertEquals(self.title,self.title2,msg=' this is mistake: %s != %s'%(self.title,self.title2))
        sleep(3)
        self.driver.quit()
    def tearDown(self):
        print 'the secoend test case is run over!'
if __name__=="__main__":
    unittest.main()