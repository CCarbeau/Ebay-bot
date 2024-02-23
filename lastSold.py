import json
import requests 
import pandas as pd
import numpy as np

def soldPrice():
    # NEED TO FIX LAST SOLD DATE INPUT
    item = "2023-topps-chrome-anthony-volpe"
    count = 10
    date = "[2024-01-30T00:00:00Z..2024-02-17T00:00:00Z]"
    token = "v^1.1#i^1#f^0#r^0#I^3#p^1#t^H4sIAAAAAAAAAOVYa2gUVxTO5lW20QQf2BICXUeFatjZO6/s7uiubhJDVmMSs2nU0CJ3Zu4kY3ZnJnPvmg1V2KatSilILFWLFe0DtFTFH1KJ1VoCbaFo2wilUNrSH/1hsUiNbS22QmcmMW5S8ZWFBrp/ljn33HO/77vn3HNnQLbUu2xH444bsz2PFR7Ogmyhx8OUAW9pSXV5UWFlSQHIcfAczi7OFg8UXV6BYSppim0Im4aOkS+TSupYdI0RKm3pogGxhkUdphAWiSwmYuuaRJYGomkZxJCNJOWL10coTmXZUI2icDIjsDWSZFv12zHbjQglSQrgpaDEAFkOsWHGHsc4jeI6JlAnEYoFLO8HrJ/l2pmQyAsiD+hgiO2kfB3Iwpqh2y40oKIuXNGda+VgvTdUiDGyiB2EisZjDYmWWLx+dXP7ikBOrOi4DgkCSRpPfqozFOTrgMk0uvcy2PUWE2lZRhhTgejYCpODirHbYB4Bviu1JKuMCgSek7kgh0JcXqRsMKwUJPfG4Vg0xa+6riLSiUb676eorYa0Bclk/KnZDhGv9zl/69MwqakasiLU6trYplhrKxWt67Y0TDToxwhacre/ta3eL0EEBYFlBL/A17C8xHDjy4zFGhd5yjp1hq5ojmTY12yQWmRjRlOV4XKUsZ1a9BYrphIHT44fC24rGAx3Ols6todp0q07u4pStgw+9/H++k/MJsTSpDRBExGmDrgCRShomppCTR10M3E8eTI4QnUTYoqBQF9fH93H0YbVFWABYAIb1zUl5G6UgpTr69S646/df4Jfc6nIyJ6JNZH0mzaWjJ2pNgC9i4ryoXA4DMZ1nwwrOtX6L0MO58DkeshXfQQhCMlAgILMh2EwKOSjPqLjKRpwcCAJ9vtT0OpBxExCGfllO8/SKWRpip1UKsuFVORXasKqnw+rql8SlBo/oyIEEJIkORz6/5TJgyZ6AskWInnK9Dxlebh3aybGENWqDaodoXa7l3VWG4nQlrretrY1tS0oYEG+WRbYDb1dkQethbuSr0tqtjLt9vr5EsCp9fyI0GhggpRp0UvIholajaQm98+sDeYspRVapD+BkknbMC2SMdOM5+ukzhO9hzokHo11PvvTf9Kb7soKOwk7s1g587EdAJoa7XQfWjZSAQPa146AU+u2ebOLelq8NfvOOqNY2yTH2GrK2GWTdinTeKtMWwgbacu+Z9Mtzu2r3ehBut3NiGUkk8jqYKZdzalUmkApiWZaWechwTU4w1otEwShIMOF+enxkt1GunmmHUn5O4iLVz7khTow+eU+WuD+mAHPMBjwfFTo8YAVYAmzCCwsLXqmuGhWJdYIojWo0ljr0u13VgvRPajfhJpVOK9g9O3XG+sqV7fsXfZ8e/9XBz4rmJXzbeHwc+DJia8L3iKmLOdTA6i6M1LCVDwxm+UBy3JMiBd40AkW3RktZhYUzz81IPx1cGlt1Q8/Xt3w6Z9HB6t6tnaC2RNOHk9JQfGAp0DqHL14s6zk3bWZ3kPXRy81VJ9+def3v4+81Xw8dWZO+RL5b29mJLNxd8VLRz7Zd/HL6jcPvFe3yXttePnXxz43y4dOPv5xJHGeWtx86rX43Mvf7hR/WVh5Zv/8VdTgCSXe0J2qLN/4imfVhdPbjm+rOLLg/RtzSt8ZGdr+7CH51rzdzTd/unLTS323J2Ce+6bq6VtrF7dere04JWX3LOee+jCxa822F07uOnhm4bDZVj0QiQ1eTJ6tX/JF7QnhZ++xpuj2+kObmzYouE/K/mbNu7L+156Xz41cOaEPnx8KDf3xYlVZ+VJw7foH5Sx9qfHGXN+Rwa4FJZTKVKyEb+y/sFfIHA2cBefWlY6O7eU/Fm54oPURAAA="
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+item+"&limit="+str(count)+"&filter=buyingOptions:{FIXED_PRICE}&sort=price"
    headers = {"Authorization":"Bearer "+token,
                "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
                "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>",
                "X-EBAY-C-ENDUSERCTX": "contextualLocation=country%3DUS%2Czip%3D19406"}
    apiReq = requests.get(url,headers=headers)
    parseddoc = apiReq.json()
    print(parseddoc)
    prices = pd.Series(index = np.arange(count))
    ids = [None]*count
    i = 0
    for item in (parseddoc["itemSummaries"]):
        title = item["title"]
        ids[i]=title
        # condition = item["condition"][0]["conditionDisplayName"][0]
        print(item)
        price = item["price"]["value"]
        prices[i] = float(price)
        i = i + 1
    ret = pd.Series(index = ids, data = prices.values)
    print(ret)
    # return ret

if __name__ == "__main__":
    soldPrice()