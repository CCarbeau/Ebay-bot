import json
import requests 
import pandas as pd
import numpy as np

# Function finds the lowest auction prices of "item" within a certain end data 
def currAucPrices(item,condition,date):
     # How many items to search (200 is max)
    count = 200

    # Zip code that the item can ship to
    zipCode = "07960"

    # Date that you want the cards to end before 
    # Must use UTC ISO 8601 format of [yyyy-MM-ddThh:mm:ss.sssZ]
    # .. in front of yyyy means from now up to that date
    date = "[..2024-02-25T10:00:00.000Z]"

    # Permission code from eBay 
    token = "v^1.1#i^1#f^0#I^3#p^1#r^0#t^H4sIAAAAAAAAAOVYa2wUVRTe3W5LsC0QkUcqwTo8jCUzO6/t7ky6C9supMujr11rKVK8O3OnnXZ3Zph7l3bBmFoISkIgmuALYhsSf2gUNVGIjxgCGhEENDE+EmPQECUSiRAN8gNwZrqUbSW8uolN3D+bOffcc7/vu+fcc2fo/pLJVVvrt14sd0/yDPXT/R63mymlJ5cUL5pS5KkodtF5Du6h/vn93oGiMzUIpFOG2AKRoWsIVvalUxoSHWOIyJiaqAOkIlEDaYhELInxyKqVIkvRomHqWJf0FFEZi4YIhWMZGgRkDtBBhpYFy6pdi5nQQwTkYLUElKTAy3yQlhRrHKEMjGkIAw2HCJZmeZJmSZZLsIzIB0WeoViWbycqW6GJVF2zXCiaCDtwRWeumYf15lABQtDEVhAiHIssizdGYtGlDYkaX16scE6HOAY4g0Y/1ekyrGwFqQy8+TLI8RbjGUmCCBG+8PAKo4OKkWtg7gK+I3WS8XNcAIDqoCL4/UKgIFIu0800wDfHYVtUmVQcVxFqWMXZWylqqZHshhLOPTVYIWLRSvuvOQNSqqJCM0QsrY2sjjQ1EeG6LlNFWAUkgsCUusimliiZBBD4/SzjJ/18NcsnGS63zHCsnMhj1qnTNVm1JUOVDTquhRZmOFYZLk8Zy6lRazQjCrbx5PtxIwoy7faWDu9hBndp9q7CtCVDpfN4a/1HZmNsqskMhiMRxg44AoUIYBiqTIwddDIxlzx9KER0YWyIPl9vby/Vy1G62eljaZrxta1aGZe6YBoQjq9d67a/eusJpOpQkaA1E6kizhoWlj4rUy0AWicR5oOCINA53UfDCo+1/suQx9k3uh4KVR98tSAxAVYJsBxgASjIURPOpajPxgGTIEumgdkDsZECEiQlK88yaWiqssj5FZYLKpCUqwWF5AVFIZN+uZpkFAhpCJNJSQj+f8rkdhM9DiUT4gJleoGyXFi/oS/CYMWsDSitwYTVy9oX6fFgd936lpbltY3QZwK+QfKzj67vDN1uLdyQfF1KtZRJWOsXSgC71gsjQr2OMJTHRS8u6QZs0lOqlJ1YG8yZchMwcTYOUynLMC6SEcOIFeqkLhC9Ozok7o51IfvTf9KbbsgK2Qk7sVjZ85EVABgqZXcfStLTPh1Y1w6fXeuWeZ2Dely8VevOOqFYWySH2ary8GWTcihTaINEmRDpGdO6Z1ON9u0rofdAzepm2NRTKWi2MuOu5nQ6g0EyBSdaWRcgwVUwwVotE6CDAZYX2PFtm+Q00nUT7Ugq3EHsXXyHF2rf6Jf7sMv5MQPuQ/SA+2OP203X0AuYefSDJUWPeIvKKpCKIaUChUJqp2a9s5qQ6oFZA6imZ7rrwt5d9XUVSxufr9qUyH65+zNXWd63haG19OyRrwuTi5jSvE8N9JzrI8XM1FnlLE+zLMcyfJBn2ul510e9zEzvfXTz8q+fWCCc3H6psfejBYdnJVd89SZdPuLkdhe7vANul/Ze+a6yCmHKldqOp/VvQud2UFs6zCk1sKTqyYvGrKs+Lbrn84rpqeMrpr1yfPZjC9/pKu3wEDVr3//pVIirGdr/59nX5S+OLNTY7zZeuHpQ3DjY3LbquZ+XfLr5qUDvs614y7ZTz7y7d9eLbTUfnjw8d8Oa+NDpPb92D7r+eujtPyadm/7J7upBc87Llw8cvfjSvcdAzwNDC8/+cmbq+UPMkswWNHPjjuZtxuZjcz0o9laTsM831bukQ0pED52/tO+30AVyTf20Vxu+v3/7SfzDt4tOtK3+AEbr5b+7r9ZvmhE5ff73g48fWH3P0cGyCrpUuvxG4Mri+a9deeHhFXvmHDndsvPHGVXxEzPg/vjwXv4D4LzwVPURAAA="
    
    # API URL
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+item+"&limit="+str(count)+"&filter=buyingOptions:{AUCTION}&sort=price&filter=conditionIds"+condition+"&filter=deliveryPostalCode:"+zipCode+"&filter=itemEndDate:"+date
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