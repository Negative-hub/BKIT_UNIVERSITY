Feature: testing Telegram bot
	Scenario: sum two digit
		Given I send bot message /start
		When I send bot first message 2
		When I send bot second message 6
		Then I send bot operation + and get answer 8