# Created by Haydn at 5/26/2021
Feature: Help Search (HW2, May 23)
  User can search for solutions of Cancelling an order on Amazon

  Scenario: Help Search
    Given Open Amazon Help page
    When Search Library
    And Emulate Enter
    Then Verify Cancel