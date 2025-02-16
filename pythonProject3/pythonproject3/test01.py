import time
import unittest
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from csvv import getcsv


@ddt.ddt
class test_demo(unittest.TestCase):
    def setUp(self):
        self.demo = webdriver.Chrome()

        self.demo.implicitly_wait(5)
        # self.demo.maximize_window()

    def tearDown(self):
        self.demo.quit()

    stream_info = getcsv()

    @ddt.data(*stream_info)
    def test_demo03(self, str):
        try:
            demo = self.demo
            demo.get('http://127.0.0.1/mgr/sign.html')
            demo.find_element(By.ID, 'username').send_keys('byhy')
            demo.find_element(By.ID, 'password').send_keys('88888888')
            demo.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button').click()
            demo.find_element(By.LINK_TEXT, '药品').click()
            demo.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/button').click()
            time.sleep(5)
            demo.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys(str[0])
            time.sleep(5)
            demo.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys(str[1])
            demo.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys(
                str[2])
            time.sleep(5)
            demo.find_element(By.CLASS_NAME, 'btn-xs').click()
            a=demo.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[1]').text
            print(a)
            time.sleep(5)
            self.assertEqual(a, str[1])
            print('测试成功')
        except:
            self.demo.get_screenshot_as_file('D:\视频\\qwddqdw.png')
            print('结果不一致')


if __name__ == '__main__':
    unittest.main()
