# Created by Haydn at 5/26/2021
Feature: Test Amazon search
  May 23 HW2

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked for "Table"

  Scenario: User can select pant colors  (lesson 8, HW5)
    Given Open Amazon product B07X8XJRS9 page
    Then Verify user can click through colors