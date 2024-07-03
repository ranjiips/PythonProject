import unittest

class TestCaseDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("#" * 30)
        print("Run once before all tests")
        print("#" * 30)
    def setUp(self):
        print("\nSet method running")

    def test_methodA(self):
        print("Running test method A")
        a = True
        self.assertTrue(a,"a is not True")

    def test_methodAB(self):
        print("Running test method B")
        b=15
        self.assertGreater(b,6, "b is lesser than 4")

    def tearDown(self):
        print("Tear down method running")

    @classmethod
    def tearDownClass(cls):
        print("#"*30)
        print("Run once after all tests")
        print("#" * 30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
