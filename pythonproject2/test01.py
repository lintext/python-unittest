from logging import root

from selenium import webdriver
import ddt
import unittest
from selenium.webdriver.common.by import By
from csvv import readzsmc
import time


@ddt.ddt
class Denglu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    stream_info = readzsmc()

    @ddt.data(*stream_info)
    def test_denglu(self, list):
        driver = self.driver
        driver.get("http://127.0.0.1/mgr/sign.html")
        driver.find_element(By.ID, 'username').send_keys("byhy")
        driver.find_element(By.ID, 'password').send_keys("88888888")
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button').click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/button').click()
        time.sleep(5)
        # driver.find_element(By.PARTIAL_LINK_TEXT,"仓库信息").click()
        # time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys(list[0])
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys(list[1])
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys(list[2])

        driver.find_element(By.XPATH, '// *[ @ id = "root"] / div / section[2] / div[1] / div[2] / button[1]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file(r'D:\视频\\testdata.png')


if __name__ == '__main__':
    unittest.main()
