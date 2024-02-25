import pandas as pd
import numpy as np

# Takes in a dataframe of the market prices returned by prices
# Takes in a dataframe of the current auctions prices from auctionSearch
# Returns cards on auction that are underpriced
def aucTargets(marketPrices, auctionPrice):
    deals = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])

    # Calculate the market price of a card (model is subject to change)
    value = 0
    if(len(marketPrices)<5):
        for i in range(len(marketPrices)):
            value = value + marketPrices.iloc[i]["Price"]
        value = value/len(marketPrices)
    else:
        for i in range(5):
            value = value + marketPrices.iloc[i]["Price"]
        value = value/5
    
    ids = []
    price = pd.Series()
    discount = pd.Series()
    links = []
    # Identify underpriced cards
    for i in range(len(auctionPrice)):
        if(auctionPrice.iloc[i]["Price"]<=0.75*value):
            ids.append(auctionPrice.iloc[i]["Title"])
            price[i] = auctionPrice.iloc[i]["Price"]
            discount[i] = ((value - auctionPrice.iloc[i]["Price"])/value)*100
            links.append(auctionPrice.iloc[i]["Link"])

    deals["Title"] = ids
    deals["Price"] = price
    deals["Discount"] = discount
    deals["Link"] = links 
    deals = deals.sort_values(by="Discount", ascending=False)
    
    return deals

# Takes in a dataframe of the market prices returned by prices
# Returns buy now cards that are underpriced
def buyNowTargets(marketPrices):
    deals = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])

    ids = []
    price = pd.Series()
    discount = pd.Series()
    links = []
    if(len(marketPrices)>=2):
        if(marketPrices.iloc[0]["Price"]<=0.75*marketPrices.iloc[1]["Price"]):
            ids.append(marketPrices.iloc[0]["Title"])
            price[0] = marketPrices.iloc[0]["Price"]
            discount[0] = ((marketPrices.iloc[1]["Price"] - marketPrices.iloc[0]["Price"])/marketPrices.iloc[1]["Price"])*100
            links.append(marketPrices.iloc[0]["Link"])
    deals["Title"] = ids
    deals["Price"] = price
    deals["Discount"] = discount
    deals["Link"] = links

    return deals

# Takes in a dataframe of the market prices returned by prices
# Takes in a dataframe of cards that are low priced with offer options
# Returns cards that could be good value offers
def offerTargets(marketPrices, offerPrices):
    deals = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])

    # Calculate the market price of a card (model is subject to change)
    value = 0
    if(len(marketPrices)<5):
        for i in range(len(marketPrices)):
            value = value + marketPrices.iloc[i]["Price"]
        value = value/len(marketPrices)
    else:
        for i in range(5):
            value = value + marketPrices.iloc[i]["Price"]
        value = value/5
    
    ids = []
    price = pd.Series()
    discount = pd.Series()
    links = []
    # Identify underpriced cards
    for i in range(len(offerPrices)):
        if(offerPrices.iloc[i]["Price"]<=0.9*value):
            ids.append(offerPrices.iloc[i]["Title"])
            price[i] = offerPrices.iloc[i]["Price"]
            discount[i] = ((value - offerPrices.iloc[i]["Price"])/value)*100
            links.append(offerPrices.iloc[i]["Link"])

    deals["Title"] = ids
    deals["Price"] = price
    deals["Discount"] = discount
    deals["Link"] = links 
    deals = deals.sort_values(by="Discount", ascending=False)
    
    return deals

# if __name__ == "__main__":
#     marketPrice = pd.DataFrame(columns = ["Title", "Price","Link"])
#     marketPrice["Title"]=pd.Series(data=["Anthony Volpe Bowman Chrome 1st", "Anthony Volpe Bowman Chrome 1st"])
#     marketPrice["Price"]=pd.Series(data=[100,150])
#     marketPrice["Link"]=pd.Series(data=["https://www.ebay.com/itm/264963280910?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D260885%26meid%3D3df643734d2e423594572ef6ba8f43af%26pid%3D101875%26rk%3D2%26rkt%3D12%26sd%3D196250216985%26itm%3D264963280910%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedV3MskuWithLambda85KnnRecallV1V2V4ItemNrtInQueryAndCassiniVisualRankerAndBertRecallWithVMEV3CPCAutoWithCassiniEmbRecallManual&_trksid=p4429486.c101875.m1851&itmprp=cksum%3A2649632809103df643734d2e423594572ef6ba8f43af%7Cenc%3AAQAIAAABQKAO6YGL7I8ZT6VFWcHmDuKm898HGH9cNRsnG%252Fep%252BzC3UPHwPSmfpPq3b41cHxht%252FCiwo5DdbtiFsRNqRhAUlK8x2MLrmISu5pnzSn%252FhiW3P7y%252BKcxGllTjL%252BG3bIP4k8fGgzCrVY1dxXbjuBFp3vefxTYgjBXBRUWQBgGciI%252FuQ5Mjsfl%252B%252FiL4cv70dT88jK1pljjSZyaCIIbAW6GYGqwxdGKs4tc%252BjbPOi6oqX393QDbrxGSAbe61t2Q6vT4EDLkQFzUtAWP8shAv5WRmJrn9%252Bbp5m5DNz%252Bfz4w7b21nuEMc3tNTWr%252BZnaTgO16A1mzQ%252BCeYgin1ezKvkbSOT1IbNr3FJ%252FuUn2FPF%252BCuAuI2nuf%252F36%252BG%252BXObkJLy5ljPvNyqnOy4CGg1cNn1GMMENn30D7%252F6yvCMAV1obaSXievLNR%7Campid%3APLP_CLK%7Cclp%3A4429486&itmmeta=01HQE758NAR1Q9QK8QA5XHEAEN","https://www.ebay.com/itm/264963280910?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D260885%26meid%3D3df643734d2e423594572ef6ba8f43af%26pid%3D101875%26rk%3D2%26rkt%3D12%26sd%3D196250216985%26itm%3D264963280910%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedV3MskuWithLambda85KnnRecallV1V2V4ItemNrtInQueryAndCassiniVisualRankerAndBertRecallWithVMEV3CPCAutoWithCassiniEmbRecallManual&_trksid=p4429486.c101875.m1851&itmprp=cksum%3A2649632809103df643734d2e423594572ef6ba8f43af%7Cenc%3AAQAIAAABQKAO6YGL7I8ZT6VFWcHmDuKm898HGH9cNRsnG%252Fep%252BzC3UPHwPSmfpPq3b41cHxht%252FCiwo5DdbtiFsRNqRhAUlK8x2MLrmISu5pnzSn%252FhiW3P7y%252BKcxGllTjL%252BG3bIP4k8fGgzCrVY1dxXbjuBFp3vefxTYgjBXBRUWQBgGciI%252FuQ5Mjsfl%252B%252FiL4cv70dT88jK1pljjSZyaCIIbAW6GYGqwxdGKs4tc%252BjbPOi6oqX393QDbrxGSAbe61t2Q6vT4EDLkQFzUtAWP8shAv5WRmJrn9%252Bbp5m5DNz%252Bfz4w7b21nuEMc3tNTWr%252BZnaTgO16A1mzQ%252BCeYgin1ezKvkbSOT1IbNr3FJ%252FuUn2FPF%252BCuAuI2nuf%252F36%252BG%252BXObkJLy5ljPvNyqnOy4CGg1cNn1GMMENn30D7%252F6yvCMAV1obaSXievLNR%7Campid%3APLP_CLK%7Cclp%3A4429486&itmmeta=01HQE758NAR1Q9QK8QA5XHEAEN"])
#     auctionPrice = pd.DataFrame(columns = ["Title", "Price","Link"])
#     auctionPrice["Title"]=pd.Series(data=["Anthony Volpe Bowman Chrome 1st"])
#     auctionPrice["Price"]=pd.Series(data=[60])
#     auctionPrice["Link"]=pd.Series(data=["https://www.ebay.com/itm/264963280910?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D260885%26meid%3D3df643734d2e423594572ef6ba8f43af%26pid%3D101875%26rk%3D2%26rkt%3D12%26sd%3D196250216985%26itm%3D264963280910%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedV3MskuWithLambda85KnnRecallV1V2V4ItemNrtInQueryAndCassiniVisualRankerAndBertRecallWithVMEV3CPCAutoWithCassiniEmbRecallManual&_trksid=p4429486.c101875.m1851&itmprp=cksum%3A2649632809103df643734d2e423594572ef6ba8f43af%7Cenc%3AAQAIAAABQKAO6YGL7I8ZT6VFWcHmDuKm898HGH9cNRsnG%252Fep%252BzC3UPHwPSmfpPq3b41cHxht%252FCiwo5DdbtiFsRNqRhAUlK8x2MLrmISu5pnzSn%252FhiW3P7y%252BKcxGllTjL%252BG3bIP4k8fGgzCrVY1dxXbjuBFp3vefxTYgjBXBRUWQBgGciI%252FuQ5Mjsfl%252B%252FiL4cv70dT88jK1pljjSZyaCIIbAW6GYGqwxdGKs4tc%252BjbPOi6oqX393QDbrxGSAbe61t2Q6vT4EDLkQFzUtAWP8shAv5WRmJrn9%252Bbp5m5DNz%252Bfz4w7b21nuEMc3tNTWr%252BZnaTgO16A1mzQ%252BCeYgin1ezKvkbSOT1IbNr3FJ%252FuUn2FPF%252BCuAuI2nuf%252F36%252BG%252BXObkJLy5ljPvNyqnOy4CGg1cNn1GMMENn30D7%252F6yvCMAV1obaSXievLNR%7Campid%3APLP_CLK%7Cclp%3A4429486&itmmeta=01HQE758NAR1Q9QK8QA5XHEAEN"])
#     buyNowTargets(marketPrice)