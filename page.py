import time
from element import BasePageElement
import locators
from pypkg2.locators import LoginPageLocators
class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    #locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. phynbeta"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "phyn" appears in page title"""
        return "Phyn" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        #element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        #element.click()
    def login(self):
        element1 = self.driver.find_element(*LoginPageLocators.EMAIL).send_keys('firooz.yazdi@phyn.com')
        time.sleep(2)
        element2 = self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys('phyn123')
        time.sleep(2)
        element3 = self.driver.find_element(*LoginPageLocators.SUBMIT)
        element3.click()
        time.sleep(2)
class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source