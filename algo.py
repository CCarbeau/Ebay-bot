# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from myEmail import email
from analyze import aucTargets

# Time library
from datetime import datetime,timezone,timedelta

def main():
    # Permission code from eBay 
    token = "v^1.1#i^1#r^0#I^3#f^0#p^1#t^H4sIAAAAAAAAAOVYe2wURRjvXR9aXoryqGhIu7xMy+3N7t3t3S69C9cWaBV6R+8oWq1kbne2XXq3u93Za3sQaT1LlQAmGlGJ4VFiCNEmEP3HGNQokv6hIYp/+Ug0mCAhFqMChpCqc9tSrpXw6iU28bLJZWa++eb3+833zTe7oKeouLyvtu/PmbZ77Ad7QI/dZmOmg+KiwopZ+fYFhXkgy8B2sGdxT0E6/1wlhom4LjQgrGsqRqVdibiKBavTTyUNVdAgVrCgwgTCgikKkeC6tQJLA0E3NFMTtThVWlfjpxiO4bxuWQaMDFwcIJ3qNZdRzU9JXrcIZA/rcnEShG6OjGOcRHUqNqFq+ikWsG4HYB0sF2W8AnkAT7t4pokqbUQGVjSVmNCAClhoBWuukQX15kghxsgwiRMqUBdcHQkF62pW1UcrnVm+AqMyRExoJvH4VrUmodJGGE+imy+DLWshkhRFhDHlDIysMN6pELwG5i7gW0q7Wcnn9bhFHnAs7+NhTqRcrRkJaN4cR6ZHkRyyZSog1VTM1K0UJWrENiPRHG3VExd1NaWZv/VJGFdkBRl+alVV8MlgOEwFqlsNBZsKdGAEDbHVEW6occQggh4Py3gcHjfHumOMa3SZEV+jIk9Yp1pTJSUjGS6t18wqRDCjicqALGWIUUgNGUHZzODJtuOvKejjmjJbOrKHSbNVzewqShAZSq3mrfUfm22ahhJLmmjMw8QBSyA/BXVdkaiJg1YkjgZPF/ZTraapC05nZ2cn3emiNaPFyQLAOJ9YtzYitqIEiQ/LNpPrxF659QSHYlEREZmJFcFM6QRLF4lUAkBtoQJuH8/zYFT38bACE3v/1ZHF2Tk+H3KVH5JXlr2QpAbyAA8r5uSoCYyGqDODA8VgypGARhsy9TgUkUMkcZZMIEORBJdHZl0+GTkkjpcdbl6WHTGPxDkYGSGAUCwm8r7/T5rcbqBHkGggM1eRnpso59s7uoKMKRtVXrnRFyW1rKlCi/g2V7c3NDxWFUJOA7rrRQ+7sb3Ff7u5cEPy1XGFKBMl6+dMgEyu50SEWg2bSJoUvYio6SisxRUxNbU22GVIYWiYqQiKx0nHpEgGdb0uZyd1bujd0SFxd6xzWp/+i9p0Q1Y4E7BTi1VmPiYOoK7QmepDi1rCqUFy7XDCTK7ryiYL9aR4K+TOOqVYE5IjbBVp5LJJW5Rp3CHSBsJa0iD3bDqUuX1FtTakkmpmGlo8joxGZtLZnEgkTRiLo6mW1jkIcAVOsVLLeIGP57w+lp8UL9EqpJum2pGUw4O4IHBnF2rn+Hf7QJ71Y9K2T0Ha9pHdZgOVYAmzCJQV5W8oyJ+xACsmohUo01hpUck7q4HoNpTSoWLYH8z7/dCe2uoFq0KvlW+Npr58czBvRtanhYPNoGTs40JxPjM960sDeOT6SCFz3/yZrBuwLMd4yb7zTWDR9dECZl7BnCV7f36rvKr/4i+negc+PF3bvXOWeALMHDOy2QrzCtK2vKKel5e6BiLDH393eWhwz7JpRXT3igvszj1HC3p3724MPyr0ly881b1v2raKSPv+xoeKYiV7l16kpI6SpqF088Dhut9Wb9n31SvlH3z2Hth/4OuBsKdi/bvHD30Tk58/smT+9y8sv1QyeGD49cbuw8dKlveePbPTzR0VH16/YevikOvFeeG+TSvVLc/OPfJ22bkDQxEpf2m0WVj5RV/ZpfNXzmy8+mPoZHrZ1Y7eHb92PnP/8I7Pq4XLZ4rRt4H6yvTT83/w4ObZa9aevvRceM37u9oHxSsLV/z09x9DfwWb7MfnnHvqxBt6xfDwee7Yq7ry0q57Z2+2t83tT9m37T27Lyj0X/jknZPbHyhLPz6yl/8A0dx5a/QRAAA="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=1)
    
    item = "2023 anthony-volpe psa 10"
    
    prices = currPrice(token, item, condition["Graded"])
    print(prices)
    auctions = currAucPrices(token, item, condition["Graded"], (date+timeRange).isoformat()[:23])
    print(auctions)
    targets = aucTargets(prices,auctions)
    print(targets)
    email(["cikoticz24@gmail.com"],targets)

if __name__ == "__main__":
    main()