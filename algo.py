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
    token = "v^1.1#i^1#p^1#r^0#I^3#f^0#t^H4sIAAAAAAAAAOVYbWwURRju9UsLVIIoApF4LJAYYPdmd2/vbpfeJdcW7Fno1d5RsKAwtzfbW7pf3ZlreyjSFFOFgolE/CShIQSiJpBoYoKiBgKRqD9KCAqoifGHYoiJ0kCDkejetZS2Er56iU28P5eZeeed53nmfeedHdBZWrawu6Z7oNx1X2FvJ+gsdLnYyaCstGTRA0WFs0sKwAgDV2/n/M7irqILFRjqmiU1IGyZBkbuDl0zsJTrDFJp25BMiFUsGVBHWCKyFAuvWC5xDJAs2ySmbGqUO1IdpERFkAOKyPsgB1jOKzq9xnWfcTNIsbzo8wcSUAlwHC+zwBnHOI0iBibQIEGKA5yXBjwNhDjHS4IgsSLjEwJNlLsR2Vg1DceEAVQoB1fKzbVHYL01VIgxsonjhApFwsti0XCkemldvMIzwldoSIcYgSSNR7eqzCRyN0ItjW69DM5ZS7G0LCOMKU9ocIXRTqXwdTD3AD8nNUwkOAREv8grfj/y50XJZaatQ3JrGNkeNUkrOVMJGUQlmdsJ6oiR2IBkMtSqc1xEqt3Zv6fSUFMVFdlBamll+OlwfT0VqkrZKiYqpDGCtpyi6xuq6QREUBA4VqAFr4/zJlh+aJlBX0Maj1mnyjSSalYx7K4zSSVyMKOxynhHKOMYRY2oHVZIFs+wnS8O2GEF+absjg5uYZqkjOymIt2RwZ1r3l7/4dmE2GoiTdCwh7EDOYGcjbYsNUmNHcwF4lDsdOAglSLEkjye9vZ2pp1nTLvZwwHAelavWB6TU0iH1KBtNtcde/X2E2g1R0VGzkysSiRjOVg6nEB1ABjNVMgbEEURDOk+GlZobO+/OkZw9oxOh3ylhxMsiowAgMDnl5X85EdoKEQ9WRwoATO0Du0WRCwNyoiWnThL68hWkxIvKBwfUBCd9IkK7RUVhU4ISR/NKggBhBIJWQz8f9LkTgM9hmQbkXxFen6iXGxt6wizRLEr/UpjIO6UsqZFZiywoaq1oeHJyijy2NBbJwvcqtbm4J3mwk3JV2mqo0zcWT9vAmRzPS8i1JiYoOS46MVk00L1pqbKmYm1wbydrIc2ycSQpjkd4yIZtqxI3k7q/NC7q0Pi3ljntT79F7XppqxwNmAnFqvsfOw4gJbKZKsPI5u6x4TOtcMDs7luqetyqMfFW3WurBOKtUNykK2aHLxsMjnKDG6TGRthM20712wmmr19xc0WZDjVjNimpiG7kR13Nut6msCEhiZaWuchwFU4wUot6weiL8CJrDguXnKukK6baEdSHg/i4tDdXag9o7/tQwW5H9vlOga6XJ8VulygAixg54G5pUUri4umzMYqQYwKFQarzYbzyWojpgVlLKjahdMLLu3dVVM1e2n09YXPxTN973xRMGXE00LvM2Dm8ONCWRE7ecRLA3j0xkgJO/WRcs4LeCBwvCCwYhOYd2O0mJ1R/NDFN7+sW7JjlyesJ85rZVuvueMnL4LyYSOXq6SguMtVMOvUty9G3m6e0halpx/9YO3yT9fXnV3/3uZkmJyuTd2/76Pu57t/2SaKMbE/OGAF+kt31pbPj5zPDLSdiJ8wLh85+vWlz797/OGrW1/avrf05RP7xSuJk0+cemVgcc+H/NWab/afXuA3rjRWHDGSPbPOra3d/Nrlrx7b0j/gKvmdubCqr7nMv+T9HfqymtWRau/Onhfgx5V7Nn1S09K39cCcc+yvuw9rB+b07tm2EehzD787rfzwwbo+de/RVwXvmak9p7Y8eAZdS+3bPum3l36aefL4ph+jaw6tfOOvQ9/v6E39/McMEy/UV07bGPh7t7jm7Nymwtr+45uaD+7Z3vrDpGetYtM23lp8rDr95+Be/gOPv+S/9BEAAA=="
    
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