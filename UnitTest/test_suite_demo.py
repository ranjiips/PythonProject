import unittest
from pythonProject.PythonUnitTest.unit_test_demo1 import TestCaseDemo1
from pythonProject.PythonUnitTest.unit_test_demo2 import TestCaseDemo2

#get all test cases from the Test method classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

#create test suite combining the test cases
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)