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
    token = "v^1.1#i^1#I^3#p^1#f^0#r^0#t^H4sIAAAAAAAAAOVYXWwUVRTu9oeKpYJC0DQq64Ai4Ozcmdmf2aGdsP0Bami3dJeCjVLuzt5pp92dmc69S7tBYlNCg4EHqwIxGGgwSoLhBY0+oJiAWJSABEUThSce/EG0BUXjg3p3t5RtJfx1E5u4D7uZe8899/u+e849Zwf0TJm6sG953++ljuL8gR7Qk+9w8CVg6pSiRfcV5JcV5YEsA8dAz7yewt6C78sxjMcsuRFhyzQwcnbHYwaW04MVTMI2ZBNiHcsGjCMsE1UOBepWyIILyJZtElM1Y4yztrqC8QtevyR6vVLUDzSI6KBxzWXYrGAgkiJIE9WoD/qRBAQ6j3EC1RqYQINUMAIQ3CwQWeALC0AWfLLocXkksZlxNiEb66ZBTVyAUdJo5fRaOwvqzZFCjJFNqBNGqQ0sDQUDtdU19eFyLsuXMiJDiECSwGOfqswocjbBWALdfBuctpZDCVVFGDOcktlhrFM5cA3MXcBPKy1qPkkU+Yg3qkq8IEk5kXKpacchuTmO1IgeZbW0qYwMopPkrRSlakTakUpGnuqpi9pqZ+pnZQLGdE1HdgVTUxl4JtDQwChVbbaOiQ5ZjKCttrENjdVsBCLo8Qi8h/W4vYI7wosj22R8jYg8bp8q04jqKcmws94klYhiRuOV4bOUoUZBI2gHNJLCk20nXFPQJzWnjjRzhgnSZqROFcWpDM704631H11NiK1HEgSNehg/kRaIJo1l6VFm/GQ6EkeCpxtXMG2EWDLHdXV1ubpEl2m3cgIAPLembkVIbUNxyGRsU7lO7fVbL2D1NBWVJjG1l0nSoli6aaRSAEYro7glv98PRnQfC0sZP/qvgSzO3Nh8yFV+CCAqQQ8veEQA6FckF/mhjIQol8KBIjDJxqHdgYgVgypiVRpniTiy9Sj1pQmipCE26vVrrNuvaWzEE/WyvIYQQCgSUf3S/ydNbjfQQ0i1EclVpOcmyv2d67sDPNHsSp/WJIVpLWteZIak9qrOxsanK4OIs6G7XvUIqztbK243F25IviqmU2XCdP+cCZDK9ZyIsNzEBEUnRC+kmhZqMGO6mpxcByza0QZok2QIxWJ0YEIkA5ZVm7ObOjf07uiSuDvWOa1P/0VtuiErnArYycUqtR5TB9DSXanq41LNOGdC2nZwMJXrlt6SRj0h3jrtWScVa0oyw1aPZppNV5qyC69XXTbCZsKmfbYrmOq+wmYHMmg1I7YZiyG7iZ9wNsfjCQIjMTTZ0joHAa7DSVZqeR/wS25R8HgmxEtNF9KWyXYl5fAiLlTurKHmxv63V/LSH77XcQT0Og7nOxygHDzOzwWPTSlYVVgwrQzrBLl0qLmw3mrQ/6w2cnWgpAV1O39m3uW925dXldUEdyzcEE6e3jWYNy3r1cLAc+Ch0ZcLUwv4kqw3DeDh6zNF/PQHSwU3EIGPto8+0dMM5l6fLeRnF8668OJ+dXjeS09UHiQnv954MP+DgXOXQemokcNRlFfY68ib/+3Z83PO+gbbN/Tu2PlYzcy9hXVzfpy77bvtmx29G4/+Vc9Yr1e/tcleEzozdITbOr/28DC+tOXdlev9SaV76GV3KcvNPxM83r2PO1oyvHZte/HnJYtODV98/p5k0YKu3xa/MfvA6VUnXlF+2D20oG/nqeKrHD4xa1/Jur8/XHyl/VmlYH9/NT4351Hl4qYv1/w6Y6j/0wOvRr5BJ+sGL23b0HJsq1jsWxI53rugaHhm3mcFlb+8d+y1XeuUq3saW87/fOH9pw71tfXc+05ZS8m5zj+/uF9tKDqufrT7jxc8Vz9ZHfSernogdqXrp44lnf2PNE9/ckZy4R7tq+rS8LLN5Yf7G4s/PrRl6O3BN5dlzvIf2eFjh/QRAAA="
    
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