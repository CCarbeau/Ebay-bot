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
    token = "v^1.1#i^1#f^0#I^3#r^0#p^1#t^H4sIAAAAAAAAAOVYe2wURRi/a69IpVQDFqQSPBYwCu7e7O1t727pnV5bag/pg95ZoGrq3N7sdeFu97oz10eMpjZSg6KJD0qsjzQkohGjiUowoZYEUfAZ5BG00YT/MPyBkRAFg+jstpRrJbx6iU285HLZb7755vf7zffNN7ege1rh0t6a3j9m2m/KG+gG3Xl2Oz8DFE4rWFacn1daYANZDvaB7sXdjp78X8oxTCXTUiPCaV3DyNmZSmpYsowBJmNokg6xiiUNphCWiCxFQrWrJDcHpLShE13Wk4wzXBVgFAF4vLJPFtx+gRd4hVq1izGjeoARIR8TvQoSYRmKI6+HjmOcQWENE6iRAOMGbg8LBBZ4okCQeF5yezleEJoZZxMysKpr1IUDTNCCK1lzjSysV4YKMUYGoUGYYDhUHakPhatW1EXLXVmxgqM6RAgkGTz+qVKPI2cTTGbQlZfBlrcUycgywphxBUdWGB9UCl0EcwPwLamhEPf6yryC3wNEICJ/TqSs1o0UJFfGYVrUOKtYrhLSiEq6rqYoVSO2Hslk9KmOhghXOc2f1RmYVBUVGQFmRUVoXaihgQlWthoqJipkMYKG3Mo2NFaxMYigKLp5kRU9ZW5PjBdGlxmJNSryhHUqdS2umpJhZ51OKhDFjCYqA7KUoU71Wr0RUoiJJ9tPHFMQNJtbOrKHGdKqmbuKUlQGp/V4df3HZhNiqLEMQWMRJg5YAtGdTqfVODNx0MrE0eTpxAGmlZC05HJ1dHRwHQKnGwmXGwDetbZ2VURuRSnIWL5mrZv+6tUnsKpFRUZ0JlYl0pWmWDppplIAWoIJenx+vx+M6j4eVnCi9V+GLM6u8fWQq/oQ+BgvemSP4uUFL+/mc1EfwdEUdZk4UAx2sSlobEAknYQyYmWaZ5kUMtS4JIiKW/ApiI2X+RXW41cUNibGy1heQQggFIvJft//p0yuNdEjSDYQyVGm5yjL/W3tnSGeKEaFV2nyRWkva16mR3zrK9saG1dW1COXAT11suhe05YIXGstXJZ8ZVKlykTp+rkSwKz13IhQo2OC4pOiF5H1NGrQk6rcNbU2WDDiDdAgXRGUTFLDpEiG0ulwrk7qHNG7rkPixljnsj/9J73psqywmbBTi5U5H9MAMK1yZvfhZD3l0iG9drjMWqfmFgv1pHir9M46pVhTkiNs1fjIZZOzKHO4XeYMhPWMQe/ZXL15+4rqG5BGuxkx9GQSGU38pKs5lcoQGEuiqVbWOUhwFU6xVst7gZ+eSj6fd1K8ZKuRtky1Iyl3B7Hjvuu8ULvG/7kP2qwP32PfC3rsQ3l2OygHS/hFYOG0/Icc+UWlWCWIU6HCYTWh0f+sBuI2oK40VI282bbT27bUVJauqO9b+ni06+Br+21FWe8WBh4Ft4+9XSjM52dkvWoA8y+NFPC3zJ3p9gAB0C/Pu73NYNGlUQc/x3Fb+8POlx7cOUfd/KUYts8/fYZ/xDEDzBxzstsLbI4eu21J9QsLAsFWccF8/yfnnlr+TqZvbfDAUe6u/n72fPk3y2sah97ertUeesX24v7is0rvsdrv1gxKiXzf4ccufL0Tn3r2nqE/N7bp8s09u88VfbD/3tPDB3fNfXd7yYldA7Oq6548O/2Nj+e8zm564M7Q+8MFA8UffrSy/Ez7vCWbew/duq8v8dPAvB+Hnyt4b89g/YLiYzu+f5WDWz7/9Ymvvjh/v6/myOHjhQdO9AX3Hn3r+ZYfaozdhy5Mf2ajUlP69Jufrd34qW324Kzw8F+nzhUdL7mw89uYo3zoOBdN3KHOa06dLMlb2FKu9W/dVP3y7z5tx77+1Xe3/iae3DZYEjyyKyGvW7V4z1xX7d8/b02O7OU/SxJhn/URAAA="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=24)

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