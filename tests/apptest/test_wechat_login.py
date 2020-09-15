

def test_login(appium):
    appium.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()

    appium.find_element_by_id('com.lqr.wechat:id/etPhone').send_keys('18010181267')
    appium.find_element_by_id('com.lqr.wechat:id/etPwd').send_keys('123456')

    appium.find_element_by_id('com.lqr.wechat:id/btnLogin').click()
