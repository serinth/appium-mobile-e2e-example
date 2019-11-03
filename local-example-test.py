import unittest
from appium import webdriver


class TestLocalField(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '10',
            'automationName': 'uiautomator2',
            'deviceName': 'Android Emulator',
            'app': './ApiDemos-debug.apk',
            # 'appPackage': 'io.appium.android.apis',
            # 'appActivity': 'view.TextFields'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test(self):
        btn = self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="App"]')
        btn.click()
        
        

if __name__ == '__main__':
    unittest.main()