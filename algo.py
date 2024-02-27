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
    token = "v^1.1#i^1#r^0#p^1#f^0#I^3#t^H4sIAAAAAAAAAOVYa2wUVRTe3T4ogYKiFmx8bAfUBJjZO7OvmUl3y/aVrkBbumvRGoU7M3faobsz27l3aRsiqdWgRqkGadXwkECCkRCFpFEbBbWYqCQE1EBAg0ElSMIPI38MSqKz01K2lfDqJjZx/2zm3HPP/b7vnnPPnQE9hdMXbqjb8Eexc5prRw/ocTmd7AwwvbBg0aw8V2mBA2Q5OHf0LOjJ7807X45hMpESmxBOGTpG7q5kQseibQxRaVMXDYg1LOowibBIZDEWWb5M5BggpkyDGLKRoNzR6hClcgFeEbzWHwK+AICWVb8SM25Y45DjIfAFWRYIqiJYwxinUVTHBOokRHGA89GAo7lgnA2IwC9yPOMVuBbK3YxMrBm65cIAKmyjFe25ZhbU6yOFGCOTWEGocDRSG2uIRKtr6uPlnqxY4VEZYgSSNB7/VGUoyN0ME2l0/WWw7S3G0rKMMKY84ZEVxgcVI1fA3AZ8W2lJCgYlgfPziAeqLfTklaw1zCQk14eRsWgKrdquItKJRrpvJKglhrQGyWT0qd4KEa12Z/5WpGFCUzVkhqiaysgTkcZGKlzVZmqYaJDGCJpyG93YVE1LEEG/n2P9tN8X4HwS6x1dZiTWqMYT1qkydEXLKIbd9QapRBZmNF4Zv+jPUsZyatAbzIhKMniy/fgrCvJ8S2ZHR7YwTdr0zKaipCWD2368sf5jswkxNSlN0FiEiQO2QCEKplKaQk0ctBNxNHe6cIhqIyQlejydnZ1Mp5cxzFYPBwDreXz5spjchpJWfoz4Zmq9C2s3nkBrNhUZWTOxJpLulIWly0pUC4DeSoV9vCAIYFT38bDCE63/MmRx9owvh1yVhwBVRVagZJWHz8/BYC7qIzyaop4MDiTBbjoJzXZEUgkoI1q28iydRKamiF6/ynl5FdFKQFBpn6CqtORXAjSrIgQQkiRZ4P8/ZXKziR5DsolIzjI9J1kudKztirBENSuDajMftzpZyyIjxq+p6mhqerSyAXlM6KuX/dzKjtbQzdbCNclXJTRLmbi1fu4EyNR6LkSoMzBByqToxWQjhRqNhCZ3T60N9ppKIzRJdwwlEpZhUiQjqVQ0dyd1Tujd0iFxe6xz25/+g950TVY4k7BTi1VmPrYCwJTGZLoPIxtJjwGta4dlytS6tspGPSnemnVlnVKsLZIjbDVl5LLJ2JQZvFZmTISNtGlds5mGzO0rbrQj3epmxDQSCWQ2s5Ou5mQyTaCUQFOtrHOQ4BqcYq2WDQIB+ASB4yfFS7Yb6aqpdiTl8iDOD93Shdoz/tU+7LB/bK9zGPQ6D7qcTlAOHmLng7LCvMfy82aWYo0gRoMqg7VW3XplNRHTjrpTUDNddzku7uyvqyqtaRhYuC7efWzLl46ZWV8WdjwF5o19W5iex87I+tAA7rs6UsDOnlvM+QDHBdkA8HN8C5h/dTSfLcm/G+0+47y8Wdr882Dl9q61Q7tKNt3jAsVjTk5ngSO/1+ko+bP4w8XU9g+2tA+VSccHy/rWx5sfeO6H1aDoc0Eb2s9ViAdW7JtdcX/43MDTH20S/q6rGfrrwpH9Jza+fPz9j6XfAm/vXf3tXtcefQH9e9FnXnHAsfToG96DR7dq0fZfn/365I/nei4OvrAouO7UyjWVy9550vVMXsmR5DTYd2ifd8+uOf0Vi1PbIuvvPfl9Udcrh90nFCcc2PaL98DuSy99EV9yuPzdQ7WvV9y5M/natLcKH/l02EHnec8fO3LmUg0MLsmPXph1dt2D1Z7msq39e8uYeTvVuacvd8z/pu+nOc9vLH0zUst+lz57dngpWc83vvrJVyuLBstf3O/rL7lj64zj+unhh0+9d54SRvbyH3fFyzbzEQAA"
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=8)

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
                "2023 Bowman Chrome Romsn-Anthony 1st auto",
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
    
    emailAddresses = ["cikoticz24@gmail.com", "dominicpiz2@gmail.com","abby.samson@richmond.edu"]

    for item in searches:
        prices = currPrice(token, item, condition["Graded"])
        auctions = currAucPrices(token, item, condition["Graded"], (date+timeRange).isoformat()[:23])
        bestOffer = bestOffPrices(token, item, condition["Graded"])
        
        print(prices)
        print(auctions)

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