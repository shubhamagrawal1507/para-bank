Feature: Bank Manager Login

  Scenario: Add a New Customer
    Given the user is on the home page
    When the user selects "Bank Manager Login"
    When the user selects "Add Customer"
    And the user enters "Ramesh" as the "First Name"
    And the user enters "Gupta" as the "Last Name"
    And the user enters "400001" as the "Post Code"
    When the user clicks "Add Customer"
    Then a new customer should be added successfully

  Scenario: Open Account for the Customer
    Given the user is on the home page
    When the user selects "Bank Manager Login"
    When the user selects "Open Account"
    And the user select "Harry Potter" as the "Customer"
    And the user select "Dollar" as the "Currency"
    When the user clicks "Process"
    Then a new account should be added successfully


