Feature: Verify the product in the cart

#Background:

 Scenario: Add and verify the product in the Cart page
 Given When I Navigate to the link "https://www.saucedemo.com/"
 Then I validate the header text is "Swag Labs"
 And I can see the login page loaded successfully
 When I Enter the user name "standard_user"
 And I Enter the password "secret_sauce"
 And I Click the login button
 Then I can see the "Products" page loaded successfully
# When I add the product "Sauce Labs Fleece Jacket" into the cart
# And I Click the cart icon
# Then I can see the product "Sauce Labs Fleece Jacket" in the cart screen
# When I Click the continue to Shopping button
# Then I can see the "Products" page loaded successfully
# When I Logout from the application
# Then I can see the login page loaded successfully