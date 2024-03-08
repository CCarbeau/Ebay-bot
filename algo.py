# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
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
    token = "v^1.1#i^1#I^3#p^1#f^0#r^0#t^H4sIAAAAAAAAAOVYbWwURRju9QMopfijREwD9ViKicW9m927ve4tvQvXD+hhv+wdhRYJzO7Otkv3drc7c7QNRJoaCRLRHwghggYLiBoJpkYjIpAIIgYMaDAhJCIJGvEHJWkMiCHGvWsp10r46iU28f5cZuadd57nmfedd3ZAz6Tcko3VG2/mOyZn7u4BPZkOB5MHciflzJ+elVmYkwFSDBy7e4p7snuzrpZhGNNMoRFh09AxcnbFNB0Lyc4AFbd0wYBYxYIOYwgLRBIiodoagXUBwbQMYkiGRjnDlQFKljmJhQCWenw8EGWP3avf8Rk1AhSUJEVErOgFPuj3I2CPYxxHYR0TqJMAxQLWSwMPDfgo4xNYn8DxLs7HtVDOJmRh1dBtExeggkm4QnKulYL1/lAhxsgithMqGA4titSHwpVVddEyd4qv4LAOEQJJHI9uVRgycjZBLY7uvwxOWguRuCQhjCl3cGiF0U6F0B0wjwE/KbUIGL/i4VmfiHi5lE+LkosMKwbJ/WEkelSZVpKmAtKJSrofJKgthrgGSWS4VWe7CFc6E38vxKGmKiqyAlRVeag51NBABSvaLBUTFdIYQUtqoxsaK2kRIshxLMPRnNfHekXGM7zMkK9hjcesU2HosppQDDvrDFKObMxorDJMijK2Ub1eb4UUksCTasffUZDztyR2dGgL46RNT2wqitkyOJPNB+s/MpsQSxXjBI14GDuQFMjOGdNUZWrsYDIQh2OnCweoNkJMwe3u7Ox0dXpchtXqZgFg3MtrayJSG4pBasg2keu2vfrgCbSapCIheyZWBdJt2li67EC1AeitVNDL+/1+MKz7aFjBsb3/6kjh7B6dDulKD84jAcnPKqVeySP6OC4d+REcDlF3AgcSYTcdg1Y7IqYGJURLdpzFY8hSZcHDKayHVxAt+/wK7fUrCi1yso9mFIQAQqIo+fn/T5o8bKBHkGQhkq5IT0+U+zvWdoUYoljlpUoTH7VLWct8I8KvqehobFxSXo/cFvTWSRy7rKM18LC5cE/yFZpqKxO110+bAIlcT4sI1QYmSB4XvYhkmKjB0FSpe2JtsMeSG6BFuiNI0+yOcZEMmWY4bSd1eug90iHxeKzTWp/+i9p0T1Y4EbATi1ViPrYdQFN1JaqPSzJibgPa1w43TOS6qa5Koh4Xb9W+sk4o1jbJIbaqPHTZdCUpu/BayWUhbMQt+5rtqk/cvqJGO9LtakYsQ9OQ1cSMO5tjsTiBooYmWlqnIcBVOMFKLVMK/H7GPpf4cfGSkoV01UQ7ktJ4EGcHH+1C7R79bR/MSP6YXsdXoNdxNNPhAGVgHjMXzJmUtTQ7a1ohVglyqVBxYbVVtz9ZLeRqR90mVK3MgozBvm3VFYVV9dtL1kW7z+38JmNaytPC7pXgqZHHhdwsJi/lpQHMujuSwzwxM5/1Ag/gGR/r4/gWMPfuaDbzZPaMjjkXT/2xYrBx/cylRQ3bQgeWH16RC/JHjByOnIzsXkfGS839r7Wtz+q77j1VXHbeefX5i+GnYwt3be5vp4/INxf4ll1ZtaOgZ/+HHw/27R8oPq38WPRydZnzzcuzzy148dbZw9Nnf1fTfNAK9ZunF577dMeRnW9Q+77YcfLvy7M6AjP+OnSs9YLzlyt7rrW9+swPk3/etyHk8hSc3bSr+fr7l/Nu75XJ3jVS/7zai/mLS0zq7bfaazfdmrIBFHxwadeNviNflrwztarq830DJ07+vuS29/iZgTmLnz3Rr302WHKwtu78b8fN1T1T2w9pv54Kt5QeqDkzpUhrv9QaXT5w/pOPwj9trr2WtefG6pXHtuTiC7NeObr9ua3C1j+9hd+uO/te5+Tizd+/+3rR11u4tUN7+Q/2XbBa9BEAAA=="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=2)

    aucTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    buyTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    offerTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    
    cards = createCards(condition)
    
    #emailAddresses = ["cikoticz24@gmail.com","dominicpiz2@gmail.com","abby.samson@richmond.edu"]
    emailAddresses = ["cikoticz24@gmail.com"]

    for item in cards:
        prices = currPrice(token, item.name, item.cond, item.auto)
        auctions = currAucPrices(token, item.name, item.cond,(date+timeRange).isoformat()[:23])
        # bestOffer = bestOffPrices(token, item.name, item.cond)
        
        # print(prices)

        # Auction Targets 
        aucs = aucTargets(prices[0],auctions)
        # print("Auction Targets")
        # print(aucs)
        if(len(aucTargDf)==0 and len(aucs)!=0):
            aucTargDf = aucs
        elif(len(aucs!=0)):
            aucTargDf = pd.concat([aucTargDf,aucs])
            aucTargDf = aucTargDf.reset_index(drop=True)

        # Buy Now Targets:
        buyNow = buyNowTargets(prices[2])
        # print("Buy now targets")
        # print(buyNow)
        if(len(buyNow)!=0 and len(buyTargDf)==0):
            buyTargDf = buyNow
        elif(len(buyNow)!=0):
            buyTargDf = pd.concat([buyTargDf,buyNow])
            buyTargDf = buyTargDf.reset_index(drop=True)

        # Best Offer Targets;
        offers = offerTargets(prices[0],prices[1])
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