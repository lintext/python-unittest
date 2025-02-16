import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
demo = webdriver.Edge()
demo.get("http://127.0.0.1/mgr/sign.html")
demo.find_element(By.ID,'username').send_keys('byhy')
demo.find_element(By.ID,'password').send_keys('88888888')
demo.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[3]/div/button').click()
time.sleep(10)

# demo.find_element(By.LINK_TEXT,"客户")
# driver.execute_script("arguments[0].removeAttribute('target');",demo)
#
# updated_target_attribute = demo.get_attribute("target")
# print(f"删除 target 属性后，当前 target 属性值为: {updated_target_attribute}")
demo.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[1]').click()

demo.get_screenshot_as_file("D:\视频\\test_target04.png")
demo.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[2]/div/label[2]').click()
time.sleep(5)