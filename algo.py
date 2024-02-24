# Internal libraries
from auctionSearch import currAucPrices
from prices import currPrice
from myEmail import email

# Time library
from datetime import datetime,timezone,timedelta

def main():
    # Permission code from eBay 
    token = "v^1.1#i^1#f^0#p^1#r^0#I^3#t^H4sIAAAAAAAAAOVYa2wUVRTe7baQCkUi7/paBkVtndk7s7PdnbG7ZLttaYF21+7aQo3B2Zk77dDZmWXuXdoNxjRFXjESQiIIghIiGk0QiBoS0QbBABofgPAHf2AIiDGBQBPFPybOTJeyrYRXN7GJ+2cz55577vd995x77gzoHVdasaZhzfUy5/iinb2gt8jppCeA0nEllZNcReUlDpDn4NzZ+0RvcZ/rt2okpNQ03wJRWtcQdPekVA3xtjFIZAyN1wWkIF4TUhDxWOTj4aZFPEMBPm3oWBd1lXA31gYJyS9wnJ+t8oIkFCUBmlbtRsyEHiRkHwMlWYayKHE0kHzmOEIZ2KghLGg4SDCAYUnAkAyboP087eUZjvJxvnbC3QoNpOia6UIBImTD5e25Rh7W20MVEIIGNoMQocZwfTwabqyta05Ue/JihXI6xLGAM2j4U0SXoLtVUDPw9ssg25uPZ0QRIkR4QoMrDA/Kh2+AuQ/4ttQ+LwNF0ccAyMqwyisVRMp63UgJ+PY4LIsikbLtykMNKzh7J0VNNZLLoIhzT81miMZat/X3fEZQFVmBRpCoqwkvCcdiRCjSaSgIKwKJoGCInWSspZZMClDw+RjaR/rYKoZN0t7cMoOxciKPWCeia5JiSYbczTqugSZmOFIZkKeM6RTVokZYxhaefD9uSEG63drSwT3M4E7N2lWYMmVw24931n9oNsaGksxgOBRh5IAtUJAQ0mlFIkYO2pmYS54eFCQ6MU7zHk93dzfV7aV0o8PDAEB7FjctioudMCUQtq9V65a/cucJpGJTEc0iNv15nE2bWHrMTDUBaB1EiA1wHAdyug+HFRpp/Zchj7NneD0Uqj44kWWhFEhKLJCSVay/EPURyqWox8IBk0KWTAlGF8RpVRAhKZp5lklBQ5F4r09mvAEZklIVJ5MsJ8tk0idVkbQMIYAwmRS5wP+nTO420eNQNCAuUKYXKMu55St6wjSWjRq/3BpImL2svVKPB5ZFlre0LKiJQo8hsM3mMdy2vCN4t7VwS/IRVTGVSZjrF0oAq9YLI0KDjjCURkUvLuppGNNVRcyOrQ32GlJMMHA2DlXVNIyKZDidbizUSV0gevd0SNwf60L2p/+kN92SFbISdmyxsuYjM4CQViir+1CinvLognnt8Fi1bpqX2qhHxVsx76xjirVJcpCtIg1eNimbMoVWiJQBkZ4xzHs2FbVuXwm9C2pmN8OGrqrQaKVHXc2pVAYLSRWOtbIuQIIrwhhrtbQfBPwcGwDcqHiJdiNdOtaOpMIdxMXz7vFC7Rn+ch9y2D+6z3kY9Dn7i5xOUA2epOeA2eNcLxS7JpYjBUNKEWQKKR2a+c5qQKoLZtOCYhRNcQzserMhUl4X3VyxMpE98fYxx8S8bws7XwIzh74ulLroCXmfGsAjN0dK6AdnlDEsYBiW9tNehmsHc26OFtPTi6ei1b8+Thw/2RZ8NiI7VqlnVtd/0wrKhpyczhJHcZ/ToZVsuHr26R7mM9/2gUNccO7X+9VE+4XN/Mm9mcSlaOWWi2WVf6DS5ofmHrwem9FWtl88dWU6eZTasecE+UPDlHV7D+9QP959etOHx9ufqe5fO2v8Oe2tK/XK+ekH+g7/9dO1WHz+c/sPruw6uX7qw2Cj6yl2/rVJu8vbGma+cmjZt48e/Vue1r3Y+LKuevvRy828q7t62uSmN8JfnPm+Ytvpz2tS3+2ZdIRvmNy2YOF68cqKhZ4L4x+Yt51V55/tf3Fv6tMNv2w9tu+DKe/P2le56+Kr507J/a9FK348sG7V+d8XDWy79PLVC96vmt5zrd24JdH782MtpQPTLvMfnT/xyZHZm+a83vXun++s2TqzacngXv4DGicdL/URAAA="
    
    # Condition legend
    condition = {"Graded":"2750", "Ungraded":"4000"}
    
    date = datetime.now(timezone.utc)
    timeRange = timedelta(hours=1)
    
    
    prices = currPrice(token, "anthony-volpe",condition["Graded"])
    auctions = currAucPrices(token, "anthony-volpe", "2750", (date+timeRange).isoformat()[:23])
    print(auctions)

if __name__ == "__main__":
    main()