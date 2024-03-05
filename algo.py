# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from bestOffer import bestOffPrices
from myEmail import email
from analyze import aucTargets
from analyze import buyNowTargets
from analyze import offerTargets
from card import createCards

# Time library
from datetime import datetime,timezone,timedelta

# Pandas
import pandas as pd

def main():
    # Permission code from eBay 
    token = "v^1.1#i^1#r^0#f^0#I^3#p^1#t^H4sIAAAAAAAAAOVYe2wURRjvtdcawktFXgXNsZVAKLs3++rdLb2Toy1pSV/0jvJKxbnduXbp3u51Z462Cto0ARMCJpKAIfIoaCKIoiFBE40kyB+gxBdBYkxIMAgag5gUEgRj4tz2KNdKePUSm3j/XPabb775/X7zffPNLugpGjNvU/WmG+Ndj+X39YCefJeLHwvGFBWWTijILy7MA1kOrr6eZ3vcvQW/lmOYMJJKE8JJy8TI05UwTKw4xiCTsk3FgljHigkTCCtEVSLhulpF4ICStC1iqZbBeGoqg0wZCiBN9fGS4EMxIAJqNW/HjFp0XPLLAVkUNDEGAz5BpeMYp1CNiQk0SZARgCCxQGSBHAWiwsuKIHF+IK1iPM3IxrplUhcOMCEHruLMtbOw3hsqxBjZhAZhQjXhxZGGcE1lVX203JsVK5TRIUIgSeGhTxWWhjzN0Eihey+DHW8lklJVhDHjDQ2sMDSoEr4N5hHgO1Ij5KMaqj6f6NOAxAs5kXKxZScguTeOtEXX2LjjqiCT6KT7fopSNWJrkUoyT/U0RE2lJ/23NAUNPa4jO8hULQqvDDc2MqGKNlvHRIcsRtBW29jGpko2BhGUZYGXWVkqE6QYL2aWGYiVEXnYOhWWqelpybCn3iKLEMWMhisDspShTg1mgx2OkzSebD85o6AvQP28t/cwRdrM9K6iBJXB4zzeX//B2YTYeixF0GCE4QOOQEEGJpO6xgwfdDIxkzxdOMi0EZJUvN7Ozk6uU+Qsu9UrAMB7V9TVRtQ2lICM45uu9bS/fv8JrO5QURGdiXWFdCcpli6aqRSA2cqEJH8gEAAZ3YfCCg23/suQxdk7tB5yVR8+lS+TJCkWl0UY0ESYi/oIZVLUm8aBYrCbTUC7HZGkAVXEqjTPUglk65oiynFB9McRq5UF4qwUiMfZmKyVsXwcIYBQLKYG/P+fMnnQRI8g1UYkR5meoywPdKzrCvMkbi/yxZv9UdrLVpVaEf/aio6mpiWLGpDXhlK9KgvLO1qDD1oLdyVfYehUmShdP1cCpGs9NyJUW5ggbUT0IqqVRI2Woavdo2uDRVtrhDbpjiDDoIYRkQwnkzW5OqlzRO+hDolHY53L/vSf9Ka7ssLphB1drNLzMQ0AkzqX7j6caiW8FqTXDm+61ql5jYN6RLx1emcdVawpyQG2ujZw2eQcyhxep3I2wlbKpvdsriF9+4pa7cik3YzYlmEgu5kfcTUnEikCYwYabWWdgwTX4ShrtbwPBMqAXxakEfFSnUa6ZrQdSbk7iN3PPeSF2jv05T6U5/z4XtfnoNd1LN/lAuVgNl8CZhUVLHMXjCvGOkGcDuMc1ltN+s5qI64ddSehbudPyuvfv726oriqYce8l6Ld3755Mm9c1reFvhYwbfDrwpgCfmzWpwYw885IIT9x6nhBAiKQgcjTHV8FSu6Muvkp7qfOHblwtLRu95LW9Y3BU7Pe+qPz+PcKGD/o5HIV5rl7XXlP9pWLrg75o5Yf/tyuXZt81b+0elfs9Lab+6L9c9bv37Wxf1/z5GTFdf+EFTvnJ2cfnbvum/z3vtoYv3Ri4qermYL25Yc3XXmc/fEzY9wlfcch/0Vtz/m5vy1sOXS8J8S3XPqgCW+uajj0xtSzZ76YVOUuXbylbXf//t3XZ8iHjx15ed/F/q+l+c0/mx3i9NoF5ZfPlrzzQm1R3Vm3Vrnwu2kHJpJXEmXG2GdaDnCPb/nly3fPbDU+XlaydkbsxOrZxvvT91ifbG7ddmqr/9UnPjyOzp+ZcuPy26c3XDvw/MoNM88Vvzbtrzl51/Ze+Pv3Ywuu3vLA1wNP919p2vviyYPgp+vrp988uvNWO7aWHzw4sJf/APvb9BP1EQAA"
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=2)

    aucTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    buyTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    offerTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    
    cards = createCards(condition)
    
    # emailAddresses = ["cikoticz24@gmail.com","dominicpiz2@gmail.com","abby.samson@richmond.edu"]
    emailAddresses = ["cikoticz24@gmail.com"]

    for item in cards:
        prices = currPrice(token, item.name, item.cond, item.auto)
        auctions = currAucPrices(token, item.name, item.cond,(date+timeRange).isoformat()[:23])
        bestOffer = bestOffPrices(token, item.name, item.cond)

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