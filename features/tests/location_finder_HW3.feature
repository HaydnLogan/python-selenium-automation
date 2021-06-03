# Created by Haydn at 6/3/2021
Feature: Check locations (HW3 Task 1 of 4)
  Verify locations are entered correctly

  Scenario: Homework location checker
    Given Open Amazon page
    When Navigate to register page
    And Click on Amazon logo
    And Go back
    And Verify Create Account text
    And Enter Name
    And Click on email field
    And Enter Password
    And ReEnter Password
    And Wait and See
    And Verify Password text
    And Click create on Registry
    And Go back
    And Click conditions
    And Go back
    And Click privacy
    And Go back
    And Click Sign in
    Then close page