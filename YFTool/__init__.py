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