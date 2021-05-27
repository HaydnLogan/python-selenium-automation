# Created by Haydn at 5/26/2021
Feature: Test Amazon search
  May 23 HW2

  Scenario: # User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked