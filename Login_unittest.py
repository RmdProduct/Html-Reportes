import HtmlTestRunner
from selenium import webdriver
import unittest
class OrangeHrm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.drivers=webdriver.Chrome(executable_path=r"C:\Users\Ram\Desktop\Drivers\chromedriver.exe")
      #  cls.drivers.maximize_window()
    def test_home(self):
        self.drivers.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual(self.drivers.title,"OrangeHRM","Is Not Equal Title")
    def test_login(self):
        self.drivers.get("https://opensource-demo.orangehrmlive.com/")
        self.drivers.find_element_by_id("txtUsername").send_keys("Admin")
        self.drivers.find_element_by_id("txtPassword").send_keys("admin")
        self.drivers.find_element_by_xpath("//*[@id='btnLogin']").click()
        self.assertEqual(self.drivers.title,"OrangeHRM","Title Is Not Equal")
    #@classmethod
    def tearDownClass(cls):
        cls.drivers.close()
if __name__ =="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\\Users\\Ram\Desktop\\Selenium\\Html-Testrunner\\Reportes"))