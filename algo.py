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
    token = getToken()
    
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