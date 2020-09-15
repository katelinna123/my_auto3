from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# 必要配置
caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': '127.0.0.1:62001',
    # 'deviceName': '127.0.0.1:21503',
    'appPackage': 'com.lqr.wechat',
    'appActivity': 'ui.activity.SplashActivity',
    'automationName': 'uiautomator2'

}

# 启动app
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.find_element_by_id("com.lqr.wechat:id/btnLogin").click()
sleep(1)
driver.find_element_by_id("com.lqr.wechat:id/etPhone").send_keys("18010181267")
driver.find_element_by_id("com.lqr.wechat:id/etPwd").send_keys("1234567")
driver.find_element_by_id("com.lqr.wechat:id/btnLogin").click()
# toast = driver.find_element_by_xpath("//*[contains(@text, '登录失败')]")  # "//*[@text='登录失败1000']"
# print(toast.get_attribute("text"))

WebDriverWait(10, 0.5).until(lambda x: driver.find_element_by_xpath("//*[contains(@text, '登录失败')]"))


sleep(3)
driver.quit()