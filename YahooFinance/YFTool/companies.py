import requests
from bs4 import BeautifulSoup

from enum import Enum

class DataType(Enum):
    profile    = 'profile'
    statistics = 'statistics'


def get_profile_of(ticker):
    # Fetch Profile Data
    # URL
    profile_url = _url_for_ticker(ticker, DataType.profile)

    # send request, convert response to Soup object
    profile_soup = _soup_from_URL(profile_url)

    # narrow down to profile section
    profile_section = profile_soup.find('div', class_='qsp-2col-profile')

    # get data we are interested in
    company_name = profile_section.h3.string
    sector, industry, nb_employees = [tag.string for tag in profile_soup.find_all('strong')]
    return company_name, sector, industry, nb_employees



def get_statistics_of(ticker):
    # Fetch Statistics Data
    # URL
    statistics_URL = _url_for_ticker(ticker, DataType.statistics)

    # send request, convert response to Soup object
    statistics_soup = _soup_from_URL(statistics_URL)

    # narrow down to statistics section
    statistics_section = statistics_soup.find('section', attrs={ 'data-test' : 'qsp-statistics' })

    # get Market Cap (intraday) and 52-Week Change from section
    market_cap = statistics_soup.find(string='Market Cap (intraday)').parent.parent.next_sibling.string
    fifty_two_week_change = statistics_soup.find(string='52-Week Change').parent.parent.next_sibling.string
    return market_cap, fifty_two_week_change


def _url_for_ticker(ticker, data_type):
    if data_type == DataType.profile:
        return 'https://finance.yahoo.com/quote/{}/profile'.format(ticker)
    else:  # if data_type == DataType.statistics
        return 'https://finance.yahoo.com/quote/{}/key-statistics'.format(ticker)

def _soup_from_URL(url):
    return BeautifulSoup(requests.get(url).text)