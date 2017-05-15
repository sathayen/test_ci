"""run

This module is a simple script to run some dummy python unit tests. 
It is used just for testing/debugging different things in a Jenkins/Travis CI
pipeline.

The code is compatible with Python 3.5.x.

Author: Ninad Sathaye
"""

# Script to be run by the Jenkins/Travis CI. 
# Used to debug/test CI pipeline


import os
import unittest

class MyTest(unittest.TestCase):    
    def setUp(self):        
        self.val = 10
        print("\nIn setUp, Running tests for run.py")
        print ("..with self.val=",self.val)
        
        
    def test_this_should_pass(self):
        print("Running test_this_should_pass...")
        self.assertTrue(self.val == 10)
    
    @unittest.skip("Skipping a known failure .. test_this_should_fail")
    def test_this_should_fail(self):
        print("Running test_this_should_fail...")
        self.assertFalse(self.val == 10)

if __name__ == '__main__':   
   unittest.main()
   

