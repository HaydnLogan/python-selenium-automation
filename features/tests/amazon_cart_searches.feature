# Created by Haydn at 6/3/2021
Feature: Amazon Cart Searches (HW3)
  Verify number of Amazon Cart items

  Scenario: Check Amazon Cart is empty (Task 3)
    Given Open Amazon page
    When Click on Cart from Amazon home
    And Wait and See
    Then Verify Amazon Cart is empty


  Scenario: Check Amazon Cart has new item (Task 4)
    Given Open Amazon page
    When Search for Danish Butter Cookies
    And Click Amazons Choice
    And Add one time to cart
    Then Verify Amazon Cart new item