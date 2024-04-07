import pandas as pd
import numpy as np
from getJson import getJSON
from model import pricingModel

bannedAutoWords = ["Signed", "signed","SIGNED", "Non", "non", "IP","you", "Your","You", "YOUR", "YOU", "⚾(pick)", "pick)", "Non-Auto","MYSTERY", "Beckett"]
bannedBaseWords = ["you", "You", "Your", "YOUR", "YOU", "Pick)"]

# Method that returns the lowest buy now prices for an "item" in a dataFrame that includes the items title, price, and eBay link
def currPrice(token, item, condition, auto):

    # How many items to search (200 is max)
    count = 10

    parseddoc = getJSON(token,item,condition, count)

    # Create series's for each items' title, price, and link
    pricesPrices = pd.Series()
    pricesIDs = []
    pricesLinks = []

    bestOfferPrices = pd.Series()
    bestOfferIDs = []
    bestOfferLinks = []

    buyNowPrices = pd.Series()
    buyNowIDs = []
    buyNowLinks = []


    try: 
        parseddoc["itemSummaries"]
    except:
        print("No comps found for: "+item)
        return [[],[],[]]
    else: 
        # Traverse the JSON document and extract desired data

        # i is the tracker for prices, j is the tracker for bestOffer, k is the tracker for buyNow
        i = 0
        j = 0
        k = 0 

        for item in (parseddoc["itemSummaries"]):
            try:
                parse = item["title"].split(" ")
            except:
                parse = ""
            else:
                if(auto):
                    if not any(x in parse for x in bannedAutoWords):
                        firstPrice = 10000
                        if(i!=0):
                            firstPrice = pricesPrices[0]
                        try:
                            price = float(item["price"]["value"])
                        except:
                            price = 100000
                        if(price <= firstPrice * pricingModel(price)):
                            try: 
                                title = item["title"]
                            except:
                                title = "None"

                            pricesIDs.append(title)
                
                            try:
                                link = item["itemAffiliateWebUrl"]
                            except:
                                link = "None"

                            pricesLinks.append(link)
                            
                            try:
                                price = price + float(item["shippingOptions"][0]["shippingCost"]["value"])
                            except:
                                # Add an arbitrary 5 dollars if shipping price isn't specified 
                                price = price + 5

                            pricesPrices[i] = float(price)
                            i = i + 1

                            if "BEST_OFFER" in item["buyingOptions"]:
                                bestOfferIDs.append(title)
                                bestOfferLinks.append(link)
                                bestOfferPrices[j] = float(price)

                                j = j + 1
                            else: 
                                buyNowIDs.append(title)
                                buyNowLinks.append(link)
                                buyNowPrices[k] = float(price)

                                k = k + 1
                else: 
                    if not any(x in parse for x in bannedBaseWords):
                        firstPrice = 10000
                        if(i!=0):
                            firstPrice = pricesPrices[0]
                        try:
                            price = float(item["price"]["value"])
                        except:
                            price = 100000
                        if(price <= firstPrice * pricingModel(price)):
                            try: 
                                title = item["title"]
                            except:
                                title = "None"

                            pricesIDs.append(title)
                
                            try:
                                link = item["itemAffiliateWebUrl"]
                            except:
                                link = "None"

                            pricesLinks.append(link)
                            
                            try:
                                price = price + float(item["shippingOptions"][0]["shippingCost"]["value"])
                            except:
                                # Add an arbitrary 5 dollars if shipping price isn't specified 
                                price = price + 5

                            pricesPrices[i] = float(price)
                            i = i + 1

                            if "BEST_OFFER" in item["buyingOptions"]:
                                bestOfferIDs.append(title)
                                bestOfferLinks.append(link)
                                bestOfferPrices[j] = float(price)

                                j = j + 1
                            else: 
                                buyNowIDs.append(title)
                                buyNowLinks.append(link)
                                buyNowPrices[k] = float(price)

                                k = k + 1

        # Create dataFrame with the series created in the loop above
        prices = pd.DataFrame(columns = ["Title", "Price", "Link"])

        bestOffer = pd.DataFrame(columns = ["Title", "Price", "Link"])

        buyNow = pd.DataFrame(columns = ["Title", "Price", "Link"])
       
        if(len(pricesIDs)):       
            prices["Title"]=pricesIDs
            prices["Price"]=pricesPrices
            prices["Link"]=pricesLinks
            prices = prices.sort_values(by="Price")
                
            bestOffer["Title"]=bestOfferIDs
            bestOffer["Price"]=bestOfferPrices
            bestOffer["Link"]=bestOfferLinks
            bestOffer = bestOffer.sort_values(by="Price")
            
            buyNow["Title"]=buyNowIDs
            buyNow["Price"]=buyNowPrices
            buyNow["Link"]=buyNowLinks
            buyNow = buyNow.sort_values(by="Price")
        
        ret = [prices,bestOffer,buyNow]

        return ret