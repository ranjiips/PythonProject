import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from opencart.base.baseMethod import BaseMethod

class HomePage(BaseMethod):

    def __init__(self, driver):
        super().__init__(driver)

    # Locator
    _myAccountLocator = "//span[contains(@class, 'd-md-inline') and text()='My Account']"
    _registerLocator = "//a[@class='dropdown-item' and text()='Register']"
    _loginLocator = "//a[@class='dropdown-item' and text()='Login']"
    _logoutLocator = "//a[@class='dropdown-item' and text()='Logout']"


    def verifyHomePage(self):
        current_URL= self.getCurrentURL()
        assert "home" in current_URL

    def selectOption(self, option):
        if option.lower()=="register":
            self.clickElement("xpath", self._myAccountLocator)
            self.clickElement("xpath", self._registerLocator)
        elif option.lower()=="login":
            self.clickElement("xpath", self._myAccountLocator)
            self.clickElement("xpath", self._loginLocator)
        elif option.lower() == "logout":
            self.clickElement("xpath", self._myAccountLocator)
            self.clickElement("xpath",self._logoutLocator)


