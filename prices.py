import pandas as pd
import numpy as np
from getJson import getJSON

bannedAutoWords = ["Signed", "signed","SIGNED", "Non", "non", "IP","you", "Your","You", "YOUR", "YOU", "⚾(pick)", "pick)"]
bannedBaseWords = ["you", "You", "Your", "YOUR", "YOU"]

# Method that returns the lowest buy now prices for an "item" in a dataFrame that includes the items title, price, and eBay link
def currPrice(token, item, condition, auto):

    # How many items to search (200 is max)
    count = 200

    parseddoc = getJSON(token,item,condition, count)

    # Create series's for each items' title, price, and link
    prices = pd.Series()
    ids = []
    links = []
    try: 
        parseddoc["itemSummaries"]
    except:
        print("No comps found for: "+item)
        data = pd.DataFrame(columns = ["Title", "Price", "Link"])
    else: 
        # Traverse the JSON document and extract desired data
        i = 0
        for item in (parseddoc["itemSummaries"]):
            try:
                parse = item["title"].split(" ")
            except:
                parse = ""
            else:
                
                if(auto):
                    if not any(x in parse for x in bannedAutoWords):
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
                else: 
                    if not any(x in parse for x in bannedBaseWords):
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