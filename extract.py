import json
import requests 

def main():
    item = "2024-Topps"
    url = ("https://api.ebay.com/buy/browse/v1/item_summary/search?q="+item+"&limit=3")
    headers = {"Authorization":"Bearer v^1.1#i^1#I^3#p^1#r^0#f^0#t^H4sIAAAAAAAAAOVYa2wUVRTu9kFTWh4qQdKgLINEhczsndmd3Z0Ju2R328oqfdhdqhQJ3pm90067O7M79y7tCiSlvIwBgxKNbwuKImqCUUATIgnyMGoIBBFRU6KYoCb+0Bj8QVBnpktpK+HVTWzi/tnMueee+33fPeeeOwN6xlXMWb9g/Z8THOXFfT2gp9jhYCtBxbiyuRNLiqvLisAQB0dfz109pb0lP83DMJVMi80Ip3UNI2d3Kqlh0TYGqKyhiTrEKhY1mEJYJLIYC9UvFDkGiGlDJ7qsJylntCZAKV4WsH7Z7WZ5lPAC1rRql2LG9QDl9icEP4dYn+LxQh/wmeMYZ1FUwwRqJEBxgPPQgKNZf5xzix6fyPoYFnCtlLMFGVjVNdOFAVTQhivac40hWK8OFWKMDGIGoYLRUF2sMRStqW2Iz3MNiRXM6xAjkGTx8KeInkDOFpjMoqsvg21vMZaVZYQx5QoOrDA8qBi6BOYm4NtSI06CbIIXfDyrQBlJBZGyTjdSkFwdh2VRE7Riu4pIIyrJXUtRUw2pA8kk/9RghojWOK2/B7MwqSoqMgJUbTi0ONTURAUj7YaKiQppjKAht9NNzTW0BBHkeY7lad7j5TwS684vMxArL/KIdSK6llAtybCzQSdhZGJGI5VxD1HGdGrUGo2QQiw8g35CHLB5BYHgbbW2dGAPs6Rds3YVpUwZnPbjtfUfnE2IoUpZggYjjBywBQpQMJ1WE9TIQTsT88nTjQNUOyFp0eXq6upiutyMbrS5OABY18P1C2NyO0pByva1at3yV689gVZtKjIyZ2JVJLm0iaXbzFQTgNZGBT1+QRBAXvfhsIIjrf8yDOHsGl4PhaoPQeIVHgjQr0iKnxdgIeojmE9Rl4UDSTBHp6DRiUg6aVYgLZt5lk0hQ02Ibl7h3H4F0QmvoNAeQVFoiU94aVZBCCAkSbLg//+UyfUmegzJBiIFyvQCZbmQWd4dYolihH1Kiz9u9rLWuXrM3xHJNDffH25ELgN6GmSeeyjTFrjeWrgi+UhSNZWJm+sXSgCr1gsjwgIdE5QYFb2YrKdRk55U5dzY2mC3kWiCBsnFUDJpGkZFMpRORwt1UheI3g0dEjfHupD96T/pTVdkha2EHVusrPnYDADTKmN1H0bWUy4dmtcOl1XrpnmZjXpUvFXzzjqmWJskB9iqiYHLJmNTZvBymTEQ1rOGec9mGq3bV1zvRJrZzYihJ5PIaGFHXc2pVJZAKYnGWlkXIMFVOMZaLesDfjcAwO0bFS/ZbqTLxtqRVLiDuHT+DV6oXcNf7oNF9o/tdRwAvY6Pix0OMA/MZmeBmeNKFpWWVFVjlSBGhQqD1TbNfGc1ENOJcmmoGsW3Ff2+7ZkFkeraxmfnrIjnjr14pKhqyLeFvqVg2uDXhYoStnLIpwYw/fJIGTvp9gmcB3Csn3N7fKyvFcy6PFrKTi2dEn3g9a1PNbxT/e62+r4dJ3f/yvT77gYTBp0cjrKi0l5HUWXrreW+SH1bx6lvXv5w0/qv/PtKmhrOPDf/xC/bP9jzKC45+sJ95O/NDZmN49fWTzsl1S2JlRqMdnH/BnbaFObg6R+4Za8tajuQ27T/s33vb/p+6/Qn0297jxZXRSbufHwq3zuZLw8v1evHr55N78p8fr5z86vspP4u/VSFlKpcviW4arXnlvMb90zeUvF88TphRfWaVROPwBOHvig7f2/Vkf6lf/y2+yPnJ5lv5dqdZ899+vMr4fdWzNDfdDrWLNx7J3NwMfNEvf8x/q1H6natO3shdZruD2xfefjMpH1rZn634Rh/riNz4aU7Du39qzY8Y8vTh1dWv/Hl/h0njy+Jrr1Yvvr4PZnw8R/Hrzz59cBe/gP0mvfx9REAAA==",
                "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
                "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"}
    apiResult = requests.get(url, headers = headers)
    parseddoc =apiResult.json()
    print(parseddoc)
    # for item in (parseddoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
    #     title = item["title"][0]
    #     condition = item["condition"][0]["conditionDisplayName"][0]
    #     price = item["sellingStatus"][0]["convertedCurrentPrice"][0]["__value__"]
    #     print(title + " " + condition + " " + price)

if __name__=="__main__":
    main()