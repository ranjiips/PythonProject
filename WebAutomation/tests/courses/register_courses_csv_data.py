from PythonProject.WebAutomation.pages.courses.register_courses_page import RegisterCoursesPage
from PythonProject.WebAutomation.pages.home.navigation_page import NavigationPage
from PythonProject.WebAutomation.utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from PythonProject.WebAutomation.utilities.read_data import getCSVData
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    # @pytest.mark.run(order=1)
    # @data(*getCSVData("/PythonProject/WebAutomation/testdata.csv"))
    # @unpack
    # def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
    #     self.courses.enterCourseName(courseName)
    #     self.courses.selectCourseToEnroll(courseName)
    #     self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
    #     result = self.courses.verifyEnrollFailed()
    #     self.ts.markFinal("test_invalidEnrollment", result,
    #                       "Enrollment Failed Verification")