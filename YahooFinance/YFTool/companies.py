import requests
from . import parser

from enum import Enum

class DataType(Enum):
    profile    = 'profile'
    statistics = 'statistics'


def get_profile_of(ticker):
    # Fetch Profile Data
    # URL
    profile_url = _url_for_ticker(ticker, DataType.profile)

    # send request, convert response to Soup object
    doc = _html_doc_from_URL(profile_url)
    return parser.parse_profile(doc)


def get_statistics_of(ticker):
    # Fetch Statistics Data
    # URL
    statistics_URL = _url_for_ticker(ticker, DataType.statistics)

    # send request, convert response to Soup object
    doc = _html_doc_from_URL(statistics_URL)
    return parser.parse_statistics(doc)




def _url_for_ticker(ticker, data_type):
    if data_type == DataType.profile:
        return 'https://finance.yahoo.com/quote/{}/profile'.format(ticker)
    else:  # if data_type == DataType.statistics
        return 'https://finance.yahoo.com/quote/{}/key-statistics'.format(ticker)

def _html_doc_from_URL(url):
    return requests.get(url).text