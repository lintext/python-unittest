import time

from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver


class getdemo5(unittest.TestCase):
    def setUp(self) -> None:
        self.we = webdriver.Edge()
        self.we.implicitly_wait(3)
        self.we.maximize_window()

    def tearDown(self) -> None:
        self.we.quit()

    def test_denglu01(self):
        self.we.get('http://127.0.0.1/mgr/sign.html')
        self.we.find_element(By.ID,'username').send_keys('byhy')
        self.we.find_element(By.ID,'password').send_keys('88888888')
        self.we.find_element(By.CLASS_NAME,'btn-flat').click()
        time.sleep(4)
    def test_denglu02(self):
        self.we.get('http://127.0.0.1/mgr/sign.html')
        self.we.find_element(By.ID, 'username').send_keys('byhy')
        self.we.find_element(By.ID, 'password').send_keys('88888888')
        self.we.find_element(By.CLASS_NAME, 'btn-flat').click()
        self.we.find_element(By.LINK_TEXT,'客户').click()
        time.sleep(2)
        # self.we.find_element(By.TAG_NAME,'button').click()
        # time.sleep(3)
        # self.we.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').click()
        # time.sleep(5)
        # # self.we.switch_to.alert.accept()
        # time.sleep(2)
        # a=self.we.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').text
        # self.assertEqual(a)
        # print('yeas')