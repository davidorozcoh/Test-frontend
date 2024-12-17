@regression_tests

Feature: Validate element created dropdown column

  Background:
    Given I navigate to the kayak main page

  Scenario: Navigate to the Kayak home page and validate principal elements
    Then I should be in the "home" page
    And The url page should be equal to the next "https://www.kayak.com.co/" url

  Scenario Outline: Navigate through the left menu and validate the page opens correctly
    When I click on the dropdown button to open the left menu
    And I click on the "<menu_option>" button
    Then I should see the "<expected_title>" page

    Examples:
      | menu_option   | expected_title          |
      | Stays         | Buscar hoteles          |
      | Cars          | Buscar autos            |
