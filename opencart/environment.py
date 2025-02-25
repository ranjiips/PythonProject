# import allure
# from allure_commons.types import AttachmentType
from selenium import webdriver

# from utils import configReader


def before_scenario(context, driver):

    # browser_name = configReader.read_configuration("basic info","browser")
    # url = configReader.read_configuration("basic info","url")

    browser_name = "chrome"
    url = "https://demo.opencart.com/en-gb?route=common/home"

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(url)


def after_scenario(context,driver):
    context.driver.quit()


# def after_step(context,step):
#     if step.status == 'failed':
#         allure.attach(context.driver.get_screenshot_as_png()
#                       ,name="failed_screenshot"
#                       ,attachment_type=AttachmentType.PNG)
