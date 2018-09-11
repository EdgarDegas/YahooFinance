from YFTool.companies import get_profile_of
from YFTool.companies import get_statistics_of


# ticker of company to inspect
ticker = input('Enter ticker of company:')

print(get_profile_of(ticker))
print(get_statistics_of(ticker))