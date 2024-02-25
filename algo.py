# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from myEmail import email

# Time library
from datetime import datetime,timezone,timedelta

def main():
    # Permission code from eBay 
    token = "v^1.1#i^1#r^0#f^0#p^1#I^3#t^H4sIAAAAAAAAAOVYXWwUVRTe3e5WEIoQKX9BXIYSsbAzd2Z3dmeG7prttg0F+kN3rbWGlNnZO9uhuzPbuXdpVzFpSiREQSRQMGBiIz8PaAz0QSUBDUQl+CLyEzGpERM1PphIDBEeePDudlu2lfDXTWzivmzm3HPP/b7vnnPPnQF9pdMrt6/ZfqvM+oRtsA/02axWdgaYXupYOavEtshhAQUO1sG+ij57f8nvVUhOJlJSC0QpQ0fQ2ZtM6EjKGf1U2tQlQ0YaknQ5CZGEFSkcbFgvcTSQUqaBDcVIUM76Gj/l5bxuzu1xKyrrA1yUGPXRkBHDT4nA7fO5oyLPQxCDioeMI5SG9TrCso79FAc4jwtwLo6PACBxXskj0IJbaKecrdBEmqETFxpQgRxaKTfXLIB6f6QyQtDEJAgVqA/WhZuC9TW1jZEqpiBWIC9DGMs4jcY/hYwYdLbKiTS8/zIo5y2F04oCEaKYwMgK44NKwVEwjwF/RGkRwqjq9rCcyMUUoShK1hlmUsb3h5G1aDGXmnOVoI41nHmQoESM6Gao4PxTIwlRX+PM/m1IywlN1aDpp2qrgy8Hm5upQKjT1BDWZBeCsql0uppbalxRGco8z7G8i/d4OU+UdeeXGYmV13jCOiFDj2lZxZCz0cDVkGCGE5VhC5QhTk16kxlUcRZPoR83qiBH/JjRLUzjTj27qTBJZHDmHh+s/9hsjE0tmsZwLMLEgZxAfkpOpbQYNXEwl4j53OlFfqoT45TEMD09PXSPmzbMOMMBwDJtDevDSidMylTeN1vrvUh78ASXlqOiQDITaRLOpAiWXpKoBIAepwIeQRRFkNd9PKzAROu/DAWcmfHlUKzyUHmVd7M+H8crgq9I9RHIpyiTxQGjcsaVlM0uiFMJWYEuheRZOglNLSa5eZVzCyp0xbyi6vKIquqK8jGvi1UhBKRso4oo/H/K5GETPQwVE+KiZXpRslzs3tIbZLFqVvvUViFCWln7SiMsbA51t7SsrW6CjCl7GhWee6k77n/YWrgn+VBCI8pEyPrFEyBb68UQYY2BMIxNil5YMVKw2UhoSmZqbbDbjDXLJs6EYSJBDJMiGUyl6ot3UheF3iMdEo/Hurj96T/oTfdkhbIJO7VYZecjEkBOaXS2+9CKkWQMmVw7iClb61pHDvWkeGvkyjqlWBOSI2y12Mhlk85RptEWhTYhMtImuWbTTdnbV8TogjrpZtg0EglotrKTruZkMo3laAJOtbIuQoJr8hRrteSFURA4IABhUryUXCPtmGpHUjEPYrv/kS7UzPhX+4Al92P7redAv/Vzm9UKqsBydhlYWlryor1k5iKkYUhrskojLa6TV1YT0l0wk5I10/a05a8PBtaEFtU27a98LZK5eOi8ZWbBl4XBjWDB2LeF6SXsjIIPDWDx3REH+9T8Ms4DOI4HgPN6hHaw7O6onZ1nn2u52qJuuODYdPOPhiMVm7/45mw8tAuUjTlZrQ6Lvd9qsb2/pb+td3Xk4JxL8z++MxhvuHZm+Ou3vj274nhfS9f1O3uSCysP3Lg2Z2fo+htLSm0Ru3ng6JuXpbZz5c+vOnaAmtV9arZj3/C1fVpwx9qD84Lb3vlosbV23QAdh8zMH1+9fX5D8HL52yfeqxBx4JX9z7HPDG2//uSOo8eurm6/efLIuhruy1MnMpGLg2tPMzcXf3jlqw44sHXPwO74J98rloVw6NOlWNw61Gwa4Ltte28f3NO+u+3nJXXGsP/PoXcP31hn+2Va5TTmB2P5T3iFeOEKN7zw1uyNm5zlh8vqOk6uPPNZRfdg/Fz5gtivp184tJdpXFWVcMz57fjcvy9X3Ho96jxEP3tp596RvfwH5byU6/MRAAA="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=1)
    
    
    prices = currPrice(token, "2023 topps chrome anthony-volpe psa 10",condition["Graded"])
    auctions = currAucPrices(token, "2023 topps chrome anthony-volpe psa 10", "2750", (date+timeRange).isoformat()[:23])
    print(prices)
    print(auctions)

if __name__ == "__main__":
    main()