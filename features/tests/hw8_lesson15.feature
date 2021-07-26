Feature: HW 8, Lesson 15


  Scenario: User can select Appliances from drop down menu
    Given Open Amazon page
    When Select department by alias appliances
    And Search for Mini Fridge
    Then Verify Appliance department is selected


  Scenario: User see popup choices under New Arrivals
    Given Open Amazon product B074TBCSC8 page
    When Hover mouse over new arrivals
    Then Women fashion deals are shown
