import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from PythonProject.WebAutomation.base.seleniumDriver import SeleniumDriver

class LoginPage(SeleniumDriver):
    # log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _loginLink = "//div/a[contains(@href,'login')]"
    _emailLocator = "email"
    _passwordLocator = "password"
    _loginBtnLocator = "//button[text()='LOG IN']"
    _homePageIcon = "//div[contains(@class,'AccountLayout')]/h1"
    _invalidCredentialsLocator = "//div[@class='toast-wrapper']/div[@data-transition='entered']"

    def clickLoginLink(self):
        self.clickElement(self._loginLink, locatorType="link")

    def enterUserName(self, username):
        self.enterText(username, locator=self._emailLocator, locatorType="id")

    def enterPassword(self, password):
        self.enterText(password, self._passwordLocator, locatorType="id")

    def clickLoginButton(self):
        self.clickElement(self._loginBtnLocator, locatorType="xpath")

    def verifyLoginSuccessful(self):
        time.sleep(5)
        return self.isElementPresent(self._homePageIcon,locatorType="xpath")

    def verifyInvalidCredentials(self):
        time.sleep(2)
        return self.isElementPresent(self._invalidCredentialsLocator, locatorType="xpath")

    def login(self, username="", password=""):
        # self.clickLoginLink()
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()
