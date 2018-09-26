from ._company_helper import get_profile_of
from ._company_helper import get_statistics_of

class Company:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_profile(self):
        return get_profile_of(self.ticker)

    def get_statistics(self):
        return get_statistics_of(self.ticker)
