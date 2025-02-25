

from behave import given, when, then
from opencart.pageobjects.homePage import HomePage
from opencart.pageobjects.registerPage import RegisterPage

@given(u'User is in opencart "{option}" page')
@then(u'User is in opencart "{option}" page')
def step_impl(context, option):
    context.homeObj = HomePage(context.driver)
    if option.lower()=="home":
        context.homeObj.verifyHomePage()
    elif option.lower()=="my account":
        print("logic to validate my account page comes here")

@when(u'User select the "{option}" option')
def step_impl(context, option):
    if option.lower()=="register":
        context.homeObj.selectOption("Register")
    elif option.lower()=="login":
        context.homeObj.selectOption("Login")
    elif option.lower()=="logout":
        context.homeObj.selectOption("Logout")

@then(u'Validate the user is in "Register Account" page')
def step_impl(context):
    context.registerObj = RegisterPage(context.driver)
    context.registerObj.validateRegisterPage()


@when(u'User enters the personal details')
def step_impl(context):
    context.registerObj.enterPersonalDetails()

@when(u'User click the "Continue" button')
def step_impl(context):
    context.registerObj.selectButton("continue")


@then(u'User verify the "Your Account Has Been Created!" message')
def step_impl(context):
    context.registerObj.verifyPageCreated()

@then(u'User successfully logged out from the application')
def step_impl(context):
    context.homeObj.accountLogout()
