import unittest
from appium import webdriver


class TestLocalField(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8',
            'deviceName': 'Motorola Moto G6',
            'phoneOnly': 'false',
            'tabletOnly': 'false',
            'privateDevicesOnly': 'false',
            'testobject_api_key': '<YOUR API KEY>',
            'testobject_app_id': '1' # If there's a new APK, this changes. See documentation
        }

        # EU Endpoint
        self.driver = webdriver.Remote('https://appium.testobject.com/wd/hub', desired_caps)

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

        # Set the status of the test, Demo only. Clean up for all tests
        try:
            self.assertEqual(expected, actual, 'Text/LogTextBox did not have the correct value after clicking "Add"')
            self.driver.execute_script('sauce:job-result=passed')
        except AssertionError:
            self.driver.execute_script('sauce:job-result=failed')
        

        

if __name__ == '__main__':
    unittest.main()