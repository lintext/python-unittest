import time

from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
class testdemo(unittest.TestCase):
    def setUp(self) -> None:
        self.demo=webdriver.Edge()
        self.demo.get("http://127.0.0.1/mgr/sign.html")
        self.demo.implicitly_wait(3)
        self.demo.maximize_window()
    def tearDown(self) -> None:
        self.demo.quit()

    def test_denglu01(self):
        self.demo.find_element(By.ID,'username').send_keys('byhy')
        self.demo.find_element(By.ID,'password').send_keys('88888888')
        self.demo.find_element(By.TAG_NAME,'button').click()

    def test_denglu02(self):
        self.demo.find_element(By.ID,'username').send_keys('byhy')
        self.demo.find_element(By.ID,'password').send_keys('88888888')

        self.demo.find_element(By.TAG_NAME,'button').click()
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()