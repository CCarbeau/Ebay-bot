import json
import requests 
import pandas as pd
import numpy as np

def soldPrice():
    # NEED TO FIX LAST SOLD DATE INPUT
    item = "anthony-volpe"
    count = 10
    date = "[2024-01-30T00:00:00Z..2024-02-17T00:00:00Z]"
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+item+"&limit="+str(count)+"&filter=buyingOptions:{AUCTION|FIXED_PRICE}&filter=lastSoldDate:[2024-01-30T00:00:00Z..2024-02-17T00:00:00Z]"
    headers = {"Authorization":"Bearer v^1.1#i^1#r^0#I^3#f^0#p^1#t^H4sIAAAAAAAAAOVYfWwURRTvXXuYSvkwgEADemwlJCW7N7t3e71deyfXr7QV2tI7SltFnN2dbZfe7V5352hPg5aiICQYiFAhSiQohmAM8QuJMWAQqBiMqAQTNIpYlH9AMSaEgMbdbSnXSvjqJTbx/rnsmzdvfr/fvDdvdkHXmNzC1ZWrL41z3OPc3gW6nA4HPRbkjnHNHZ/tzHdlgTQHx/auh7pyurPPFRswHkvw9chIaKqB3J3xmGrwtjFIJHWV16ChGLwK48jgschHwgvm8wwF+ISuYU3UYoS7qixIcELAxwX8fi8t+2mGYU2rei1mVAsSghwQkFjE+f0+WhIkrzluGElUpRoYqjhIMIDxkYAhaS5Ke3mW42lA+dlAM+FuQLqhaKrpQgEiZMPl7bl6GtabQ4WGgXRsBiFCVeGKSG24qqy8JlrsSYsVGtAhgiFOGkOfSjUJuRtgLIluvoxhe/ORpCgiwyA8of4Vhgblw9fA3AV8W2qv4GckLwD+Ip/EyhKXESkrND0O8c1xWBZFImXblUcqVnDqVoqaagjLkIgHnmrMEFVlbutvYRLGFFlBepAoLwk3hevqiFBpq64YWIGkgaAutpJ19WWkABFkWYZmSdbnZ3wC7R1Ypj/WgMjD1inVVEmxJDPcNRouQSZmNFwZX5oyplOtWquHZWzhSfdjBxVkm60t7d/DJG5VrV1FcVMGt/14a/0HZ2OsK0ISo8EIwwdsgYIETCQUiRg+aGfiQPJ0GkGiFeME7/F0dHRQHV5K01s8DAC0p3HB/IjYiuKQsH2tWrf8lVtPIBWbiojMmYbC41TCxNJpZqoJQG0hQr4Ax3FgQPehsELDrf8ypHH2DK2HTNUHJ9CSTAPGX8QFfILfl4n6CA2kqMfCgQSYIuNQb0M4EYMiIkUzz5JxpCsS72VlxhuQESn5OZn0cbJMCqzkJ2kZIYCQIIhc4P9TJreb6BEk6ghnKNMzlOVc+/LOMI1lvaRIbghEzV7WPFeLBJaVttfXV5fUIo8OfTUiyyxubwnebi3ckHxpTDGViZrrZ0oAq9YzI0KlZmAkjYheRNQSqE6LKWJqdG2wV5fqoI5TERSLmYYRkQwnElWZOqkzRO+ODom7Y53J/vSf9KYbsjKshB1drKz5hhkAJhTK6j6UqMU9GjSvHR6r1k3zUhv1iHgr5p11VLE2SfazVaT+yyZlU6aM5SKlI0NL6uY9m6q1bl9RrQ2pZjfDuhaLIb2BHnE1x+NJDIUYGm1lnYEEV+Aoa7V0EQh4WZpmR8ZLtBvp0tF2JGXuIM555A4v1J6hL/ehLPtHdzsOgm7HfqfDAYrBbLoAzBqTvSgnOy/fUDCiFChThtKimu+sOqLaUCoBFd05KeuPHZsrS/PLa3sKn46mjr/Sm5WX9m1h+xIwbfDrQm42PTbtUwOYcX3ERU+YOo7xAYbmaC/L0aAZFFwfzaHvz5n8y4tzAr2T3786Jffvnt2HnY1nvnY2gnGDTg6HKyun25H15OnN+fP4He9Vz+a3uM7tPsKOdx04+c6hsyumT+u9fPa+H6jzKyu27nscVk54uPJIgPy9ebK8N3pw8fTNm1pWbFq5oenCn8XnPwdNlVe+OnGpBvSd+LTg+3urj6/9bXX1TveXs5jTu9dffPSNLyo+e+qlq1vWrfmurf7Yq28udhU+4V337s7Xygs+WPGs+vLlwilvlVQ8OPGTnz27juJEQfjIvIvj3z6w9uS+Ja9PmNkrHO47+uMBR33D+pmnnvMumrRw49Y9UTe82Nx+6OO/er5dU/hNyYcbn3fNORY/D1746MzCbXs2nGqC85/pUVYt31rwk3h876m8UJ7vCvp16f5dU7OFGY1btAuP5ax6oG9b38T+vfwHP81Ar/URAAA=",
                "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
                "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"}
    apiReq = requests.get(url,headers=headers)
    parseddoc = apiReq.json()
    print(parseddoc)
    # prices = pd.Series(index = np.arange(count))
    # ids = [None]*count
    # i = 0
    # for item in (parseddoc["itemSummaries"]):
    #     title = item["title"]
    #     ids[i]=title
    #     # condition = item["condition"][0]["conditionDisplayName"][0]
    #     price = item["price"]["value"]
    #     prices[i] = price
    #     i = i + 1
    # ret = pd.Series(index = ids, data = prices.values)
    # return ret

if __name__ == "__main__":
    soldPrice()