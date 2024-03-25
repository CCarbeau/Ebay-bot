import json
import requests 
import pandas as pd
import numpy as np

bannedAutoWords = ["Signed", "signed","SIGNED", "Non", "non", "IP", "Non-Auto","Beckett"]

# Function finds the lowest auction prices of "item" within a certain end data 
def currAucPrices(token,item,condition,date, auto):
     # How many items to search (200 is max)
    count = 100

    # Zip code that the item can ship to
    zipCode = "07960"

    # Date that you want the cards to end before 
    # Must use UTC ISO 8601 format of [yyyy-MM-ddThh:mm:ss.sssZ]
    # .. in front of yyyy means from now up to that date
    date = "[.."+date+"Z]"
    
    # API URL
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+item+"&limit="+str(count)+"&filter=buyingOptions:{AUCTION}&sort=price&filter=conditionIds:{"+condition+"}&filter=deliveryPostalCode:"+zipCode+"&filter=itemEndDate:"+date
    headers = {"Authorization":"Bearer "+token,
                "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
                "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"}
    
    # Make API Get request 
    apiReq = requests.get(url,headers=headers)

    # Parse json file
    parseddoc = apiReq.json()

    # Create series's for each items' title, price, and link
    prices = pd.Series(index = np.arange(count))
    ids = []
    links = []

    # Traverse the JSON document and extract desired data
    i = 0
    try: 
        parseddoc["itemSummaries"]
    except:
        # print("No auctions found for: "+item)
        data = pd.DataFrame(columns = ["Title", "Price", "Link"])
    else: 
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
                            price = float(item["currentBidPrice"]["value"])
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