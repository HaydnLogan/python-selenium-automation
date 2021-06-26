# Created by Haydn at 6/26/2021
Feature: Loop test Best Seller links
  # HW6 Task 2


  Scenario: Loop test top 5 Best Seller links
    Given Open Amazon page
    When Click on Best Sellers
    Then Verify user can click through top 5