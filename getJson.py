import json
import requests 

def getJSON(token, item, condition, count):

    # Zip code that the item can ship to
    zipCode = "07960"
    
    # API URL
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+item+"&limit="+str(count)+"&filter=buyingOptions:{FIXED_PRICE}&sort=price&filter=conditionIds:{"+condition+"}&filter=deliveryPostalCode:"+zipCode
    headers = {"Authorization":"Bearer "+token,
                "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
                "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"}
    
    # Make API Get request 
    apiReq = requests.get(url,headers=headers)

    # Parse json file
    parseddoc = apiReq.json()

    return parseddoc