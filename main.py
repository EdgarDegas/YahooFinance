import YFTool as yf

while True:
    ticker = input('\n\nEnter company ticker: ')

    company = yf.Company(ticker)

    print('\n\nProfile of {}'.format(ticker))

    for k, v in company.get_profile().items():
        print(k, ':', v)


    print('\n\nStatistics of {}'.format(ticker))

    for k, v in company.get_statistics().items():
        print(k, ':', v)