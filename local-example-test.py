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
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_log_text_box_adds_expected_text(self):
        expected = 'This is a test\n'

        btn_text = self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Text"]')
        btn_text.click()

        btn_logTextBox = self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="LogTextBox"]')
        btn_logTextBox.click()

        btn_add = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Add"]')
        btn_add.click()
        
        textView = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TextView')
        
        actual = textView.get_attribute('text')

        self.assertEqual(expected, actual, 'Text/LogTextBox did not have the correct value after clicking "Add"')
        

if __name__ == '__main__':
    unittest.main()