from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
  LOGO          = (By.ID, 'nav-logo')
  ACCOUNT       = (By.CSS_SELECTOR, 'input.full-width')
  SIGNUP        = (By.CSS_SELECTOR, '#nav-flyout-ya-newCust > a')
  LOGIN         = (By.CSS_SELECTOR, '.circle-button>p:nth-child(1)')
  SEARCH        = (By.ID, 'twotabsearchtextbox')
  SEARCH_LIST   = (By.ID, 's-results-list-atf')
  GO_BUTTON     = (By.ID, 'submit')

class LoginPageLocators(object):
  EMAIL         = (By.CSS_SELECTOR, 'input.full-width')
  PASSWORD      = (By.CSS_SELECTOR, '#app > div > div > div:nth-child(1) > div > div > div.login > div.account-info > form > div:nth-child(2) > input')
  SUBMIT        = (By.CSS_SELECTOR, '.circle-button>p:nth-child(1)')
  ERROR_MESSAGE = (By.ID, 'message_error')
  #from selenium.webdriver.common.by import By


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass