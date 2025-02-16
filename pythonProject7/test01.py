import time

from selenium.webdriver.common.by import By
import ddt
from selenium import webdriver
import unittest
from csvv import getcsv


@ddt.ddt
class testdemo(unittest.TestCase):
    def setUp(self) -> None:
        self.de = webdriver.Edge()
        self.de.implicitly_wait(4)
        self.de.maximize_window()

    def tearDown(self) -> None:
        self.de.quit()

    getscsv = getcsv()

    @ddt.data(*getscsv)
    def testdemo7(self, str):
        try:
            self.de.get('http://127.0.0.1/mgr/sign.html')
            self.de.find_element(By.ID, 'username').send_keys('byhy')
            self.de.find_element(By.ID, 'password').send_keys('88888888')
            self.de.find_element(By.TAG_NAME, 'button').click()
            time.sleep(2)
            self.de.find_element(By.CLASS_NAME, 'btn-md').click()
            self.de.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys(
                'str[0]')
            self.de.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys(
                'str[1]')
            self.de.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys(
                'str[2]')
            self.de.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()
            time.sleep(5)
            qu = self.de.find_element.send_keys('str[1]').text
            print(qu)
            self.assertEqual(qu, str[1])
        except:
            print('测试失败')


if __name__ == '__main__':
    unittest.main()
