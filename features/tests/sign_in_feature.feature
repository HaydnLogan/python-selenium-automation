# Created by Haydn at 6/18/2021
Feature: Tests for sign in page


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opened

  Scenario: Sign in popup appears and disappears
    Given Open Amazon page
    Then Verify Sign in popup is clickable
    When Wait for 8 sec
    Then Verify Sign in popup is clickable
    Then Verify Sign in popup disappears