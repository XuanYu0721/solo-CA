Feature: Test site behavior
    Scenario: Users can view the home page
        Given I am on the homepage
        When I navigate to the home page
        Then I should see the welcome message
