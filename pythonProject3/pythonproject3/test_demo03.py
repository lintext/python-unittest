import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.service import Service


class Testdemo3(unittest.TestCase):
    def setUp(self) :
        self.demo = webdriver.Chrome()
        self.demo.get("http://127.0.0.1/mgr/sign.html")
        self.demo.implicitly_wait(3)
        self.demo.maximize_window()

    def tearDown(self):
        self.demo.quit()

    def test_denglu01(self):
        self.demo.find_element(By.ID, 'username').send_keys("byhy")
        self.demo.find_element(By.ID, 'password').send_keys("88888888")
        self.demo.find_element(By.TAG_NAME, 'button').click()

    def test_denglu02(self):
        self.demo.find_element(By.ID, 'username').send_keys("byhy")
        self.demo.find_element(By.ID, 'password').send_keys("88888888")
        self.demo.find_element(By.TAG_NAME, 'button').click()
        self.demo.find_element(By.LINK_TEXT,'药品').click()
        link= self.demo.find_element(By.XPATH,'//*[@id="root"]/footer/a')

        self.demo.execute_script("arguments[0].removeAttribute('target')",link)

        # 打印 target 属性的值
        print(f"target 属性的值为: {link}")

        # 如果需要，可以对 target 属性进行操作，例如删除
        if link:
           self.demo.execute_script("arguments[0].removeAttribute('target');", link)
        print("target 属性已删除")

        link.click()
        self.demo.get_screenshot_as_file("D:\视频\\demo222.png")

if __name__ == '__main__':
    unittest.main()