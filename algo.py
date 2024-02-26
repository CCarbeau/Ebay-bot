# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from myEmail import email
from analyze import aucTargets

# Time library
from datetime import datetime,timezone,timedelta

def main():
    # Permission code from eBay 
    token = "v^1.1#i^1#r^0#p^1#I^3#f^0#t^H4sIAAAAAAAAAOVYa2wUVRTeabcltQ8liMgjug6vCO68dmYfk+7E7YO0BrqluxYoVrgze6edMjuznXu37SKapjFoYgwalYiANlJC/EP4VRUBCUiIJgRMeCSGSIBgqjEaCcaYGHF2ui3bSnh1E5u4fzZz7rnnft93z7nnzjD9pWXLtjZs/aOSmFE02M/0FxEEW86UlZYsryoumlfiYvIciMH+Rf3ugeKRagSSekpsgShlGgh6+pK6gUTHGCbTliGaAGlINEASIhErYiyyaqXIUYyYskxsKqZOehrrwmQgwQic7Od5nmUDIV/AthpjMeNmmGSBCoJQDvhCUFETIdkeRygNGw2EgYHDJMdwvJfhvJw/zggiw4q8QPmEQBvpaYUW0kzDdqEYUnLgis5cKw/rnaEChKCF7SCk1BhZEYtGGuvqm+LVdF4sKadDDAOcRhOfas0E9LQCPQ3vvAxyvMVYWlEgQiQtja4wMagYGQPzAPAdqYMs5w+xMCj4ZD8XUgoj5QrTSgJ8ZxxZi5bwqo6rCA2s4czdFLXVkLuggnNPTXaIxjpP9m91GuiaqkErTNbXRNZFmptJqbbT0hDWgBdBYCmd3uaWOq8MIBAEjhW8Au/neJn15ZYZjZUTedI6taaR0LKSIU+TiWugjRlOVIYXhTxlbKeoEbUiKs7iyfcLjCnI23702B6mcaeR3VWYtGXwOI931398NsaWJqcxHI8wecARKEyCVEpLkJMHnUzMJU8fCpOdGKdEmu7t7aV6fZRpddAcw7D02lUrY0onTALS8c3WetZfu/sEr+ZQUaA9E2kizqRsLH12ptoAjA5S4oOhUIjJ6T4RljTZ+i9DHmd6Yj0Uqj5gAgT9PlbwQX8ChgpRHVIuQeksCiiDjDcJrE0Qp3SgQK9iZ1k6CS0tIfoElfMFVehN+EOqlw+pqlcWEn4vq0LIQCjLSij4/ymSe03zGFQsiAuU5wXK8VB3T1+ExapVE1Bbg3G7k7UtN2PBrtrulpbnaqKQtgDfpAjcmu6O8L1Wwm3J1+qarUzcXr9wAji1XgARGkyEYWJK9GKKmYLNpq4pmem1wT4r0QwsnIlBXbcNUyIZSaUaC3VOF4jefR0SD8a6kN3pP+lMt2WFsgk7vVhl5yM7AEhpVLb7UIqZpE1gXzpsU7bWtQ0O6inx1uwb67RibZMcZaslRq+alEOZQj0KZUFkpi37lk1Fs3evuLkJGnY3w5ap69BqZadczclkGgNZh9OtrAuQ4BqYZq2WDTDBEOcLMMKUeClOI90w3Y6kQh7E7vB9Xafpia/2ksv5sQPEMWaAOFJEEEw1s5hdyDxVWvy8u7hiHtIwpDSgUkjrMOw3VgtSm2AmBTSraJbr+sfvNdTOq49uX/ZSPHNm50lXRd6XhcF25vHxbwtlxWx53ocGZsGtkRL24TmVHM9wnJ8RGJYX2piFt0bd7GPuR89WbKnt7jp6wb/oWsnmIX314cj2DFM57kQQJS73AOFSi25I2oxZM84M3Th18Nxa7tX29vazhvjWxrnNwTf2n3x77YvSZbJ/1+BeeuTpi3t/OAS+Kz7/5JxTv+whKk6UDXs6PpcaSn89Mvu3fZ9K7st/L9l/Be5eOvvAtoM/77k+3Hxwy7evuHvW3Hxmwc0Tmflzv3zq2qXXPtt1UVq/wyQGdrddLaeqDny1fv6q/o8+/PHCzSWLlm4YPI6Oy0+s6To3LNEZ/QXP0AfvzPz9SlPgaGR3/cuVh0s7Z/csfvN0eTAeeGjdyLq/pC3dXwvvVldsrmrYx++8er6b+GLbjuWfPHJNqLgwy3V6aLju0rFnZ1LXe0uq/pxJhKPf0Mv2jLRfel3+6f3GQxu3DXxfPbqX/wDdZbgp8xEAAA=="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=1)
    
    item = "2023 topps chrome"
    
    prices = currPrice(token, item, condition["Graded"])
    auctions = currAucPrices(token, item, condition["Graded"], (date+timeRange).isoformat()[:23])
    targets = aucTargets(prices,auctions)
    email(["cikoticz24@gmail.com","christian.carbeau@duke.edu"],targets)

if __name__ == "__main__":
    main()