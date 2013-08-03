'''
Created on Jul 20, 2013

@author: justin
'''
import unittest
import math


class Test(unittest.TestCase):


    def setUp(self):
        print 'Running machine learning tests'
        math.ceil(20)
        pass


    def tearDown(self):
        pass


    def testName(self):
        #self.assertEqual(0, 1, "purposefully fails this test")
        pass
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()