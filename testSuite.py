import unittest
from selenium import webdriver
import page
import inspect
import re
import testpages

def suite():

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testpages.PhynSearch.test_login_phynbeta()))
    #test_suite.addTest(unittest.makeSuite(TestCases.DataObjectsPage_TestCase.DataObjectsPage_TestCase))
# etc...