from . import _DataTool

class Company:
    def __init__(self, ticker):
        self.ticker          = ticker
        self.profile_soup    = None
        self.statistics_soup = None


    def get_profile(self):
        soup, dct = _DataTool.profile_of_company(self.ticker, self.profile_soup)
        self.profile_soup = soup
        return dct

    def get_statistics(self):
        soup, dct = _DataTool.statistics_of_company(self.ticker, self.statistics_soup)
        self.statistics_soup = soup
        return dct