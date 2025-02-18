import time
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver


class testdemo08(unittest.TestCase):
    def setUp(self) -> None:
        self.we = webdriver.Chrome()
        self.we.implicitly_wait(3)
        self.we.maximize_window()

    def tearDown(self) -> None:
        self.we.quit()

    def test_denglu01(self):
        self.we.get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')
        self.we.find_element(By.NAME, 'accounts').send_keys('bbbb')
        self.we.find_element(By.NAME, 'pwd').send_keys('123123')
        self.we.find_element(By.TAG_NAME, 'button').click()

    def test_denglu02(self):
        self.we.get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')
        self.we.find_element(By.NAME, 'accounts').send_keys('bbbb')
        self.we.find_element(By.NAME, 'pwd').send_keys('123123')
        self.we.find_element(By.TAG_NAME, 'button').click()
        self.we.find_elements(By.TAG_NAME, 'span')[0].click()
        # self.we.find_element(By.XPATH,'').click()
        # self.we.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/form/div[1]/input').send_keys('bbbb')
        # self.we.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/form/div[2]/div/input').send_keys('123123')

        # self.we.find_element(By.XPATH,'/html/body/div[8]/div/span').click()
        time.sleep(50)
        # self.we.find_element(By.PARTIAL_LINK_TEXT,'资料管理').click()
        # time.sleep(3)


if __name__ == '__main__':
    unittest.main()
