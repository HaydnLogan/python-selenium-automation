# Created by Haydn at 6/3/2021
Feature: Amazon Cart Searches (HW3, Tasks 3 and 4)
  Verify number of Amazon Cart items

  Scenario: Check Amazon Cart is empty (HW3 Task 3)
    Given Open Amazon page
    When Click on Cart from Amazon home
    And Wait and See
#   Then Verify Amazon Cart is empty #HW3
    Then "Your Amazon Cart is empty" message is displayed


  Scenario: Check Amazon Cart has new item (HW3 Task 4)
    Given Open Amazon page
#   When Search Danish Butter Cookies
    When Search for Dress
    When Click on the second product
#   And Click Amazons Choice
#   And Add one time to cart
    And Click on Add to cart button
    # Then Verify Amazon Cart new item
    Then Verify cart has 1 item