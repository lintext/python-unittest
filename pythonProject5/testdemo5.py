from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.support import select

we = webdriver.Edge()
we.get('http://127.0.0.1/mgr/sign.html')
we.implicitly_wait(3)
we.maximize_window()
we.find_element(By.ID, 'username').send_keys('byhy')
we.find_element(By.ID, 'password').send_keys('88888888')
we.find_element(By.TAG_NAME, 'button').click()
time.sleep(5)
we.find_element(By.LINK_TEXT,'其它菜单').click()
# we.find_element(By.CSS_SELECTOR,'span').click()
we.get_screenshot_as_file(r'D:\视频\\test1231.png')

