import pandas as pd
import numpy as np
from getJson import getJSON

# Method that returns the lowest buy now prices for an "item" in a dataFrame that includes the items title, price, and eBay link
def currPrice(token, item, condition):

    # How many items to search (200 is max)
    count = 200

    parseddoc = getJSON(token,item,condition, count)

    # Create series's for each items' title, price, and link
    prices = pd.Series(index = np.arange(count))
    ids = []
    links = []

    # Traverse the JSON document and extract desired data
    i = 0
    for item in (parseddoc["itemSummaries"]):
        try: 
            ids.append(item["title"])
        except: 
            ids.append("None")

        try:
            links.append(item["itemWebUrl"])
        except:
            links.append("None")
        
        try:
            price = float(item["price"]["value"])
        except:
            price = 100000
        try:
            price = price + float(item["shippingOptions"][0]["shippingCost"]["value"])
        except:
            # Add an arbitrary 5 dollars if shipping price isn't specified 
            price = price + 5

        prices[i] = float(price)
        i = i + 1

    # Create dataFrame with the series created in the loop above
    data = pd.DataFrame(columns = ["Title", "Price", "Link"])
    data["Title"]=ids
    data["Price"]=prices
    data["Link"]=links

    # Sort dataFrame by price from least to greatest
    data = data.sort_values(by="Price")

    return data