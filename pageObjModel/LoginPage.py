from selenium import webdriver
import selenium
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    textbox_username_xpath = "//*[@id='Email']"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def loginbutton(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def logoutbutton(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

