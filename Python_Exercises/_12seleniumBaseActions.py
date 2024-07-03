from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumBaseActions(object):

    global driver

    def __int__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    #def launch_browser_and_maximize(self):

    def load_webPage(self, url):
        # Open the Url
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def get_page_title(self):
        return self.driver.title


    def get_current_url(self):
        # Get Current Url
        currentUrl = self.driver.current_url
        print("Current Url of the web page is: " + currentUrl)

    def enter_text(self, locator, inputValue):
        #wait for the element is visible
        element = self.wait_till_element_visible(locator)
        if element.is_enabled():
            #enter the text
            element.send_keys(inputValue)
        else:
            raise Exception("The field is not in Enabled state")

    def click_element(self, locator):
        element = self.wait_till_element_clickable(locator)
        if element.is_enabled():
            element.click()
        else:
            raise Exception("The field is not in Enabled state")

    def getByType(self, locatorType):
        if locatorType.lower() == "id":
            return By.ID
        elif locatorType.lower() == "name":
            return By.NAME
        elif locatorType.lower() == "xpath":
            return By.XPATH
        elif locatorType.lower() == "css":
            return By.CSS_SELECTOR
        elif locatorType.lower() == "class":
            return By.CLASS_NAME
        elif locatorType.lower() == "linktext":
            return By.LINK_TEXT
        elif locatorType.lower() in "partial":
            return By.PARTIAL_LINK_TEXT
        elif locatorType.lower() in "tag":
            return By.TAG_NAME

    def wait_till_element_visible(self, locator):
        wait = WebDriverWait(self.driver, timeout=30)
        return wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR(locator)))

    def wait_till_element_clickable(self, locator):
        wait = WebDriverWait(self.driver, timeout=30)
        return wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR(locator)))

    def wait_till_all_elements_present_in_page(self, locator):
        wait = WebDriverWait(self.driver, timeout=30)
        return wait.until(EC.presence_of_all_elements_located(locator))

    def refresh_the_page(self):
        # Browser Refresh
        self.driver.refresh()
        print("Browser Refreshed")

    def back_one_page(self):
        # Browser Back
        self.driver.back()
        print("Go one step back in browser history")

    def forward_one_page(self):
        # Browser Forward
        self.driver.forward()
        print("Go one step forward in browser history")

    def get_page_source(self):
        # Get Page Source
        return self.driver.page_source

    def close_borwser(self):
        # Browser Close / Quit
        # driver.close()
        self.driver.quit()

    #def select_radio_option(self, locator, value):




