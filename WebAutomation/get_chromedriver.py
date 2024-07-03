from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class FailedToLoadPage(Exception):
    pass


class Get_ChromeDriver():

    PythonURL = 'https://robotframework.org/'
    RobotURL = 'https://robotframework.org/'
    DefaultURL = 'https://www.google.com/'
    LetsKodeIt = 'https://letskodeit.teachable.com/'
    PracticePage = 'https://courses.letskodeit.com/practice'

    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path='.\\Drivers\\chromedriver_97.exe')
        s = Service('.\\Drivers\\chromedriver_100.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def navigateToPage(self,application):
        self.launchpageURL(application)

    def launchpageURL(self, application):
        if 'python' in application.lower():
            self.driver.get(self.PythonURL)
            self.validatePageTitle('Welcome to Python.org')
        elif 'robot' in application.lower():
            self.driver.get(self.RobotURL)
            self.validatePageTitle('Robot Framework')
        elif 'letskode' in application.lower():
            self.driver.get(self.LetsKodeIt)
            self.validatePageTitle('Let\'s Kode')
        elif 'practicepage' in application.lower():
            self.driver.get(self.PracticePage)
            self.validatePageTitle('Practice Page')
        else:
            self.driver.get(self.DefaultURL)
            self.validatePageTitle('Google')

    def validatePageTitle(self, expectedTitle):
        try:
            pagetitle = self.driver.title
            print(f'Actual Title: {pagetitle} Expected Title: {expectedTitle}')
            if expectedTitle.lower() in pagetitle.lower():
                print(f'Given page: {pagetitle} loaded successfully')
            else:
                raise FailedToLoadPage
        except FailedToLoadPage:
            print(f'Exception Occurred: The expected page: {expectedTitle} is not loaded. Instead loaded {pagetitle}')
        except Exception as e:
            print('Exception Occurred:\n'+str(e))
            print(f'Exception Occurred: The expected page: {expectedTitle} is not loaded. Instead loaded {pagetitle}')

    def closeBrowser(self):
        self.driver.close()

    def select_car_radiobtn(self, carname):
        ele = self.driver.find_element(By.XPATH,f"//div[@id='radio-btn-example']//input[@value='{carname.lower()}']")

    def list_of_elements(self):
        ele = self.driver.find_elements(By.XPATH, "//div[@id='radio-btn-example']//input[@type='radio']")
        length = len(ele)
        tagele = self.driver.find_elements(By.TAG_NAME, 'td')
        length = len(ele)

    def click_on_element(self,locator):
        self.driver.find_element(locator)


dd=Get_ChromeDriver()
dd.navigateToPage('PracticePage')
dd.closeBrowser()