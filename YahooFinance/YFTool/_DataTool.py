import requests
from bs4 import BeautifulSoup


def profile_of_company(ticker, profile_soup=None):
    """
    Returns a BeautifulSoup object and a dictionary with keys: 
    Company Name, Sector, Industry, Number of employees.
    """

    if profile_soup is None:
        profile_soup = _profile_soup_of_company(ticker)

    company_name_tag = profile_soup.h3
    strong_lst = profile_soup.find_all('strong')

    profile_dct = { 'Company Name' : company_name_tag.string,
                          'Sector' : strong_lst[0].string,
                        'Industry' : strong_lst[1].string,
             'Number of employees' : int(strong_lst[2].string.replace(',', ''))
    }

    return profile_soup, profile_dct


def statistics_of_company(ticker, statistics_soup=None):
    """
    Returns a BeautifulSoup object and a dictionary with keys: 
    Market Cap ($ millions), 52 Week Price Change In %, 
    Average Trading Volume Last 3 Months (thousands).
    """

    if statistics_soup is None:
        statistics_soup = _statistics_soup_of_company(ticker)

    statistics_dct = {       'Market Cap ($ millions)' : _value_of_key(statistics_soup, 'Market Cap (intraday)'),
                           '52 Week Price Change In %' : _value_of_key(statistics_soup, '52-Week Change'),
    'Average Trading Volume Last 3 Months (thousands)' : _value_of_key(statistics_soup, 'Avg Vol (3 month)')
    }

    return statistics_soup, statistics_dct



def _profile_soup_of_company(ticker):
    """
    Returns a BeautifulSoup object, which represents the HTMl node
    that contains Profile info associated with ticker.
    """

    url = r"""https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}""".format(ticker=ticker)

    soup = _response_soup_of_url(url)
    two_col_profile = soup.find('div', class_='qsp-2col-profile')

    return two_col_profile


def _statistics_soup_of_company(ticker):
    """
    Returns a BeautifulSoup object, which represents the HTMl node
    that contains Statistics info associated with ticker.
    """

    url = r"""https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}""".format(ticker=ticker)

    soup = _response_soup_of_url(url)
    qsp_statistics = soup.find('section', attrs={ 'data-test' : 'qsp-statistics' })

    return qsp_statistics



def _response_soup_of_url(url):
    """
    Sends a GET request to url, then returns a BeautifulSoup object
    which represents the response body coresponding to the request.
    """

    headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3536.0 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def _value_of_key(soup, key):
    """
    Returns value coresponding to key from HTML table.
    """

    return soup.find(string=key)[0].parent.parent.next_sibling.string


def main():
    statistics_of_company('CEA')

if __name__ == '__main__':
    main()