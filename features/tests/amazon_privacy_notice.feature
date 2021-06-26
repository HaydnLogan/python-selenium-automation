# Created by Haydn at 6/26/2021
Feature: Switch to new Privacy page
  # HW6 Task 1

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to new window
    Then Verify Amazon Privacy Notice page is opened
    Then Close new window
    When Return to original window