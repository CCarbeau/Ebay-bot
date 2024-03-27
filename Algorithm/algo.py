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

def lambda_handler(event, context):

    # Permission code from eBay 
    token = getToken()
    # token = "v^1.1#i^1#r^0#f^0#I^3#p^1#t^H4sIAAAAAAAAAOVYa2wUVRTebbc1taAGCmglug4qApnZmd2Z7s6ku7htKSyPdukuBapQ7szcaYfuzixz79KuolmrIEgFXxCSJjw0Jj5CYpSEQCrIQ0j8YYj+QFGBKDEYeQRJwBh/ODNdyrYSXt3EJu6fzZx77rnf991z7rkzdLa0bOqaWWuujnbeU7Q9S2eLnE6mnC4rLZl2X3FRZYmDznNwbs8+nnV1F5+tRiCZSAlNEKV0DUF3VzKhIcE2Bom0oQk6QCoSNJCESMCSEAvPmyt4KVpIGTrWJT1BuCN1QULiFEkEilglKpK/ipVNq3YtZlwPEoDxAa+oAOD3S4pPUsxxhNIwoiEMNBwkvLSXJWkfybBxhhc4TmA4iuP9LYS7GRpI1TXThaKJkA1XsOcaeVhvDhUgBA1sBiFCkXB9rDEcqZvREK/25MUK5XSIYYDTaPBTrS5DdzNIpOHNl0G2txBLSxJEiPCE+lcYHFQIXwNzF/BtqQM8QwdYjoV+BXC8LBdEynrdSAJ8cxyWRZVJxXYVoIZVnLmVoqYa4nIo4dxTgxkiUue2/uanQUJVVGgEiRk14cXhaJQI1bYbKsIqIBEEhtRORpvqSBFAwHFehiM5tsrLiowvt0x/rJzIQ9ap1TVZtSRD7gYd10ATMxyqDJunjOnUqDUaYQVbePL8vMyAgr4Wa0v79zCN2zVrV2HSlMFtP95a/4HZGBuqmMZwIMLQAVsgs2hSKVUmhg7amZhLni4UJNoxTgkeT2dnJ9Xpo3SjzeOlacazaN7cmNQOk4Cwfa1at/zVW08gVZuKBM2ZSBVwJmVi6TIz1QSgtREhNsDzPJ3TfTCs0FDrvwx5nD2D66FQ9eFjvIriVXgxIPIK6+cKUR+hXIp6LBxQBBkyCYwOiFMJIEFSMvMsnYSGKgs+TvH6Agok5SpeIVleUUiRk6tIRoGQhlAUJT7w/ymT2030GJQMiAuU6QXKcn7Fyq4wgxWjxq80B+JmL2uZpscCy2tXNDXNrmmEHgOwDRLnXbiiLXi7tXBD8rUJ1VQmbq5fKAGsWi+MCLN0hKE8LHoxSU/BqJ5QpczI2mCfIUeBgTMxmEiYhmGRDKdSkUKd1AWid0eHxN2xLmR/+k960w1ZISthRxYraz4yA4CUSlndh5L0pEcH5rXDY9W6aW61UQ+Lt2reWUcUa5NkP1tV7r9sUjZlCq2UKAMiPW2Y92yq0bp9xfUOqJndDBt6IgGNZmbY1ZxMpjEQE3CklXUBElwFI6zVMn6GZtkqhuGGxUuyG2nrSDuSCncQu6bf4YXaM/jlPuSwf0y38yDd7dxX5HTS1fQTzCT6sdLiBa7iUZVIxZBSgUIhtU0z31kNSHXATAqoRtFYxx/vbppVWzmjcfPU5+OZY71HHaPyvi1sX0I/OPB1oayYKc/71EBPvD5Swtw/YbSXpX0My/Acx3At9KTroy5mvKvi46hRtqf86qrvXiur7nVc/nDn/pkP0KMHnJzOEoer2+mYP+XH57rXHfrs6NKt6EKPc+N815OruCnv1Z14YeGLm1Yf30a2L9v4wfpzax99+ND4LZ+81FCNZ58FjxzZteCtAxWejvbmtaP6XAfGnfi559gz5PtP9W2KrW9448DmyzvOn5vT9cUvX3+7YVFP4qErr59pHjP9witjdibHLjW+CmcWzxwT33L0+An/Qan1iufVDcrhikt/Xl7GnHz6m9Zdc8ZfPP3O9PqNbMWGCRf9xacvbd3WMWdH8tc+UPlm71+/j7t4SvTtbOJ/Sv92Khp5O7tv0eyPxNbJx+vXl5R3PXv6y91n/C/3/NA6cf/nf9MtpetK1e87rizZI987LUt0Hv7Uf/7k3slH6o7A3Xt7L7WN6+vfy38AoBsQjfURAAA="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=2)

    aucTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    buyTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    offerTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    
    cards = createCards(condition)
    
    # emailAddresses = ["cikoticz24@gmail.com","dominicpiz2@gmail.com","abby.samson@richmond.edu"]
    emailAddresses = ["cikoticz24@gmail.com"]

    for item in cards:
        prices = currPrice(token, item.name, item.cond, item.auto)

        auctions = currAucPrices(token, item.name, item.cond,(date+timeRange).isoformat()[:23], item.auto)

        # Auction Targets 
        aucs = aucTargets(prices[0],auctions)
        
        if(len(aucTargDf)==0 and len(aucs)!=0):
            aucTargDf = aucs
        elif(len(aucs!=0)):
            aucTargDf = pd.concat([aucTargDf,aucs])
            aucTargDf = aucTargDf.reset_index(drop=True)

        # Buy Now Targets:
        buyNow = buyNowTargets(prices[2])
        
        if(len(buyNow)!=0 and len(buyTargDf)==0):
            buyTargDf = buyNow
        elif(len(buyNow)!=0):
            buyTargDf = pd.concat([buyTargDf,buyNow])
            buyTargDf = buyTargDf.reset_index(drop=True)

        # Best Offer Targets;
        offers = offerTargets(prices[0],prices[1])
        
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
    
    return {
        'statusCode': 200,
        'body': 'Success'
    }

if __name__ == "__main__":
    print(lambda_handler("hi","ok"))