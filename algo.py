# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from bestOffer import bestOffPrices
from myEmail import email
from analyze import aucTargets
from analyze import buyNowTargets
from analyze import offerTargets
from card import createCards
from authTok import getToken

# Time library
from datetime import datetime,timezone,timedelta

# Pandas
import pandas as pd

def main():

    # Permission code from eBay 
    # token = getToken()
    token = "v^1.1#i^1#r^0#f^0#p^1#I^3#t^H4sIAAAAAAAAAOVYb2wURRTvXVuw0vonoNRGzHUpkED2bvb2/u3aO732SnoCbekdVZsgmdubbZfu7S47c7QXjClFEEyM0YB8oIFaSFBiKKjRSIgxGiBIIIrGSDQRNICfIPEDBLTG2W0p10r410ts4n257Js3b97vN+/NezOgd1rZwk2Nm65WOKY7B3pBr9Ph4GaAsmmlix4qdlaVFoE8BcdAb01vSV/x77UYZlRDbEXY0DWMXD0ZVcOiLQwzWVMTdYgVLGowg7BIJDERXbZU9LqBaJg60SVdZVzxWJjx+mUIOcgLaR7yUtBPpdoNm0k9zMgCCMkgBSQhFeRSkkDHMc6iuIYJ1AidD7w+FvAsCCWBV+RDIuDdASHQzrjakIkVXaMqbsBEbHdFe66Z5+vtXYUYI5NQI0wkHl2caI7GYw1NyVpPnq3IKA8JAkkWj/+q19PI1QbVLLr9MtjWFhNZSUIYM57IyArjjYrRG87ch/s21YKPFzhKNPABngOCXBAqF+tmBpLb+2FJlDQr26oi0ohCcndilLKRWo0kMvrVRE3EYy7rb3kWqoqsIDPMNNRFX4y2tDCR+k5TwUSBLEbQlDrZltYYm4II+v1ezs/6fQGvL8Xxo8uM2BolecI69bqWVizKsKtJJ3WI+owmMuPNY4YqNWvNZlQmlj/5er4xBrl2a0tH9jBLOjVrV1GG0uCyP+/M/9hsQkwllSVozMLEAZugMAMNQ0kzEwftSBwNnh4cZjoJMUSPp7u7293Nu3Wzw+MFgPO8sGxpQupEGcjYulauW/rKnSewig1FQnQmVkSSM6gvPTRSqQNaBxPxhQRBAKO8j3crMlH6L0EeZs/4fChUfgS9QV8I8iFJlmQgBdKFyI/IaIh6LD9QCubYDDS7EDFUKCFWonGWzSBTSYu8X/byIRmx6YAgsz5BltmUPx1gORkhgFCKHn2h/0+a3G2gJ5BkIlKgSC9QlAtr1vZEOSKbdUG5LZSktax9kZ4Ira5f09r6XF0z8pjQ1yT5vc+v6QjfbS7cEny9qlBmknT9QhFg5XphSGjUMUHpScFLSLqBWnRVkXJTa4N5M90CTZJLIFWlgkmBjBpGvFAndYHg3dMhcX+oC1mf/pPadEtU2ArYqYXKmo+pAWgobqv6uCU949EhbTs8Vq5T8Srb60nhVmjPOqVQU5AjaJX0SLPptiG78VrJbSKsZ03aZ7ubre4rqXchjVYzYuqqisw2btLZnMlkCUypaKqldQECXIFTrNRyQSCEAn5faHLHkWQX0lVT7Ugq3EFc8sw9NtSe8Zf7SJH94/ocX4I+x+dOhwPUgnncXFA9rXhFSXF5FVYIcitQdmOlQ6N3VhO5u1DOgIrpnFn0x+C2xvqqhuZ3Fq5L5r7ZcayoPO9tYWAlqBx7XSgr5mbkPTWAJ2+OlHIPz67w0psrCAHaKAO+Hcy9OVrCPV4ya9+hos1z9l+8VP7IR87k+Uvdr1/r8YGKMSWHo7SopM9RlHspXLwnNvzB/t9i9TVPH+haUjnfX7H+xKOnwd8HHgvOf7VjxtWZFTsuH+kfvjAvUJvcX/frm0vf+vTY5kPxjT8gZlfl9rMRdZu6O2l8uJbLfNu/YYteXTL05zYut/HMuy1fhw+Wf7ar5vCPw9tP97v2fhE09l0/ezLhWXLk+iflT7iOn9kweO3KiiFl+4KjsQs7L/c69aG935dXX3G9N3RgbkP1ypoH8YKhwcZTT52bvmXdrKO9m5cPd4izT/50PhlZ99pJrmzP4fcPvhF2bHG+9vYv38UEdl//4MVnM1urxa/A0Z/nnKheWFp5rsq1y3dqN975wFXmDD/4VzJYVbd+5tZXQvj4wJyXUx+P7OU/yh0WnvURAAA="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=1)

    aucTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    buyTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    offerTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    
    cards = createCards(condition)
    
    #emailAddresses = ["cikoticz24@gmail.com","dominicpiz2@gmail.com","abby.samson@richmond.edu"]
    emailAddresses = ["cikoticz24@gmail.com"]

    for item in cards:
        prices = currPrice(token, item.name, item.cond, item.auto)
        auctions = currAucPrices(token, item.name, item.cond,(date+timeRange).isoformat()[:23])
        bestOffer = bestOffPrices(token, item.name, item.cond)
        # print(prices)

        # Auction Targets 
        aucs = aucTargets(prices,auctions)
        # print("Auction Targets")
        # print(aucs)
        if(len(aucTargDf)==0 and len(aucs)!=0):
            aucTargDf = aucs
        elif(len(aucs!=0)):
            aucTargDf = pd.concat([aucTargDf,aucs])
            aucTargDf = aucTargDf.reset_index(drop=True)

        # Buy Now Targets:
        buyNow = buyNowTargets(prices)
        # print("Buy now targets")
        # print(buyNow)
        if(len(buyNow)!=0 and len(buyTargDf)==0):
            buyTargDf = buyNow
        elif(len(buyNow)!=0):
            buyTargDf = pd.concat([buyTargDf,buyNow])
            buyTargDf = buyTargDf.reset_index(drop=True)

        # Best Offer Targets;
        offers = offerTargets(prices,bestOffer)
        # print("Offer targets")
        # print(offers)
        if (len(offers)!=0 and len(offerTargDf)==0):
            offerTargDf = offers
        elif(len(offers)!=0):
            offerTargDf = pd.concat([offerTargDf,offers])
            offerTargDf = offerTargDf.reset_index(drop = True)

    aucTargDf = aucTargDf.sort_values(by="Discount", ascending=False)
    aucTargDf = aucTargDf.reset_index(drop=True)

    buyTargDf = buyTargDf.sort_values(by="Discount", ascending=False)
    buyTargDf = buyTargDf.reset_index(drop=True)

    offerTargDf = offerTargDf.sort_values(by="Discount", ascending=False)
    offerTargDf = offerTargDf.reset_index(drop = True)
    
    email(emailAddresses,aucTargDf, buyTargDf, offerTargDf)

if __name__ == "__main__":
    main()