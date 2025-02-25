import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from opencart.base.baseMethod import BaseMethod
from opencart.utils.readCSV import ReadCSV

class RegisterPage(BaseMethod):
    def __init__(self,driver):
        super().__init__(driver)
        self.dfObj = ReadCSV()


    #Locator
    _registerAccountLocator = "//h1"
    _firstNameLocator = "//input[@id='input-firstname']"
    _lastNameLocator = "//input[@id='input-lastname']"
    _eMailLocator = "//input[@id='input-email']"
    _passwordLocator = "//input[@id='input-password']"
    _subscribeLocator = "//input[@id='input-newsletter']"
    _privacyPolicyLocator = "//input[@name='agree']"
    _continueLocator = "//*[contains(@class,'btn-primary') and text()='Continue']"
    _accountCreatedHeaderLocator = "//h1"  # LinkText


    def validateRegisterPage(self):
        registerHeader = self.getElementText("xpath",self._registerAccountLocator)
        assert "Register Account" == registerHeader

    def enterPersonalDetails(self, fName, lName, email, pwd):
        self.enterText("xpath",self._firstNameLocator,fName)
        self.enterText("xpath",self._lastNameLocator,lName)
        self.enterText("xpath",self._eMailLocator,email)
        self.enterText("xpath",self._passwordLocator,pwd)
        self.scroll_to_element("xpath", self._continueLocator)
        self.wait_until_element_visible("xpath", self._continueLocator)
        self.clickElement("xpath",self._subscribeLocator)
        self.clickElement("xpath",self._privacyPolicyLocator)

    def verifyPageCreated(self):
        self.hard_wait()
        verifyPageCreatedHeader = self.getElementText("xpath",self._accountCreatedHeaderLocator)
        assert "Your Account Has Been Created!" == verifyPageCreatedHeader

    def selectButton(self, btnName):
        if btnName.lower()=="continue":
            self.clickElement("xpath", self._continueLocator)

    def registerUserDetails(self):
        self.data = self.dfObj.read_data_from_csv()
        for key, value in self.data.items():
            fName = value['FirstName']
            lName = value['LastName']
            email = value['Email']
            pwd = value['Password']
            self.enterPersonalDetails(fName, lName, email, pwd)

