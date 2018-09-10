import requests
from bs4 import BeautifulSoup

# ticker of company to inspect
ticker = 'CEA'

# Fetch Profile Data
# URL
profile_url = 'https://finance.yahoo.com/quote/{}/profile'.format(ticker)

# send request, convert response to Soup object
profile_response = requests.get(profile_url)
profile_soup = BeautifulSoup(profile_response.text)

# narrow down to profile section
profile_section = profile_soup.find('div', class_='qsp-2col-profile')

# get data we are interested in
company_name = profile_section.h3.string
sector, industry, nb_employees = [tag.string for tag in profile_soup.find_all('strong')]



# Fetch Statistics Data
# URL
statistics_URL = 'https://finance.yahoo.com/quote/{}/key-statistics'.format(ticker)

# send request, convert response to Soup object
statistics_response = requests.get(statistics_URL)
statistics_soup = BeautifulSoup(statistics_response.text)

# narrow down to statistics section
statistics_section = statistics_soup.find('section', attrs={ 'data-test' : 'qsp-statistics' })

# get Market Cap (intraday) and 52-Week Change from section
market_cap = statistics_soup.find(string='Market Cap (intraday)').parent.parent.next_sibling.string
fifty_two_week_change = statistics_soup.find(string='52-Week Change').parent.parent.next_sibling.string

print(company_name)
print(market_cap)