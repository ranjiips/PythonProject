import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from PythonProject.WebAutomation.base.basepage import BasePage
import PythonProject.WebAutomation.utilities.custom_logger as cl
import logging
from PythonProject.WebAutomation.pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #locators
    _loginLink = "//a[text()='Log in']"
    _usernameLocator = "//input[@id='loginusername']"
    _passwordLocator = "//input[@id='loginpassword']"
    _loginBtnLocator = "//button[text()='Log in']"
    _homePageIcon = "//a[text()='Home ']"
    _invalidCredentialsLocator = "//div[@class='toast-wrapper']/div[@data-transition='entered']"

    def clickLoginLink(self):
        self.elementClick(self._loginLink, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._emailLocator)

    def enterPassword(self, password):
        self.sendKeys(password, self._passwordLocator)

    def clickLoginButton(self):
        self.elementClick(self._loginBtnLocator, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement("//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._emailLocator)
        emailField.clear()
        passwordField = self.getElement(locator=self._passwordLocator)
        passwordField.clear()
