Feature: Register the Opencart application


  Scenario: User Registers into opencart Application
    Given User is in opencart "home" page
    When User select the "Register" option
    Then Validate the user is in "Register Account" page
    When User enters the personal details
    And User click the "Continue" button
    Then User verify the "Your Account Has Been Created!" message
    When User click the "Continue" button
    Then User is in opencart "my account" page
    When User select the "Logout" option
    Then User successfully logged out from the application

