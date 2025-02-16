import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver


class testdemo1(unittest.TestCase):
    def setUp(self) -> None:
        self.de = webdriver.Chrome()
        self.de.implicitly_wait(3)
        self.de.maximize_window()

    def tearDown(self) -> None:
        self.de.quit()

    def test_denglu01(self):
        self.de.get('http://127.0.0.1/mgr/sign.html')
        self.de.find_element(By.ID, 'username').send_keys('byhy')
        self.de.find_element(By.ID, 'password').send_keys('88888888')
        self.de.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button').click()

    def test_denglu02(self):
        self.de.get('http://127.0.0.1/mgr/sign.html')
        self.de.find_element(By.ID, 'username').send_keys('byhy')
        self.de.find_element(By.ID, 'password').send_keys('88888888')
        self.de.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button').click()
        # self.de.switch_to.alert.dismiss()
