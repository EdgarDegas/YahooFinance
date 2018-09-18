from bs4 import BeautifulSoup

def parse_profile(doc):
    profile_soup = BeautifulSoup(doc)

    # narrow down to profile section
    profile_section = profile_soup.find('div', class_='qsp-2col-profile')

    # get data we are interested in
    company_name = profile_section.h3.string
    sector, industry, nb_employees = [tag.string for tag in profile_soup.find_all('strong')]
    return company_name, sector, industry, nb_employees
    


def parse_statistics(doc):
    statistics_soup = BeautifulSoup(doc)
    # narrow down to statistics section
    statistics_section = statistics_soup.find('section', attrs={ 'data-test' : 'qsp-statistics' })

    # get Market Cap (intraday) and 52-Week Change from section
    market_cap = statistics_section.find(string='Market Cap (intraday)').parent.parent.next_sibling.string
    fifty_two_week_change = statistics_section.find(string='52-Week Change').parent.parent.next_sibling.string
    return market_cap, fifty_two_week_change