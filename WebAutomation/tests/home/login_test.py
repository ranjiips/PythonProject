from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
from PythonProject.WebAutomation.pages.home.loginPage import LoginPage
from PythonProject.WebAutomation.utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        # baseURL = "https://ecommercepractice.letskodeit.com/"
        baseURL = "https://ecommercepractice.letskodeit.com/login/"
        # self.driver.get(baseURL)
        self.lp.login("test@gmail.com","July@2024")
        self.ts.mark(True, "Title Verified")
        result = self.lp.verifyLoginSuccessful()
        # assert result==True
        self.ts.markFinal("test_validLogin", result, "Login was successful")

    @pytest.mark.run(order=2)
    def test_inValidLogin(self):
        baseURL = "https://sso.teachable.com/secure/42299/identity/login/"
        # baseURL = "https://ecommercepractice.letskodeit.com/login/"
        # self.driver.get(baseURL)

        self.lp.login()
        result = self.lp.verifyInvalidCredentials()
        assert result==True


# loginobj = LoginTests()
# loginobj.test_validLogin()
# loginobj.test_inValidLogin()