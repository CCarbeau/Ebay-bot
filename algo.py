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
    token = "v^1.1#i^1#r^0#I^3#p^1#f^0#t^H4sIAAAAAAAAAOVYf2wTVRxvtw4yN5REGEKG1gN16Wj77q7tepe10nVbVoR1rLWyEQPvru+2Y9e77t7rugY1zQIkouEPEX9ElkwSJGBMFBMJQQ1qDP5BFEiIJqiAYhT+IAEU/B3vujG6Sfi1Ji6x/zT3fd/3fZ/P532/7/vuQH5GpWNT26Yrs6wzy0byIF9mtdJVoHJGRf3d5WULKiygyME6kl+ctw2V/9SIYUpJ850IpzUVI/tgSlExXzAGqIyu8hrEMuZVmEKYJyIfC61YzjMuwKd1jWiiplD2SHOA8vgbfDTHMXRDg+DjuKRhVa/GjGsBSmI4AJIs9AmAlSTkMcYxzqCIiglUSYBiAONxAtYJPHHaw7MMD2gXzTDdlD2BdCxrquHiAlSwAJcvzNWLsN4YKsQY6cQIQgUjodZYNBRpbmmPN7qLYgXHdIgRSDJ44lNYSyJ7AioZdONlcMGbj2VEEWFMuYOjK0wMyoeugrkD+KNScwyEAiNJnMhyDBBKImWrpqcguTEO0yInnVLBlUcqkUnuZooaagjrkEjGntqNEJFmu/m3MgMVWZKRHqBamkJdoY4OKhju1WVMZOjECOpir7Ojs9kpQAS9Xob2Or0eH+MRaHZsmdFYYyJPWiesqUnZlAzb2zXShAzMaLIyTJEyhlNUjeohiZh4iv18VxWk/d3mlo7uYYb0quauopQhg73weHP9x2cTostChqDxCJMHCgIFKJhOy0lq8mAhE8eSZxAHqF5C0rzbnc1mXVnWpek9bgYA2r1qxfKY2ItSkCr4mrVu+ss3n+CUC1REZMzEMk9yaQPLoJGpBgC1hwp6/BzHgTHdJ8IKTrb+y1DE2T2xHkpVH14vx4nAC0CD4PdDKJaiPoJjKeo2cSAB5pwpqPchklagiJyikWeZFNLlJM96JYb1S8iZ9HGS08NJklPwJn1OWkIIICQIIuf//5TJrSZ6DIk6IiXK9BJlOdc/MBiiiaQ3NUgJf9zoZd31Wsy/Ltzf2bmsKYrcOvS0i17mif6ewK3WwnXJhxXZUCZurF8qAcxaL40IbRomKDklejFRS6MOTZHF3PTaYFZPdkCd5GJIUQzDlEiG0ulIqU7qEtG7rUPizliXsj/9J73puqywmbDTi5U5HxsBYFp2md3HJWoptwaNa4fbrHXDvKaAekq8ZePOOq1YGyRH2crJ0cumq0DZhQdEl46wltGNe7Yrat6+4lofUo1uRnRNUZCeoKdczalUhkBBQdOtrEuQ4DKcZq2WbgCc18c0MFPbNrHQSNdMtyOpdAex7dHbvFC7J77cBy2FHz1k/RgMWT8ss1pBI3iIXgQenFH+uK28egGWCXLJUHJhuUc13ll15OpDuTSU9bJ7LRd3bGsLL2iJvuRYH88dee2Qpbro28LIk+C+8a8LleV0VdGnBlB7baSCvmfeLMYDWOChPSwD6G6w6Nqoja6xzTl3KbF9a9+Gt3dWtfx9UsoeOrjeuhHMGneyWisstiGrxZcfHibZtW+A03jkGcuX+6hde8TVSzvOPzv/kf7VA/PAJ9ELB9reidR3bZ67dW7d3OMXruxc+HBw43Bvfd3slV2Lv/jxxK8P/FZ7IZQtb3SUvbyW/tlxfGNL58KnlYrda04vc3x66feoY8mJ6m1dR1/Z9f6b+x37Vh35I59PHqh9/vCfNS98f9eGnmHFOpCQvjqx9q9jcfTqc/cLFf5TKOT47Pyciwd/OJyb8/WLl4/OnD/7FAO6pQ++u1xZI35be2SLVV5/jv/84F563f6nathfWts2vwUcS+BZ2/749vieqnT4vXl7Zy+uq4bfvP6utxMl9h07e2aQqdtyspYeWMWyHbt3DHy0NHvmsdG9/Af+sb0W9REAAA=="
    
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