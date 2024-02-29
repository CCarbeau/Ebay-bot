# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from bestOffer import bestOffPrices
from myEmail import email
from analyze import aucTargets
from analyze import buyNowTargets
from analyze import offerTargets

# Time library
from datetime import datetime,timezone,timedelta

# Pandas
import pandas as pd

def main():
    # Permission code from eBay 
    token = "v^1.1#i^1#I^3#r^0#f^0#p^1#t^H4sIAAAAAAAAAOVYb2wURRTvtdeShhY+gIKIpiziB8jt7e7t3t1ueleu1xJKoFd6R4UGxdnd2Xa5u93rzlzbEyGXGiAYiYlGCeGPDRZD8B8SxcQACUbUxIgEjCGHfJCEBAWNMQqB+MHZbSnXSvjXS2zifbnMmzdv3u837817O0y+qnrhlqVbrte6ppQP5pl8ucvFTmWqqyoXTason1NZxhQpuAbzT+XdAxWX6xFIpzJSO0QZ00Cwrj+dMpDkCENU1jIkEyAdSQZIQyRhRYpHViyXOJqRMpaJTcVMUXUtTSFKCSq8JgR8rKjyUFFkIjVu2UyYIQqIjN+vskFBAZBjGD+ZRygLWwyEgYFDFMdwvIfhPJyYYHnJJ0qCSDNMoJOq64AW0k2DqNAMFXbclZy1VpGvd3cVIAQtTIxQ4ZbIkngs0tLU3Jqo9xbZCo/wEMcAZ9HYUdRUYV0HSGXh3bdBjrYUzyoKRIjyhod3GGtUitxy5iHcd6iWgaByok/w+ZUA7wOloXKJaaUBvrsftkRXPZqjKkED6zh3L0YJG/J6qOCRUSsx0dJUZ/+tzIKUrunQClHNjZE1kbY2KhzttnSEdeBBEFhKt6etvckjAwgEgWMFj8D7OV5mfSPbDNsaIXncPlHTUHWbMlTXauJGSHyG45nhipghSjEjZkU0bPtTrOd3GAzSoih22kc6fIZZ3G3YpwrThIY6Z3hv/kdXY2zpchbDUQvjJxyCSNJkMrpKjZ90InEkePpRiOrGOCN5vX19fXSfjzatLi9JMNa7esXyuNIN04BydO1ct/X1ey/w6A4UBZKVSJdwLkN86SeRShwwuqgwHyRkMCO8j3UrPF76L0ERZu/YfChVfgR42e/ngn5VDmq8qpQkP8IjIeq1/YAyyHnSwEpCnEkBBXoUEmfZNLR0VfIJGucLatCj+kXNw4ua5pEF1e9hNQgZCGVZEYP/nzS530CPQ8WCuESRXqIoF3t6+yMs1qzGgNYRTJBa1rnIjAfXR3va25c1xqDXAnyrInDP9HSF7jcX7gg+mtIJMwmyf6kIsHO9NCQsNRGG6oTgxRUzA9vMlK7kJtcB+yy1DVg4F4epFBFMCGQkk2kp1U1dIngPdEk8HOpS1qf/pDbdERWyA3ZyobLXI2IAZHTarj60Yqa9JiBth9fOdSJe53g9Idw66VknFWoCchitrg43m7QDmUa9Cm1BZGYt0mfTMbv7SphJaJBqhi0zlYJWBzvhbE6nsxjIKTjZ0roEAa6DSVZq2QAjcmxAGG2NHg6X4hTSdZPtSirdRexueMCG2jv24z5c5vzYAdfnzIDreLnLxdQzC9j5zLyqilXuipo5SMeQ1oFGI73LIN+sFqSTMJcBulU+o+yPfW8sjc5pjr25cEMid3rXV2U1RW8Lg88ys0dfF6or2KlFTw3M3Nszlez0WbUcz3CcyPI+URA7mfm3Z93so+6ZBW/sW3dN4nHhkceGrkxdxh5y/TDE1I4quVyVZe4BV1nHjJczHfTN8N7jv22UtQWzcGX12t3ne1cORa+eWfzkwI81Bbb94pqeQ/nBRGF378nLH1L5hIgXVRW+bzizddXz1c1BcfN3062ribPv9q/yNpTP/nrr8sXzPooU3E+fkj99v2/j/gOhAy+9dmTtqYo/P9vF7xBfOPhKl6K998lba3dkj28e+v31kwuMOJefHv276uMTxxIF7dzOny+0n19z4YM9N451T7l2bsMTyZlZeK2wYxr/0+qGo1+evfbGXKs28M1foJ7e2bfp8J63X922v7o2eWNa742jz52uPJLce2leofMApXZf37rtsHXx4IkrrTPmblK3b0/unV1980XxnV++YDs3yVd+7dl3afgs/wE+bbV/9REAAA=="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=12)

    aucTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    buyTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    offerTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    
    searches = ["2023 Topps Chrome Anthony-Volpe PSA 10",
                "2023 Topps Chrome Anthony-Volpe auto",
                "2020 Bowman Chrome Anthony-Volpe 1st auto",
                "2023 Topps Chrome Adley-Rutschman PSA 10",
                "2023 Topps Chrome Adley-Rutschman auto",
                "2019 Bowman Chrome Adley-Rutschman 1st auto",
                "2022 Topps Chrome Update Julio-Rodriguez PSA 10",
                "2022 Topps Chrome Update Julio-Rodriguez auto",
                "2022 Topps Chrome Update Bobby-Witt-Jr PSA 10",
                "2022 Topps Chrome Update Bobby-Witt-Jr auto",
                "2023 Bowman Draft Max-Clark 1st auto",
                "2023 Bowman Draft Max-Clark 1st",
                "2020 Bowman Chrome 1st Luisangel-Acuna auto",
                "2022 Bowman Draft Chase-DeLauter 1st auto",
                "2022 Bowman Chrome Jackson-Merrill 1st auto",
                "2021 Bowman Chrome Adael-Amador 1st auto",
                "2021 Bowman Draft Carson-Williams 1st auto",
                "2023 Bowman Draft Colt-Emerson 1st auto",
                "2022 Bowman Chrome Colson-Montgomery 1st auto",
                "2022 Bowman Chrome Curtis-Mead 1st auto",
                "2022 Bowman Draft Jett-Williams 1st auto",
                "2021 Bowman Draft Jordan-Lawlar 1st auto",
                "2022 Bowman Chrome James-Wood 1st auto",
                "2020 Bowman Chrome Jasson-Dominguez 1st auto",
                "2023 Bowman Draft Matt-Shaw 1st auto",
                "2023 Bowman Chrome Roman-Anthony 1st auto",
                "2021 Bowman Chrome Anthony-Mayo 1st auto",
                "2020 Bowman Draft Colt-Keith 1st auto",
                "2019 Bowman Chrome Noelvi-Marte 1st auto",
                "2020 Bowman Draft Pete-Crow-Armstrong 1st auto", 
                "2023 Bowman Chrome Samuel-Basallo 1st auto",
                "2020 Bowman Draft Evan-Carter 1st auto",
                "2023 Bowman Chrome Ethan-Salas 1st auto",
                "2023 Bowman Chrome Junior-Caminero 1st auto",
                "2023 Bowman Draft Wyatt-Langford 1st auto",
                "2023 Bowman Draft Wyatt-Langford 1st",
                "2022 Bowman Chrome Jackson-Chourio 1st auto",
                "2022 Bowman Chrome Jackson-Chourio 1st",
                "2022 Bowman Draft Jackson-Holiday 1st auto"]
    
    emailAddresses = ["cikoticz24@gmail.com"]

    for item in searches:
        prices = currPrice(token, item, condition["Graded"])
        auctions = currAucPrices(token, item, condition["Graded"], (date+timeRange).isoformat()[:23])
        bestOffer = bestOffPrices(token, item, condition["Graded"])
        
        # print(prices)
        # print(auctions)

        # Auction Targets 
        if(len(aucTargets(prices,auctions))!=0):
            aucTargDf = pd.concat([aucTargDf,aucTargets(prices,auctions)])
            aucTargDf = aucTargDf.reset_index(drop=True)

        # Buy Now Targets:
        if(len(buyNowTargets(prices))!=0):
            buyTargDf = pd.concat([buyTargDf,buyNowTargets(prices)])
            buyTargDf = buyTargDf.reset_index(drop=True)

        # Best Offer Targets;
        if (len(offerTargets(prices,bestOffer))!=0):
            offerTargDf = pd.concat([offerTargDf,offerTargets(prices,bestOffer)])
            offerTargDf = offerTargDf.reset_index(drop = True)

    aucTargDf = aucTargDf.sort_values(by="Discount", ascending=False)
    email(emailAddresses,aucTargDf, buyTargDf, offerTargDf)

if __name__ == "__main__":
    main()