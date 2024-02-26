import pandas as pd
import numpy as np 
from getJson import getJSON

# Function will get the json file from the getJSON library and return a dataframe of best offer cards 
# sorted from lowest to highest price
def bestOffPrices(token, item, condition):
    count = 200; 
    
    parsseddoc = getJSON(token,item,condition, count)

    # Create series's for each items' title, price, and link
    prices = pd.Series()
    ids = []
    links = []

    i = 0
    for item in parsseddoc["itemSummaries"]:
        if "BEST_OFFER" in item["buyingOptions"]:
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
    bestOffers = pd.DataFrame(columns=["Title", "Price", "Link"])
    bestOffers["Title"]=ids
    bestOffers["Price"]=prices
    bestOffers["Link"]=links

    # Sort dataFrame by price from least to greatest
    bestOffers = bestOffers.sort_values(by="Price")

    return bestOffers


# if __name__ == "__main__":
#     token = "v^1.1#i^1#r^0#p^1#I^3#f^0#t^H4sIAAAAAAAAAOVYa2wUVRTe3bZoUx4+UAmBuAyiFJzZO7PPmXTXbFvoI9Cu3dJiQZu7s3faaXdmlrl36S7UUCsi/DBiVKwQtdiQaqQQX0TEoFEDokSMSqIEowFBJZGgfzCEoDPTUraV8OomNnH/bObcc8/9vu+ec8+dAV0TCuetq1x3dpL9JkdvF+hy2O1sESicUDB/cp5jeoENZDnYe7vu6crvzvu1BEMlkRTqEE5qKkbOtJJQsWAZg1RKVwUNYhkLKlQQFogoRMOLFwkcA4SkrhFN1BKUs6o8SAVYnx/EYFzkeRSAPG9Y1Ysx67Ug5QdQYjleBAGPaPixxjjGKVSlYgJVEqQ4wHlowNGct571CoATWA/DsmwT5WxAOpY11XBhABWy4ArWXD0L65WhQoyRTowgVKgqvDBaG64qX1BTX+LKihUa0iFKIEnhkU9lWhw5G2Aiha68DLa8hWhKFBHGlCs0uMLIoEL4IpgbgG9JzbPQ55PcLAz4faLki+dEyoWarkByZRymRY7TkuUqIJXIJHM1RQ01Ym1IJENPNUaIqnKn+fdgCiZkSUZ6kFpQGn4oHIlQobJWXcZEhjRGUBdb6UhdOR2DCHq9HOulvR4f54mx7qFlBmMNiTxqnTJNjcumZNhZo5FSZGBGI5XxCN4sZQynWrVWD0vExJPt57+oIPA1mVs6uIcp0qqau4oUQwan9Xh1/YdnE6LLsRRBwxFGD1gCBSmYTMpxavSglYlDyZPGQaqVkKTgcnV0dDAdbkbTW1wcAKxr6eJFUbEVKZCyfM1aN/3lq0+gZYuKiIyZWBZIJmlgSRuZagBQW6iQJ8DzPBjSfSSs0GjrvwxZnF0j6yFX9eHhAXRzPPDzEPEsK+aiPkJDKeoycaAYzNAK1NsRSSagiGjRyLOUgnQ5Lri9EucOSIiO+3iJ9vCSRMe8cR/NSggBhGIxkQ/8f8rkWhM9ikQdkRxleo6ynF+xMh1miaSX+qWGQL3Ry5rma9FAW9mKurrq0lrk0qGnRvRyjStagtdaC5clX5aQDWXqjfVzJYBZ67kRoVLDBMXHRC8qakkU0RKymBlfG+zW4xGok0wUJRKGYUwkw8lkVa5O6hzRu65D4sZY57I//Se96bKssJmw44uVOR8bAWBSZszuw4ia4tKgce1wmbVumJst1GPiLRt31nHF2iA5yFaOD142GYsyg1eKjI6wltKNezZTa96+6rV2pBrdjOhaIoH0BnbM1awoKQJjCTTeyjoHCS7DcdZqWT8IBPxut9szJl6i1Uibx9uRlLuDOP+B67xQu0a+3Ids1o/ttn8Muu17HXY7KAFz2Nlg1oS8Jfl5E6djmSBGhhKD5RbVeGfVEdOOMkko647bbX+++nxl2fQFtZvmra7PfLVlv21i1reF3ofBtOGvC4V5bFHWpwYw49JIATvlrkmcB3Ccl/UCjvU0gdmXRvPZO/On9n64vGmKrfiOZnjmPvqPF3vn/HBUAJOGnez2Alt+t91WW9Jzcvu0nmMHzv64sWTXhT7nkYOFFY37XtZTFwaKivuebjuA059xA9UVH32ybe3uSCbE739tZn9n54mZzx1X1kzbee6viVzR77yQ3zfDP999obhna//5ZYIymU18u/L+CDV1+8632jd1Hj7X1n/6ltZdfHfeG0vvPfD6140dPec3Pia933Pwg8d7H90KNpQ2Lj+6fNZPL7iWpI6w3V9Qq5VVeyq3tR165XDl3M+fWbZm4M3v9OAZx88v7X2nv+ab6opf1mcOEcdv755ID5w6ld5Qsfm9k7vXFJx2TZk7x/HpDv+W2DHl5n1P9q1ae/zvmuoZsHkhc9uzxZ1fRvbAW78PRd/ece7uzRseeeKposG9/AfXkITu9REAAA=="
#     item = "2023 topps anthony-volpe psa 10"
#     condition = "2750"
#     bestOffPrices(token,item,condition, 200)