import pandas as pd
import numpy as np

# Takes in a dataframe of the market prices returned by prices
# Takes in a dataframe of the current auctions prices from auctionSearch
def targets(marketPrice, auctionPrice):
    print(1)

if __name__ == "__main__":
    marketPrice = pd.DataFrame(columns = ["Title", "Price","Discount","Link"])
    marketPrice["Title"]=pd.Series(data=["Anthony Volpe Bowman Chrome 1st"])
    marketPrice["Price"]=pd.Series(data=[100])
    marketPrice["Link"]=pd.Series(data=["https://www.ebay.com/itm/264963280910?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D260885%26meid%3D3df643734d2e423594572ef6ba8f43af%26pid%3D101875%26rk%3D2%26rkt%3D12%26sd%3D196250216985%26itm%3D264963280910%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedV3MskuWithLambda85KnnRecallV1V2V4ItemNrtInQueryAndCassiniVisualRankerAndBertRecallWithVMEV3CPCAutoWithCassiniEmbRecallManual&_trksid=p4429486.c101875.m1851&itmprp=cksum%3A2649632809103df643734d2e423594572ef6ba8f43af%7Cenc%3AAQAIAAABQKAO6YGL7I8ZT6VFWcHmDuKm898HGH9cNRsnG%252Fep%252BzC3UPHwPSmfpPq3b41cHxht%252FCiwo5DdbtiFsRNqRhAUlK8x2MLrmISu5pnzSn%252FhiW3P7y%252BKcxGllTjL%252BG3bIP4k8fGgzCrVY1dxXbjuBFp3vefxTYgjBXBRUWQBgGciI%252FuQ5Mjsfl%252B%252FiL4cv70dT88jK1pljjSZyaCIIbAW6GYGqwxdGKs4tc%252BjbPOi6oqX393QDbrxGSAbe61t2Q6vT4EDLkQFzUtAWP8shAv5WRmJrn9%252Bbp5m5DNz%252Bfz4w7b21nuEMc3tNTWr%252BZnaTgO16A1mzQ%252BCeYgin1ezKvkbSOT1IbNr3FJ%252FuUn2FPF%252BCuAuI2nuf%252F36%252BG%252BXObkJLy5ljPvNyqnOy4CGg1cNn1GMMENn30D7%252F6yvCMAV1obaSXievLNR%7Campid%3APLP_CLK%7Cclp%3A4429486&itmmeta=01HQE758NAR1Q9QK8QA5XHEAEN"])
    auctionPrice = pd.DataFrame(columns = ["Title", "Price","Discount","Link"])
    auctionPrice["Title"]=pd.Series(data=["Anthony Volpe Bowman Chrome 1st"])
    auctionPrice["Price"]=pd.Series(data=[60])
    auctionPrice["Link"]=pd.Series(data=["https://www.ebay.com/itm/264963280910?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D260885%26meid%3D3df643734d2e423594572ef6ba8f43af%26pid%3D101875%26rk%3D2%26rkt%3D12%26sd%3D196250216985%26itm%3D264963280910%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedV3MskuWithLambda85KnnRecallV1V2V4ItemNrtInQueryAndCassiniVisualRankerAndBertRecallWithVMEV3CPCAutoWithCassiniEmbRecallManual&_trksid=p4429486.c101875.m1851&itmprp=cksum%3A2649632809103df643734d2e423594572ef6ba8f43af%7Cenc%3AAQAIAAABQKAO6YGL7I8ZT6VFWcHmDuKm898HGH9cNRsnG%252Fep%252BzC3UPHwPSmfpPq3b41cHxht%252FCiwo5DdbtiFsRNqRhAUlK8x2MLrmISu5pnzSn%252FhiW3P7y%252BKcxGllTjL%252BG3bIP4k8fGgzCrVY1dxXbjuBFp3vefxTYgjBXBRUWQBgGciI%252FuQ5Mjsfl%252B%252FiL4cv70dT88jK1pljjSZyaCIIbAW6GYGqwxdGKs4tc%252BjbPOi6oqX393QDbrxGSAbe61t2Q6vT4EDLkQFzUtAWP8shAv5WRmJrn9%252Bbp5m5DNz%252Bfz4w7b21nuEMc3tNTWr%252BZnaTgO16A1mzQ%252BCeYgin1ezKvkbSOT1IbNr3FJ%252FuUn2FPF%252BCuAuI2nuf%252F36%252BG%252BXObkJLy5ljPvNyqnOy4CGg1cNn1GMMENn30D7%252F6yvCMAV1obaSXievLNR%7Campid%3APLP_CLK%7Cclp%3A4429486&itmmeta=01HQE758NAR1Q9QK8QA5XHEAEN"])
    targets(marketPrice,auctionPrice)