import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'When I Navigate to the link "https://www.saucedemo.com/"')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    time.sleep(2)


@then(u'I validate the header text is "{header}"')
def step_impl(context, header):
    element = context.driver.find_element(By.CLASS_NAME, "login_logo")
    pageHeader = element.text
    assert header == pageHeader, f"The expected page header '{header}' is NOT loaded, instead '{pageHeader}' loaded"
    print(f"{pageHeader} loaded successfully")


@then(u'I can see the login page loaded successfully')
def step_impl(context):
    element = context.driver.find_element(By.ID, "login-button")
    assert element.is_displayed(), "Login button is not loaded"


@when(u'I Enter the user name "{username}"')
def step_impl(context, username):
    element = context.driver.find_element(By.ID,"user-name")
    element.send_keys("standard_user")


@when(u'I Enter the password "{password}"')
def step_impl(context,password):
    element = context.driver.find_element(By.XPATH,"//input[@id='password']")
    element.send_keys("secret_sauce")


@when(u'I Click the login button')
def step_impl(context):
    element = context.driver.find_element(By.XPATH,"//input[@id='login-button']")
    element.click()

    time.sleep(3)


@then(u'I can see the "{products}" page loaded successfully')
def step_impl(context, products):
    element = context.driver.find_element(By.XPATH,"//span[@class='title']")
    productHeader = element.text
    assert products == productHeader, "Products page not loaded"
    print(f"{productHeader} page loaded successfully")


@when(u'I add the product "Sauce Labs Fleece Jacket" into the cart')
def step_impl(context):
    element = context.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
    element.click()
    # time.sleep(2)


@when(u'I Click the cart icon')
def step_impl(context):
    element = context.driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']")
    element.click()
    # time.sleep(3)

@then(u'I can see the product "{productname}" in the cart screen')
def step_impl(context,productname):
    element = context.driver.find_element(By.ID,"item_5_title_link")
    pageTitle = element.text
    assert productname == pageTitle, "product title is not populated"
    print(f"{pageTitle} is populated successfully in the cart")


@when(u'I Click the continue to Shopping button')
def step_impl(context):
    element = context.driver.find_element(By.ID,"continue-shopping")
    element.click()


@when(u'I Logout from the application')
def step_impl(context):
    element=context.driver.find_element(By.ID,"react-burger-menu-btn")
    element.click()
    time.sleep(2)
    logoutButton=context.driver.find_element(By.ID,"logout_sidebar_link")
    logoutButton.click()
    time.sleep(2)
