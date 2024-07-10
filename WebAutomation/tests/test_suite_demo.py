import unittest
from PythonProject.WebAutomation.tests.home.login_test import LoginTests
from PythonProject.WebAutomation.tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

#py.test tests/test_suite_demo.py  --browser chrome