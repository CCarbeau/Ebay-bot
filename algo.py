# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from myEmail import email
from analyze import aucTargets

# Time library
from datetime import datetime,timezone,timedelta

def main():
    # Permission code from eBay 
    token = "v^1.1#i^1#p^1#r^0#f^0#I^3#t^H4sIAAAAAAAAAOVYfWwURRS/6xcpH5JglVo1ORZJDeT2Zvf2vlZ65PqVnqHt2TsrXiRkbne2XbjbXXbmaA8hHkUIEKumCFIRgpAgGo1GmsZoFASNJgYDQcEAagyaGAnRUAwQNXF3e5RrJXz1Ept4/1zmzZs37/eb9+a9HZAtK5+7vmn9pWn2SUW7siBbZLczU0B5Wem8u4qLqkptIE/Bviv7ULakp/iX+RimkhrfhrCmKhg5ulNJBfOWsIZK6wqvQixjXoEphHki8NFQ80KepQGv6SpRBTVJOcL1NRQbQBwn+BmvBBOim/EYUuWqzZhaQ0kowXl9XuiGgYAEvawxj3EahRVMoEKM9YDlnIB1sp4Y4Hi3n+d8tBcE4pSjHelYVhVDhQZU0HKXt9bqeb7e2FWIMdKJYYQKhkON0dZQuL6hJTbflWcrmOMhSiBJ49GjOlVEjnaYTKMbb4MtbT6aFgSEMeUKDu8w2igfuurMHbhvUZ0AHOcWpYDE+JiAAKSCUNmo6ilIbuyHKZFFp2Sp8kghMsncjFGDjcRSJJDcqMUwEa53mH+PpWFSlmSk11ANtaEnQ5EIFazr1GVMZOjECOpCpzPSVu9MQAQ9HpbxOD2cl+USjDu3zbCtHMlj9qlTFVE2KcOOFpXUIsNnNJYZNo8ZQ6lVadVDEjH9ydfzjjDoi5tHOnyGadKpmKeKUgYNDmt4c/5HVhOiy4k0QSMWxk5YBNVQUNNkkRo7aUViLni6cQ3VSYjGu1xdXV10l5tW9Q4XCwDjWtS8MCp0ohSkLF0z1019+eYLnLIFRUDGSizzJKMZvnQbkWo4oHRQQc4fCARAjvfRbgXHSv8lyMPsGp0PBcsP6Pd6OMnt5xIe4ObEQuRHMBeiLtMPlIAZZwrqyxDRklBATsGIs3QK6bLIuz0S6/ZLyCl6A5KTC0iSM+ERvU5GQggglEgIAf//J01uNdCjSNARKVCkFyjKA8tXdIcYIum1PqndHzNqWXyeGvUvrVve1vZobSty6ZBrETzsE8s7am41F64Lvi4pG8zEjP0LRYCZ64UhoUnFBInjghcVVA1F1KQsZCbWAbt1MQJ1komiZNIQjAtkSNPChbqpCwTvti6JO0NdyPr0n9Sm66LCZsBOLFTmemwYgJpMm9WHFtSUS4VG2+Eyc90QL7G8Hhdu2ehZJxRqA+QwWlkcbjZpCzKNVwi0jrCa1o0+m241u6+YugwpRjUjuppMIr2dGXc2p1JpAhNJNNHSugABLsMJVmoZH/D73Z4A6xsXLsEqpEsm2pVUuIu4ZMFtNtSu0R/3QZv1Y3rsh0CP/eMiux3MB3OY2WBWWfHjJcVTq7BMEC1DicZyh2J8s+qIXoYyGpT1orttF3ZvaaqramjdOvfpWObo9s9tU/PeFnYtBpUjrwvlxcyUvKcG8MC1mVJm+sxpLAdY1gM4o0X3xcHsa7MlzL0lFVvckdcr+vsHui92l9m+2v5T5s0BL5g2omS3l9pKeuy2zOB73/z2cNX9yYGK03Mf3P9dy6Dae7JpzZn9L//Zd/nKcf/Ms5OHJv9c7q1at+jr3a2uikvwwLpXz8/5qPLXJc/NOrxKP904tbe0f8fvwenpjbHjBz/LhNNDmxrI0ILT3/Mt7qc2Hy4/HqEr//ihb+Uk+OOmvVWvkJd6mwZ3Nl04ceqDwZ3as74XzjnOnD/6fOnAW18cOXRyT/zvy57qRyJnP12/8czbLZvPnYydWst8mJly0RZ3oNV034xt+6ob3r/SvqN6m3/Gu1nQfsC26pPevpIX79sTdx1847VmCWzYV/TX6obqYyufWTPU96XjnsV9zZWXN2zVyoKOd0q/FfeurZzUeOkIc0I81pYFw2f5D07nolr1EQAA"
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=1)
    
    item = "2023 topps chrome psa 10"
    
    prices = currPrice(token, item, condition["Graded"])
    auctions = currAucPrices(token, item, condition["Graded"], (date+timeRange).isoformat()[:23])
    print(prices)
    print(aucTargets(prices,auctions))

if __name__ == "__main__":
    main()