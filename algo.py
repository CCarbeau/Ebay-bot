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
    token = "v^1.1#i^1#I^3#p^1#f^0#r^0#t^H4sIAAAAAAAAAOVYW2wUVRjutluwFBSjoFCBMihycWbOzM5eZmQ32bbUFnqjuxZpNOTM7Jl26O7MdM5Z2ookpRpEBF4ajIIhBS+E8mDig1xECWrwGiQ2aKrxAR8IxGCURAGNxJnpUraVcOsmNnFfNnPOf/7zfd/5//P/M6B7QtGijVUbL07xTMzv6wbd+R4PVwyKJhQuvrsgf2ZhHsgy8PR1P9zt7Sk4uwTDVNKUGhE2DR2j0s5UUseSOxim0pYuGRBrWNJhCmGJKFIsWlsj8QyQTMsghmIkqdLqijAVkIWQwoXUoBD0yaKs2qP6VZ9xI0xxIV6RgwFR4IIiArxoz2OcRtU6JlAnYYoHvEADHw24OM9LPCcBgeEFfzNV2oQsrBm6bcIAKuLCldy1VhbWG0OFGCOL2E6oSHW0MlYfra5YWhdfwmb5imR0iBFI0njkU7mRQKVNMJlGN94Gu9ZSLK0oCGOKjQztMNKpFL0K5g7gu1KrQEj4QwgFRQXCgAByImWlYaUguTEOZ0RL0KprKiGdaKTrZoraashrkEIyT3W2i+qKUudvRRomNVVDVphaWhZdFW1ooCLlrZaGiQZpjKCltNINjRW0DBH0+3nOT/uFAC/InC+zzZCvjMij9ik39ITmSIZL6wxShmzMaLQyXJYytlG9Xm9FVeLgGbbj4wBcVdAnNjtHOnSGadKqO6eKUrYMpe7jzfUfXk2IpclpgoY9jJ5wBQpT0DS1BDV60o3ETPB04jDVSogpsWxHRwfT4WMMq4XlAeDYp2prYkorSkHKtXVy3bHXbr6A1lwqCrJXYk0iXaaNpdOOVBuA3kJFhJAoiiCj+0hYkdGj/xrI4syOzIdc5QdUuIBf5PxBzo+4QCAX6RHJRCjrwEAy7KJT0GpDxExCBdGKHWbpFLK0hOTzq7wvpCI6ERBVWhBVlZb9iQDNqQgBhGRZEUP/nyy51TiPIcVCJEeBnqMgF9vXdkY5olplQbUpFLdLWfNiIxZaU97e2LisrB6xFhTqFD+/sr0lfKupcF3y5UnNViZu758zAZxcz4kIVQYmKDEmejHFMFGDkdSUrvF1wD4r0QAt0hVDyaQ9MCaSUdOsztVFnSN6t3VJ3BnrXJan/6Q0XZcVdgJ2fLFy1mPbATQ1xqk+jGKkWAPaXQcLnVw3tdUu6jHx1uyWdVyxtkkOsdUSQ70m41Jm8FqFsRA20pbdZjP1TvMVN9qQblczYhnJJLKauDFncyqVJlBOovGW1jkIcA2Os1LLBYHo89mtmjAmXopbSFePtysphxexN3J7/TQ78t0+kuf+uB7PR6DH82G+xwOWgEe4eWDuhIInvQWTZ2KNIEaDKoO1Ft1+ZbUQ04a6TKhZ+fflXdizvap85tL6Vxati3ed3Plp3uSsTwt9z4AHhz8uFBVwxVlfGsBD12YKuXsemMILwAc4nuc5IDSDeddmvdx07/3G0zPa9s5vfXTvpvlH7vq54ErJiS3FYMqwkcdTmOft8eSZW1/Y8CsH5y70sVOf371s4XOHN/TPDq3623/u4NFdvSK7Rf9q3ya2anbFrDdOH/L+EBbOtP04Z5c0bdKxP79/0VxJovTpmq/Pl3jbB955e8eJuoHZ3aEVH+8++oR80eovPnbk+KyDid633t0+57WyC9u59sovL6FLtd8NlqwP7x38/FDsQIuHDPZtPtdfPfBN1baUtfBeUBw8O/H584+ffGzR5uWH1/YzJ3ZcOdC75VTNwG+9nacGL5csrjnfoZftn+Gr0J/9/fVDl2tf/WXj8fe54M7DfwhvLvhrD6g4va5ofcvLZzas/6J7f926OZUfTGyf/tO2qRcn7Vy9/LOVn+xb8O2OS1vfa2yUp720gho6y38AL1nMOfQRAAA="
    
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
        prices = currPrice(token, item.name, item.cond)
        auctions = currAucPrices(token, item.name, item.cond, (date+timeRange).isoformat()[:23])
        bestOffer = bestOffPrices(token, item.name, item.cond)
        
        print("Prices")
        print(prices)

        print("Auctions")
        print(auctions)

        # Auction Targets 
        aucs = aucTargets(prices,auctions)
        print("Auction Targets")
        print(aucs)
        if(len(aucTargDf)==0 and len(aucs)!=0):
            aucTargDf = aucs
        elif(len(aucs!=0)):
            aucTargDf = pd.concat([aucTargDf,aucs])
            aucTargDf = aucTargDf.reset_index(drop=True)

        # Buy Now Targets:
        buyNow = buyNowTargets(prices)
        print("Buy now targets")
        print(buyNow)
        if(len(buyNow)!=0 and len(buyTargDf)==0):
            buyTargDf = buyNow
        elif(len(buyNow)!=0):
            buyTargDf = pd.concat([buyTargDf,buyNow])
            buyTargDf = buyTargDf.reset_index(drop=True)

        # Best Offer Targets;
        offers = offerTargets(prices,bestOffer)
        print("Offer targets")
        print(offers)
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
    
    # email(emailAddresses,aucTargDf, buyTargDf, offerTargDf)

if __name__ == "__main__":
    main()