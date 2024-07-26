import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
from PythonProject.WebAutomation.pages.home.loginPage import LoginPage
from PythonProject.WebAutomation.utilities.teststatus import TestStatus
import PythonProject.WebAutomation.utilities.custom_logger as cl

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_t1invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_t2validLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1validLogin started")
        self.log.info("*#" * 20)
        self.lp.login("ranji_ips1", "July@2024")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.markFinal("test_t2validLogin", result2, "Login Verification")


# loginobj = LoginTests()
# loginobj.test_validLogin()
# loginobj.test_inValidLogin()