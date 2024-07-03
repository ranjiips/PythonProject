from get_chromedriver import Get_ChromeDriver


class LaunchPage(Get_ChromeDriver):

    def __init__(self):
        Get_ChromeDriver.__init__(self)

    def launchURL(self):
        self.driver.get('http"//www.google.co.in')

url=LaunchPage()
url.launchURL()