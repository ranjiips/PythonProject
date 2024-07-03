import unittest

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("#" * 30)
        print("Run once before all tests")
        print("#" * 30)
    def setUp(self):
        print("\nSet method running")

    def test_methodD(self):
        print("Running test method D")
        a = True
        self.assertTrue(a,"a is not True")

    def test_methodE(self):
        print("Running test method E")
        b=15
        self.assertGreater(b,6, "b is lesser than 4")

    def test_methodC(self):
        print("Running test method C")

    def tearDown(self):
        print("Tear down method running")

    @classmethod
    def tearDownClass(cls):
        print("#"*30)
        print("Run once after all tests")
        print("#" * 30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
