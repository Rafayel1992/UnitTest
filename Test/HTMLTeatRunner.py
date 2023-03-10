from HTMLTestRunner import HTMLTestRunner
import unittest
from Test.SignInTest import MyTest
from Test.SercheTest import SercheTest
from Test.CartTest import CartTest

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(MyTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(SercheTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(CartTest),

        ])

        outfile = open("SmokeTest.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )

        runner1.run(smoke_test)