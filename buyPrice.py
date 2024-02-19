import json
import requests 
import pandas as pd
import numpy as np

def prices():
    item = "Anthony-Volpe"
    count = 10
    url = ("https://api.ebay.com/buy/browse/v1/item_summary/search?q="+item+"&limit="+str(count))
    headers = {"Authorization":"Bearer v^1.1#i^1#I^3#f^0#p^1#r^0#t^H4sIAAAAAAAAAOVYa2wUVRTu9oVNKZWHoi2SZQrRUGb3zuzstDt0F7a7YBfow+5apJHH3Zk77dDZme3cu7QbNC4VeQXjI5Gk8gMUQyTRGP5ANIZXJIiiYjSBKL8MMSYQRCURJQVnpqVsK+HVTWzi/tmdc8899/u+e849dwdkikvmbmrY9GeZY0L+7gzI5DscTCkoKS6qnlSQX1GUB7IcHLszszOFfQW/1GGYUJNCK8JJXcPI2ZtQNSzYRj+VMjRBh1jBggYTCAtEFKLBxmUC6wJC0tCJLuoq5YyE/ZTEsjxAPtkLzR8ewJpW7WbMmO6neK8sorjIczwfZ1lJMscxTqGIhgnUiJ9iAcvRgKUZXwwwgpcRAOfyeNl2ytmGDKzomuniAlTAhivYc40srHeGCjFGBjGDUIFIcHG0ORgJL2qK1bmzYgWGdIgSSFJ45FNIl5CzDaopdOdlsO0tRFOiiDCm3IHBFUYGFYI3wTwAfFtqlvECr8gBPg4ZUeRyI+Vi3UhAcmcclkWRaNl2FZBGFJK+m6KmGvG1SCRDT01miEjYaX09k4KqIivI8FOL6oMrgi0tVCDUaSiYKJDGCBpiJ93SGqbjEEGv1yRNezme5eKMZ2iZwVhDIo9aJ6RrkmJJhp1NOqlHJmY0WhkuSxnTqVlrNoIysfBk+3luKujh2q0tHdzDFOnUrF1FCVMGp/14d/2HZxNiKPEUQcMRRg/YAvkpmEwqEjV60M7EoeTpxX6qk5Ck4Hb39PS4ejwu3ehwswAw7ucal0XFTpSAlO1r1brlr9x9Aq3YVERkzsSKQNJJE0uvmakmAK2DCnC1Pp8PDOk+ElZgtPVfhizO7pH1kKv6YFggixKHeMhwPIQwF/URGEpRt4UDxWGaTkCjC5GkCkVEi2aepRLIUCTB45VZT62MaIn3yTTnk2U67pV4mpERAgjF46Kv9v9TJvea6FEkGojkKNNzlOW+7nW9QYbIRn2N3FYbM3tZe7UerV0b6m5tXVLfjNwG5JpEL7u8u8N/r7VwW/IhVTGViZnr50oAq9ZzI0KDjgmSxkQvKupJ1KKripgeXxvsMaQWaJB0FKmqaRgTyWAyGcnVSZ0jevd1SDwY61z2p/+kN92WFbYSdnyxsuZjMwBMKi6r+7hEPeHWoXntcFu1bppX26jHxFsx76zjirVJcpCtIg1eNl02ZRdeJ7oMhPWUYd6zXc3W7SumdyHN7GbE0FUVGW3MmKs5kUgRGFfReCvrHCS4AsdZq2VqQK0H1HA8NyZeot1IV4+3Iyl3B3Hhgvu8ULtH/rkP5Nkfps9xDPQ5DuU7HKAOzGGqwKzigmcLCyZWYIUglwJlF1Y6NPM/q4FcXSidhIqRPzXv93ffaghVLGreMXd9LH1654m8iVnvFnavBI8Nv10oKWBKs141gBm3RoqY8ullLAdYxgcYLwO4dlB1a7SQebRw2tmQ/rd8dHEgfHLysdQffZUD1cHXQdmwk8NRlFfY58jjP6g/cu3G+iWOVakZFefn8+Sj717uHtgZljPb359Teeb4rCOhrdUb5vdeXDH9qY2fS6DhnYbSPerBq6eiVYert+w5ceyTyCsHKge6du5xr63f3//24x8feujDzXs3XZzw9Mbf5mzAq3/8+Y3+2ZPnHj+5cWnN1UP9L35zsLL2/A/w1Llt+57YVfHmdr5sYlP9uV2rth69kvnpC2aa+rDjkZfQ1OVi+aXqzwpmztswYenXC7TyI40Da/5yf/vpC8FkuP9yl+fCyqKaS1MiF09f/16QDu+40nimdL+sbn2y+MD1ki0rv9y38Ku65/MO36h8daZ6gW7+dUpT+eULvoXXGvLnrXlthn9SlRGueG9b9Ozewb38B3QPOm31EQAA",
                "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
                "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"}
    apiResult = requests.get(url, headers = headers)
    parseddoc =apiResult.json()
    prices = pd.Series(index = np.arange(count))
    ids = [None]*count
    i = 0
    for item in (parseddoc["itemSummaries"]):
        title = item["title"]
        ids[i]=title
        # condition = item["condition"][0]["conditionDisplayName"][0]
        price = item["price"]["value"]
        prices[i] = price
        i = i + 1
    ret = pd.Series(index = ids, data = prices.values)
    print(ret)
    
if __name__ == "__main__":
    prices()
