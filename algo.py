# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from bestOffer import bestOffPrices
from myEmail import email
from analyze import aucTargets
from analyze import buyNowTargets
from analyze import offerTargets
from card import card

# Time library
from datetime import datetime,timezone,timedelta

# Pandas
import pandas as pd

def main():
    # Permission code from eBay 
    token = "v^1.1#i^1#r^0#f^0#I^3#p^1#t^H4sIAAAAAAAAAOVYe2wURRi/R1skgJRAgKDRYxFDaHZvH/fatXfmem3TIu21vbPSguLc7my79G53b2eO9gKGWgWjESIGjAJNGnwkRiWKRvhLTBMgkEiAaLQiRENMjbziE9BA3HtQrpXw6iU28f65zMw33/x+v/m++WaH7i2bvHhD3YaL06yTbAO9dK/NamWm0JPLSivutdvmlVroAgPrQO9DvSV99p8qEUjEdaEFIl1TEXT0JOIqErKdfiJlqIIGkIIEFSQgErAoRIINSwWWogXd0LAmanHCUV/tJwAvcSIAbtbjZVnAxcxe9ZrPqOYnGG/MQ/NMzB1zQRZ6oTmOUArWqwgDFfsJlmZdJM2RNBNlPALHCxxH8SzfTjhaoYEUTTVNKJoIZOEK2blGAdabQwUIQQObTohAfbA2Eg7WV9c0RiudBb4CeR0iGOAUGt0KaRJ0tIJ4Ct58GZS1FiIpUYQIEc5AboXRToXgNTB3AT8rNcO5Icv6XLQEPC43VxQlazUjAfDNYWR6FImUs6YCVLGC07cS1BQjtgqKON9qNF3UVzsyf80pEFdkBRp+oqYq2BZsaiICoU5DQVgBJILAEDvJppZqMgYgcLtZxk26XR7WFWO4/DI5X3mNx6wT0lRJySiGHI0aroImZjhWGbZAGdMorIaNoIwzeArtfCMKutozO5rbwhTuVDObChOmDI5s89b6j8zG2FBiKQxHPIwdyApk5pSuKxIxdjAbiPnY6UF+ohNjXXA6u7u7qW6O0owOJ0vTjHNZw9KI2AkTgMjZZnLdtFduPYFUslREM0dNewGndRNLjxmoJgC1gwi4fDzP03ndR8MKjO39V0cBZ+fodChWekBG9kogRsuy6PPwnLsY+RHIh6gzgwPGQJpMAKMLYj0OREiKZpylEtBQJIFzyyznkyEpeXiZdPGyTMbckodkZAhpCGMxkff9f9LkdgM9AkUD4mJFenGinE+u7gkyWDaqvHKrL2qWsvYKLeJbFUq2tCypCkOnAVyNopt9Itnhv91cuCH5UFwxlYma6xdNgEyuF0WEOg1hKI2LXkTUdNikxRUxPbE2mDOkJmDgdATG42bHuEgGdb2+aCd1cejd0SFxd6yLWp/+i9p0Q1YoE7ATi1VmPjIdAF2hMtWHErWEUwPmtcMJMrmuKyuzqMfFWzGvrBOKtUkyx1aRcpdNKkuZQqtFyoBISxnmNZsKZ25fUa0LqmY1w4YWj0OjlRl3NicSKQxicTjR0roIAa6ACVZqGS/NcwzDeMd3HInZQrpyoh1JRTyISwJ3dqF2jv62D1iyP6bPOkj3WT+zWa10Jb2QWUDPL7M/XmKfOg8pGFIKkCmkdKjmJ6sBqS6Y1oFi2GZaft25tS40ryb82uI10fTR7QctUwueFgaepOeOPC5MtjNTCl4a6Puvj5Qy0+dMY100RzOMh+M5rp1ecH20hJldMis0sGh5+dsamfS9W/P9ZVfyr7d+mENPGzGyWkstJX1WS/X86S987dXKhkqbjwzV7UDfbInMkLZ9Onxm7+xzay+X9w2G9mzd8c7ZvfLVe75csWL7mi1Dw3V/nGE1+4JHv33OdgJjz6Xff3GeX3nMuXid9av1p/WZYO7aR76wzy5Pvvr5y/sG26izB9o2Ve4+v3H5wPDw9p3EgX7P8fSFmT9u+2TRHOFoedW+VQuDM9xbjszyPVB57PSyCs+S49p9r/zG7evXrr5eKbzXcPlFcEla6D7sv7juZ9uaGc37h2o3G/tPDh660tT/0pvPH06+v/+xN4JTvut/9sPahxtauz6q2OQKf7xr/TMVm1f8fbD6wQ+eOndqUDr554W2Y/FJp3ad2OOff+XMIcGyu7n14tMnc3v5Dy650yL0EQAA"
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=1)

    aucTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    buyTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    offerTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    
    searches = [card("2023 Topps Chrome Anthony-Volpe PSA 10",condition["Graded"]),
                card("2023 Topps Chrome Anthony-Volpe auto", condition["Graded"]),
                card("2020 Bowman Chrome Anthony-Volpe 1st auto", condition["Graded"]),
                card("2023 Topps Chrome Adley-Rutschman PSA 10",condition["Graded"]),
                card("2023 Topps Chrome Adley-Rutschman auto",condition["Graded"]),
                card("2019 Bowman Chrome Adley-Rutschman 1st auto",condition["Graded"]),
                card("2022 Topps Chrome Update Julio-Rodriguez PSA 10",condition["Graded"]),
                card("2022 Topps Chrome Update Julio-Rodriguez auto",condition["Graded"]),
                card("2022 Topps Chrome Update Bobby-Witt-Jr PSA 10",condition["Graded"]),
                card("2022 Topps Chrome Update Bobby-Witt-Jr auto",condition["Graded"]),
                card("2023 Bowman Draft Max-Clark 1st auto",condition["Graded"]),
                card("2023 Bowman Draft Max-Clark Chrome 1st",condition["Graded"]),
                card("2020 Bowman Chrome 1st Luisangel-Acuna auto",condition["Graded"]),
                card("2022 Bowman Draft Chase-DeLauter 1st auto",condition["Graded"]),
                card("2022 Bowman Chrome Jackson-Merrill 1st auto",condition["Graded"]),
                card("2021 Bowman Chrome Adael-Amador 1st auto",condition["Graded"]),
                card("2021 Bowman Draft Carson-Williams 1st auto",condition["Graded"]),
                card("2023 Bowman Draft Colt-Emerson 1st auto",condition["Graded"]),
                card("2022 Bowman Chrome Colson-Montgomery 1st auto",condition["Graded"]),
                card("2022 Bowman Chrome Curtis-Mead 1st auto",condition["Graded"]),
                card("2022 Bowman Draft Jett-Williams 1st auto",condition["Graded"]),
                card("2021 Bowman Draft Jordan-Lawlar 1st auto",condition["Graded"]),
                card("2022 Bowman Chrome James-Wood 1st auto",condition["Graded"]),
                card("2020 Bowman Chrome Jasson-Dominguez 1st auto",condition["Graded"]),
                card("2023 Bowman Draft Matt-Shaw 1st auto",condition["Graded"]),
                card("2023 Bowman Chrome Roman-Anthony 1st auto",condition["Graded"]),
                card("2021 Bowman Chrome Anthony-Mayo 1st auto",condition["Graded"]),
                card("2020 Bowman Draft Colt-Keith 1st auto",condition["Graded"]),
                card("2019 Bowman Chrome Noelvi-Marte 1st auto",condition["Graded"]),
                card("2020 Bowman Draft Pete-Crow-Armstrong 1st auto",condition["Graded"]), 
                card("2023 Bowman Chrome Samuel-Basallo 1st auto",condition["Graded"]),
                card("2020 Bowman Draft Evan-Carter 1st auto",condition["Graded"]),
                card("2023 Bowman Chrome Ethan-Salas 1st auto",condition["Graded"]),
                card("2023 Bowman Chrome Junior-Caminero 1st auto",condition["Graded"]),
                card("2023 Bowman Draft Wyatt-Langford 1st auto",condition["Graded"]),
                card("2023 Bowman Draft Wyatt-Langford Chrome 1st",condition["Graded"]),
                card("2022 Bowman Chrome Jackson-Chourio 1st auto",condition["Graded"]),
                card("2022 Bowman Chrome Jackson-Chourio 1st",condition["Graded"]),
                card("2022 Bowman Draft Jackson-Holiday 1st auto",condition["Graded"])]
    
    emailAddresses = ["cikoticz24@gmail.com"]

    for item in searches:
        prices = currPrice(token, item.name, item.cond)
        auctions = currAucPrices(token, item.name, item.cond, (date+timeRange).isoformat()[:23])
        bestOffer = bestOffPrices(token, item.name, item.cond)
        
        # print(prices)
        # print(auctions)

        # Auction Targets 
        aucs = aucTargets(prices,auctions)
        if(len(aucTargDf)==0 and len(aucs)!=0):
            aucTargDf = aucs
        elif(len(aucs!=0)):
            aucTargDf = pd.concat([aucTargDf,aucs])
            aucTargDf = aucTargDf.reset_index(drop=True)

        # Buy Now Targets:
        buyNow = buyNowTargets(prices)
        if(len(buyNow)!=0 and len(buyTargDf)==0):
            buyTargDf = buyNow
        elif(len(buyNow)!=0):
            buyTargDf = pd.concat([buyTargDf,buyNow])
            buyTargDf = buyTargDf.reset_index(drop=True)

        # Best Offer Targets;
        offers = offerTargets(prices,bestOffer)
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