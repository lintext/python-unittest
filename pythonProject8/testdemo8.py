import time

from selenium.webdriver.common.by import By
from selenium import webdriver

we = webdriver.Chrome()
we.get('http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html')
we.implicitly_wait(5)
we.maximize_window()
we.find_element(By.NAME, 'accounts').send_keys('bbbb')
we.find_element(By.NAME, 'accounts').send_keys('123123')
we.find_element(By.TAG_NAME, 'button').click()

we.find_elements(By.TAG_NAME, 'button')[0].click()
we.find_element(By.XPATH, '/html/body/div[4]/div/ul/li[2]/div/a/img').click()
time.sleep(2)
we.switch_to.window(we.window_handles[1])
time.sleep(5)
we.find_element(By.LINK_TEXT, '个人中心').click()
time.sleep(5)
we.find_element(By.XPATH, '/html/body/div[8]/div/span').click()

time.sleep(30)
