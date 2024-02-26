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
    token = "v^1.1#i^1#r^0#f^0#I^3#p^1#t^H4sIAAAAAAAAAOVYa2wUVRTuttsahEqkjSJisgwQkLqzM7M7uztjd+t2W6AI7dLdFi0RuDNztx26O7Ode7ePILEpBlQ08AdNQEg1vmIiJSEiwaSCRghqlUciBAxgogRB/iii+IjemS5lWwmvbmIT989mzj333O/77jn33Bmmu2jcnLXz1/5abLsrv7eb6c632djxzLiiwrJ7CvKnFOYxWQ623u4Z3faegnPlCCQTKbEeopSuIejoTCY0JFrGAJU2NFEHSEWiBpIQiVgWo6FFC0WOZsSUoWNd1hOUo6YqQHndfgUIPsknQZlx8xKxaldjxvQABQSPLPglSfGTQYHnyDhCaVijIQw0HKA4hvM4Gc7JeWOsIHK8yDO0l2GaKEcjNJCqa8SFZqigBVe05hpZWG8MFSAEDUyCUMGa0NxoXaimqro2Vu7KihXM6BDFAKfR8KewrkBHI0ik4Y2XQZa3GE3LMkSIcgUHVxgeVAxdBXMH8C2p/TLwQQZICif5JbfkzYmUc3UjCfCNcZgWVXHGLVcRaljFXTdTlKghrYQyzjzVkhA1VQ7zb3EaJNS4Co0AVV0ZejIUiVDBcIuhIqwCJ4LAkFuckfoqpwQg4HmO5Z28x8t5JNadWWYwVkbkEeuEdU1RTcmQo1bHlZBghiOVYbOUIU51Wp0RimMTT5Yfx2YU5AW2ydzSwT1M4xbN3FWYJDI4rMeb6z80G2NDldIYDkUYOWAJRIomlVIVauSglYmZ5OlEAaoF45TocnV0dNAdblo3ml0cw7CuJxYtjMotMAkoy9esddNfvfkEp2pRkSGZiVQRd6UIlk6SqQSA1kwFPX5BEJiM7sNhBUda/2XI4uwaXg+5qg9Binu9DB/3yYrH7+PZXNRHMJOiLhMHlECXMwmMVohTCSBDp0zyLJ2EhqqIbj7Ouf1x6FS8QtzpEeJxp8QrXicbh5CBUJLIKfj/KZNbTfQolA2Ic5TpOcpyoa29M8TiuFHpizf6Y6SXNZXpUf/KcFt9/YLKOugygKdW5rklbc2BW62F65IPJ1SiTIysnysBzFrPjQjzdYShMip6UVlPwYieUOWusbXBbkOJAAN3RWEiQQyjIhlKpWpydVLniN5tHRJ3xjqX/ek/6U3XZYXMhB1brMz5iAQAKZU2uw8t60mXDsi1w2XWOjEvt1CPirdK7qxjijUhOchWVQYvm7RFmUbtMm1ApKcNcs+m68zbV0xvhRrpZtjQEwloNLKjruZkMo2BlIBjraxzkOAqGGOtlvUxfsHH8/zoeMlWI10+1o6k3B3E9orbvFC7hr/cB/OsH9tj+5jpsfXn22xMOTOTnc5MKyposBdMmIJUDGkVxGmkNmvkndWAdCvsSgHVyC/J++n1TfPDU6rrXp6zKtZ1aMuBvAlZ3xZ6n2ImD31dGFfAjs/61MBMvTZSyE68v5jzMBznZQWO7HgTM/3aqJ29z17aR897+/GSR55ZumZa1cm+zqWbjz4tM8VDTjZbYZ69x5Y3fUHk7trLZQevrP9E27VwU+zwO/QeR9+HZ9Il5y4sO5MY2PNj0+GKF17zfNk0M7Cd3T1p50tb062XH1vRGOsrFTZuP3Bg/eZlz71bElFmF8/bf6g8/OcbNe3r/t525CFqybbVK37rz69Luv/Y9/veM8A+0HBl3StHAhdXvvfwpH3u1Q9s7J/wHX+wd/WOR0+cTRd6F9uWzmp4c+eiGZ6ZC9jTA5Vb3EfVvQcvPN92ZNax86fZUEXep8d/2cBE9nMdP/QfU+4Ne0+9P9D62ayKFx9sm33p4prmHaXPTj757ap9Z0vb/pr7+VcXdr36TUvD9/l7w1PLJhahr0+dP2Fv+ugLz9b2DzZc+nlz5Dhcs5t/a3Av/wFd5gvu9REAAA=="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=8)

    aucTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    buyTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    offerTargDf = pd.DataFrame(columns = ["Title", "Price", "Discount", "Link"])
    
    searches = ["2023 anthony-volpe psa 10",
                "2023 adley-rutschman psa 10",
                "2022 julio-rodriguez psa 10",
                "2022 bobby-witt-jr psa 10",
                "2023 bowman 1st max-clark",
                "2023 bowman 1st wyatt-langford",
                "2022 bowman 1st jackson-chourio"]
    
    emailAddresses = ["cikoticz24@gmail.com", "dominicpiz2@gmail.com","abby.samson@richmond.edu"]

    for item in searches:
        prices = currPrice(token, item, condition["Graded"])
        auctions = currAucPrices(token, item, condition["Graded"], (date+timeRange).isoformat()[:23])
        bestOffer = bestOffPrices(token, item, condition["Graded"])

        # Auction Targets 
        aucTargDf = pd.concat([aucTargDf,aucTargets(prices,auctions),])
        aucTargDf = aucTargDf.reset_index(drop=True)

        # Buy Now Targets:
        buyTargDf = pd.concat(buyTargDf,buyNowTargets(prices))
        buyTargDf = buyTargDf.reset_index(drop=True)

        # Best Offer Targets;
        offerTargDf = pd.concat(offerTargDf,offerTargets(prices,bestOffer))
        offerTargDf = offerTargDf.reset_index(drop = True)

    aucTargDf = aucTargDf.sort_values(by="Discount", ascending=False)
    email(emailAddresses,aucTargDf, buyTargDf, offerTargDf)

if __name__ == "__main__":
    main()