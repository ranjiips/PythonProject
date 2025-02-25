import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BaseMethod():

    def __init__(self, driver):
        self.driver = driver

    def enterText(self, locator_type, locator_value, text_to_entered):
        # element = self.get_element(locator_type, locator_value)
        self.wait_until_element_visible(locator_type, locator_value)
        element = self.wait_until_element_clickable(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_entered)

    def clickElement(self, locator_type, locator_value):
        # element = self.get_element(locator_type, locator_value)
        self.wait_until_element_visible(locator_type, locator_value)
        element = self.wait_until_element_clickable(locator_type, locator_value)
        element.click()

    def getElementText(self, locator_type, locator_value):
        element = self.wait_until_element_visible(locator_type, locator_value)
        return element.text

    def getCurrentURL(self):
        return self.driver.current_url

    def hard_wait(self):
        time.sleep(2)

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType.__eq__("id"):
            return By.ID
        elif locatorType.__eq__("name"):
            return By.NAME
        elif locatorType.__eq__("xpath"):
            return By.XPATH
        elif locatorType.__eq__("css"):
            return By.CSS_SELECTOR
        elif locatorType.__eq__("class"):
            return By.CLASS_NAME
        elif locatorType.__eq__("link"):
            return By.LINK_TEXT
        else:
            return False

    def get_element(self, locator_type, locator_value):
        element = None
        byType = self.getLocatorType(locator_type)
        element = self.driver.find_element(byType, locator_value)
        return element

    def scroll_to_element(self,locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_until_element_clickable(self, locator_type, locator_value, timeout=60):
        byType = self.getLocatorType(locator_type)
        wait=WebDriverWait(self.driver,timeout)
        return wait.until(EC.element_to_be_clickable((byType,locator_value)))

    def wait_until_element_visible(self, locator_type, locator_value, timeout=60):
        byType = self.getLocatorType(locator_type)
        wait=WebDriverWait(self.driver,timeout)
        return wait.until(EC.visibility_of_element_located((byType,locator_value)))

