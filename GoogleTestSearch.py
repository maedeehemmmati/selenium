from selenium import webdriver

import time

import HtmlTestRunner


import unittest

class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("گمرک")
        time.sleep(5)
        self.driver.find_element_by_name("btnK").click()
    
    def test_search_2(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("ایران")
        time.sleep(5)
        self.driver.find_element_by_name("btnK").click()

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports') )
