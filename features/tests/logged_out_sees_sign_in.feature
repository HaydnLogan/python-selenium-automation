# Created by Haydn at 5/26/2021
Feature: Logged out checker (HW2, May 23)
  Logged out user sees Sign in page when clicking Orders

  Scenario: Logged out clicks Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign-In shown
