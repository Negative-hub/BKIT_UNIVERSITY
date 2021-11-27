Feature: testing the function get_roots_b
	Scenario: get roots of BQ
		Given I put roots [0, 4] into the function
		Then I get roots [0, 2, -2] 

	Scenario: get roots of BQ
		Given I put roots [9, 4] into the function
		Then I get roots [3, -3, 2, -2] 
