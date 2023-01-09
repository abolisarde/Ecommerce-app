import time

from selenium import webdriver
import selenium
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObjModel.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service
from utilities.ReadProperties import Readconfig
from utilities.CustomLogger import Loggen

class Test_001_login:
    Baseurl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = 'admin@yourstore.com'
    password = 'admin'

    logger = Loggen.loggen()

    def test_homepagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.Baseurl)
        actualtitle = self.driver.title

        if actualtitle =='Your store. Login':
            assert True
            self.logger.info("1st Test case is passed")
        else:
            self.logger.info("1st Test case is failed")
            assert False



    def test_loginuser(self,setup):
        self.driver=setup
        self.driver.get(self.Baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.loginbutton()
        time.sleep(3)

        self.driver.save_screenshot(".\\ScreenShots\\"+"loginscreenshot.png")
        self.lp.logoutbutton()


        self.logger.info(" 2nd Test case is passed")


