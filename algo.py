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
    token = "v^1.1#i^1#r^0#f^0#p^1#I^3#t^H4sIAAAAAAAAAOVYe2wURRjv9UWwPGLkoeV1XYrBktubfdz1bu2duT5IT/uidxRpJM3s7my77d3usjPX9jAktSpKokhMeCRgRKIQEyEgEBJePiKSQFQUE0UkxNCIYILIH9KYGt17UK6V8OolNvH+uczMN9/8fr/5vvlmB/QVTixbU7vmxmTbhNxtfaAv12ZjisDEwoJFU/JyiwtyQIaBbVtfaV9+f94vFRhGI4bQjLChaxjZe6MRDQvJTh8VMzVBh1jFggajCAtEEkKB+jqBpYFgmDrRJT1C2YPVPorjOEXhIeLc5S5Olt1Wr3bTZ1j3UTwLOdbDeiQkKoooWsMYx1BQwwRqxEexgOUdgHMAJszwAucSeEADwLVS9hZkYlXXLBMaUP4kWiE518yAemekEGNkEssJ5Q8GFocaA8HqmoZwhTPDlz8tQ4hAEsMjW1W6jOwtMBJDd14GJ62FUEySEMaU059aYaRTIXATzAPATyrtFiWvAhiP7JLcHjdyZUXKxboZheTOOBI9quxQkqYC0ohK4ndT1FJD7EQSSbcaLBfBanvib0kMRlRFRaaPqqkMLA80NVH+qg5TxUSFDoygKXU4mpqrHSJE0OViGZfDxbtZXmS49DIpX2mRR61TpWuympAM2xt0UokszGi0MmyGMpZRo9ZoBhSSwJNp5x5WELQmtjS1hzHSoSV2FUUtGezJ5t31H55NiKmKMYKGPYweSArko6BhqDI1ejAZieng6cU+qoMQQ3A6e3p66B6O1s12JwsA43y2vi4kdaAopFK2iVy37NW7T3CoSSoSsmZiVSBxw8LSa0WqBUBrp/y8x+v1grTuI2H5R/f+qyODs3NkPmQrPzgvhG4P5GQvL7pZ2ZON/PCnQ9SZwIFEGHdEodmFiBGBEnJIVpzFoshUZcudwnIeBTlkt1dx8F5FcYgu2e1gFIQAQqKVu57/T5rca6CHkGQikq1Iz06Ue1d29wYYopiV5UqLJ2yVstZFesjTWbWyufnpykbkNCHfILnYZSvbffeaC7clXxVRLWXC1vpZEyCR61kRoVbHBMljoheSdAM16RFVio+vDeZMuQmaJB5CkYjVMSaSAcMIZu2kzg69+zokHox1VuvTf1GbbssKJwJ2fLFKzMeWA2iodKL60JIederQunY4YSLXDbUtiXpMvFXrzjquWFskU2xVOXXZpJOUadwt0SbCesy07tl0Y+L2Fda7kGZVM2LqkQgyW5gxZ3M0GiNQjKDxltZZCHAVjrNSy5QDLwe4cn5svKRkIW0bb0dSFg/ifP/9XaidI7/t/TnJH9Nv+xT0247l2mygAixg5oOSwryl+XmTirFKEK1ChcZqu2Z9s5qI7kJxA6pm7iM517dvqK0qrmncWPZ8OH56y4mcSRlPC9tWgEeHHxcm5jFFGS8NYPatkQJm6szJLA84wDA85+JBK5h/azSfmZE/7cdVTR9cKRm88NDqJZcj5/a5j+50rwWTh41stoKc/H5bTplRsunYk2jhwfU/zFr65o3vAl+d23xp66WCTbv3vP5567uvltV+1O+d0r7s24vHZz9+ZmDXqhnbd8z8Yn/47KkzyrG3zu/YvfDsDv3hgZbKgVnTfvum5zwsrvi+c96kFRuPXDi0tGRT3WNH18fnrBsqbZhzfd5r4fotp4eu+Q/UTs8RDx/dIBVu/vvq4PlDaz/7ue7LPaXvzFmw9+Ifp65+ffInjQ7u+vXtkuiLL2ysr847vMqTO/MJ6Zktc2/sarIteeM66pLaKgamd+7dP/fly+wJu+S/8lxw8K/yTwaPnNUO7F5YtPr9ooPm73/Of++VnVs/fmrC3pdyt3f7aoc+9LYdr9l3aOrQtemL2pevL+0WT6b28h9vG8cK9BEAAA=="
    
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
                "2023 Bowman Draft Max-Clark Chrome 1st",
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
                "2023 Bowman Draft Wyatt-Langford Chrome 1st",
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