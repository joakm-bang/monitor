# This keeps track of the scrapers

Each scraping computer checks in to Heroku every 5 minutes provided the code didn't crash. This code publishes a list of their latest activity on https://gentle-eyrie-28039.herokuapp.com/monitor/activity/ and sends me an email whenever a computer has not checked in for 10 minutes.

