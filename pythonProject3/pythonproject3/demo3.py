from selenium.webdriver.common.by import By
import time
from selenium import webdriver
we = webdriver.Edge()
we.get("http://127.0.0.1/mgr/sign.html")
we.find_element(By.ID,'username').send_keys("byhy")
we.find_element(By.ID,'password').send_keys("88888888")
we.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[3]/div/button').click()
we.find_element(By.PARTIAL_LINK_TEXT,'客户').click()
time.sleep(2)
# we.find_elements(By.TAG_NAME,'button')[0].click()
we.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').click()
time.sleep(4)
we.switch_to.alert.accept()

time.sleep(2)
