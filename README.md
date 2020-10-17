# Scrape Data from Linked and then Connect to them
You need to fill in the necessary details in the parameters.py file, for logging into LinkedIn, as well as, the route to Chrome driver
You first log into the Linked In account, using, your credentials.
Then you search in Google for a pythn developer in Linked In, from a location. In the parameters.py, the search query has been mentioned for Washington DC.
You may change the place, according to your wish, in the code.
Then the results from the search, are scraped one by one. The name, designation and the place has been scraped from the Linked in profile.
Each of the scraped data, along with the URL is stored in the CSV file.
A connection request will be send to each and every profile in the search result.
Technology Used : Selenium, Python, Parsel package

Required Packages: selenium, parsel, csv
