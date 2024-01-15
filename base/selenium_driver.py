from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack

class Selenium_driver():
    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class':
            return By.CLASS
        elif locatorType == 'css':
            return By.CSS
        else:
            print('No locator found with :' + locatorType)
        return False

    def getElement(self,locator,locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print('Element found with locator:' + locator + ' and locator-type:' + locatorType )
        except:
            print('Element not found with locator:' + locator + ' and locator-type:' + locatorType)
        return element

    def clickElement(self,locator,locatorType):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            print('Clicked on element with locator: ' + locator + ' and locator type: '+ locatorType)

        except:
            print('Cannot click on element')


    def sendKeysElement(self,locator,locatorType,data):
        try:
            element = self.getElement(locator,locatorType)
            element.send_keys(data)
            print('Sent data on element with locator: ' + locator + ' and locator type: ' + locatorType)
        except:
            print('Cannot send data on element')

    def elementIsPresent(self,locator,locatorType):
        element = self.getElement(locator, locatorType)
        try:
            if element is not None:
                print('Element found using ' + locatorType)
                return True
            else:
                print('Element not found using ' + locatorType)
                return False
        except:
            print('Element not found using ' + locatorType)
            return False




