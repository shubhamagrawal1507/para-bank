Feature: Customer Login

  Scenario Outline: Perform transaction for the Customer
    Given the user is on the home page
    When the user selects "Customer Login"
    And the user select "Harry Potter" as the "Your Name"
    When the user clicks "Login"
    When the user selects "<Transaction>"
    And the user enters "<Amount>" as the "amount"
    When the user clicks "<Transaction>"
    Then transaction should be successful

    Examples:
      | Transaction | Amount |
      | Deposit     |   2000 |
      | Withdraw    |    500 |
      | Deposit     |    100 |
