import unittest
from selenium import webdriver
import page
import inspect
import os
#from selenium import SAFARI
#from selenium import DesiredCapabilities
#import HTMLTestRunner

class PhynSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        #self.driver = webdriver.Firefox()
        #self.driver = webdriver.Safari()
        app = os.path.join(os.path.dirname(__file__),
                           'TableSearchwithUISearchController/Swift',
                           'Search.swift.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '11.0.3',
                'browserName': 'Safari',
                'udid': 'd2eba0cddbc41466267c0d4adda76c9f0ebfa3c9',
                'deviceName': 'iPhone 6s',
                'bundleId':'com.example.apple-samplecode.Search-swift'})
        
                                
        
        #self.driver = webdriver.Chrome('/usr/local/Cellar/chromedriver/2.32/bin/chromedriver')
        self.driver.get("http://phynbeta.com")
    #    import { IosDriver } from `appium-ios-driver`

#let defaultCaps = {
  #app: 'path/to/your.app',
 # platformName: 'iOS',
 # deviceName: 'iPhone 6'
#};

#let driver = new IosDriver();
#await driver.createSession(defaultCaps);
        
        #self.driver.man
        #output = 'C:\\Reports\TestReport.html'
        #test_suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromModule('testpages.py'))
        #runner = HTMLTestRunner(output=output)
        #runner.run(test_suite)
        #eMail='firooz.yazdi@phyn.com'
        #pAssword = 'phyn123'
   # @overrides(login)
    def test_login_phynbeta(self):
        """
        Tests phynbeta.com search feature. Searches for the word "phyn" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """
        login_page=page.MainPage(self.driver)
        login_page.login('firooz.yazdi@phyn.com', 'phyn123')
        #Load the main page. In this case the home page of phyn.org.
    #def test_search(self):
     #   main_page = page.MainPage(self.driver)
        #Checks if the word "phyn" is in title
     #   assert main_page.is_title_matches(), "phynbeta.com title doesn't match."
        #Sets the text of search textbox to "pycon"
     #   main_page.search_text_element = "Phyn"
     #   main_page.click_go_button()
     #   search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
     #   assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()