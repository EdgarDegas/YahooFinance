"""YFTool is short for Yahoo Finance
Tool. Use YFTool to fetch Profile and
statistics information of a company
according to its ticker.
"""


"""

Abstract

YF stands for Yahoo Finance.  
YFTool is used to get a company's profile and statistics information from https://finance.yahoo.com.

---


How to use

```
import YFTool as yf

company = yf.Company(ticker=)

company.get_profile()
company.get_statistics()
```

"""

from ._Companies import Company