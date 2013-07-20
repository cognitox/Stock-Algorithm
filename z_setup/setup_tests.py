'''
Created on Jul 20, 2013

@author: justin
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        print 'Running data tests'
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()