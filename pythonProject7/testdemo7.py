import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

we = webdriver.Chrome()
we.get('http://127.0.0.1/mgr/sign.html')
we.find_element(By.ID, 'username').send_keys('byhy')
we.find_element(By.ID, 'password').send_keys('88888888')

login_button = we.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/div/button')
qw = ActionChains(we)  # 引入ActioChains类时不要直接调用，定义变量qw接受ActioChains传入的值
qw.click(login_button).perform()  # 通过变量点击传入的值点击按钮登录perform函数必不可少
time.sleep(3)
we.find_element(By.TAG_NAME, 'input').click()
eq = we.find_element(By.TAG_NAME, 'input').send_keys('qwqw')
qw = ActionChains(we)
time.sleep(5)
qw.double_click(eq).perform()
we.get_screenshot_as_file('D:\视频\\wgahfbc.png')
time.sleep(5)
