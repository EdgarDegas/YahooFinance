import YFTool as yf

# ticker of company to inspect
csv_file_path = input('Enter path of the CSV file path:')

try:
    yf.handle_csv(csv_file_path)
except OSError:
    print('File not found!')