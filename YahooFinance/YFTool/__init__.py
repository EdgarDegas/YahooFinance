"""YFTool is a tool to fetch information about a company according to its ticker.  

How to Use:

import YFTool as yf  
some_company = yf.Company('CEA')  

some_company.get_profile()  
some_company.get_statistics()

"""

from ._companies import Company