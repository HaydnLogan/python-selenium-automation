# Created by Haydn at 6/3/2021
Feature: Amazon Cart (HW3)
  Verify Amazon Cart is empty

  Scenario: Check Amazon Cart is empty
    Given Open Amazon page
    When Click on Cart from Amazon home
    And Wait and See
    Then Verify Amazon Cart is empty


  Scenario: Check Amazon Cart has new item
    Given Open Amazon page
    When Search for Danish Butter Cookies
    And Click Amazons Choice
    And Add one time to cart
    Then Verify Amazon Cart new item