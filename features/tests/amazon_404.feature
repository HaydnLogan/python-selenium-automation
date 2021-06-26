# Created by Haydn at 6/26/2021
Feature: Test for 404 page
  # Lesson 10 Class work

  Scenario: 404 page takes to Amazon Blog
    Given Open Amazon product Invalid_B07X8XJRS9 page
    When Store original windows
    When Click on the dog image
    When Switch to new window
    Then Verify Amazon Blog url
    Then Close new window
    When Return to original window
    Then Verify Amazon url