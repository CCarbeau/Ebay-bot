# Email sending libraries
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl

#Time library
from datetime import datetime

# Pandas for testing
import pandas as pd

# Email addresses is an array of the recipients of the email
# Items is a list of identified targets that we are notifying the userbase about
def email(emailAddresses,aucTargDf, buyTargDf, offerTargDf):
    if(aucTargDf.size != 0):
        myEmail ="christiancarbeau@gmail.com"
        password = "ezcx vfwc sbae ohpk"

        time = datetime.now().strftime("%m/%d/%y %H:%M")
        
        subject = time + " Targets:"
        
        email = MIMEMultipart("mixed")
        email["From"]=myEmail
        email["Subject"]=subject
        
        # Create body of the email: 

        # AUCTION TARGETS:
        html_content = """\
<html>
<head>
  <title>Auction Targets</title>
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid black;
      padding: 8px;
      text-align: left;
    }
  </style>
  <style>
    td.discount-cell-green {
      background-color: rgba(0, 255, 0, 1);
    }
    td.discount-cell-light-green {
      background-color: rgba(0, 255, 0, 0.5);
    }
    td.discount-cell-yellow {
      background-color: rgba(255, 255, 0, 1);
    }
  </style>
</head>
<body>
  <h2>Auction Targets</h2>
  <table>
    <tr>
      <th>Item</th>
      <th>Price</th>
      <th>Discount</th>
      <th>Link</th>
    </tr>
"""
        # Add rows dynamically
        for row,value in aucTargDf.iterrows():
            item = aucTargDf.loc[row]["Title"]
            price = aucTargDf.loc[row]["Price"]
            discount = ("%.2f" % round(aucTargDf.loc[row]["Discount"], 2))
            discount_cell_class = "green"
            if(float(discount) >= 50):
                discount_cell_class="discount-cell-green"
            elif(float(discount) >= 35):
                discount_cell_class="discount-cell-light-green"
            else: 
                discount_cell_class="discount-cell-yellow"
            try: 
              link = aucTargDf.loc[row]["Link"]
            except:
              link = "None"
            html_content += f"""
            <tr>
              <td>{item}</td>
              <td>{price}</td>
              <td class ={discount_cell_class}>{discount}</td>
              <td><a href="{link}">Link</a></td>
            </tr>
            """

        # Close the table and HTML body
        html_content += """
          </table>
        </body>
        </html>
        """
        email.attach(MIMEText(html_content,"html")) 
            
        # BUY NOW TARGETS: 
        # Create body of the email: 
        html_content = """\
<html>
<head>
  <title>Buy Now Targets</title>
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid black;
      padding: 8px;
      text-align: left;
    }
  </style>
  <style>
    td.discount-cell-green {
      background-color: rgba(0, 255, 0, 1);
    }
    td.discount-cell-light-green {
      background-color: rgba(0, 255, 0, 0.5);
    }
    td.discount-cell-yellow {
      background-color: rgba(255, 255, 0, 1);
    }
  </style>
</head>
<body>
  <h2>Buy Now Targets</h2>
  <table>
    <tr>
      <th>Item</th>
      <th>Price</th>
      <th>Discount</th>
      <th>Link</th>
    </tr>
"""
        # Add rows dynamically
        for row, value in buyTargDf.iterrows():
            item = buyTargDf.loc[row]["Title"]
            price = buyTargDf.loc[row]["Price"]
            discount = ("%.2f" % round(buyTargDf.loc[row]["Discount"], 2))
            discount_cell_class = "green"
            if(float(discount) >= 50):
                discount_cell_class="discount-cell-green"
            elif(float(discount) >= 35):
                discount_cell_class="discount-cell-light-green"
            else: 
                discount_cell_class="discount-cell-yellow"
            link = buyTargDf.loc[row]["Link"]
            html_content += f"""
            <tr>
              <td>{item}</td>
              <td>{price}</td>
              <td class ={discount_cell_class}>{discount}</td>
              <td><a href="{link}">Link</a></td>
            </tr>
            """

        # Close the table and HTML body
        html_content += """
          </table>
        </body>
        </html>
        """
        email.attach(MIMEText(html_content,"html")) 

        # BEST OFFER TARGETS: 
        # Create body of the email: 
        html_content = """\
<html>
<head>
  <title>Best Offer Targets</title>
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid black;
      padding: 8px;
      text-align: left;
    }
  </style>
  <style>
    td.discount-cell-green {
      background-color: rgba(0, 255, 0, 1);
    }
    td.discount-cell-light-green {
      background-color: rgba(0, 255, 0, 0.5);
    }
    td.discount-cell-yellow {
      background-color: rgba(255, 255, 0, 1);
    }
  </style>
</head>
<body>
  <h2>Best Offer Targets</h2>
  <table>
    <tr>
      <th>Item</th>
      <th>Price</th>
      <th>Discount</th>
      <th>Link</th>
    </tr>
"""
        # Add rows dynamically
        print(offerTargDf)
        for row, value in offerTargDf.iterrows():
            item = offerTargDf.loc[row]["Title"]
            price = offerTargDf.loc[row]["Price"]
            discount = ("%.2f" % round(offerTargDf.loc[row]["Discount"], 2))
            discount_cell_class = "green"
            if(float(discount) >= 50):
                discount_cell_class="discount-cell-green"
            elif(float(discount) >= 35):
                discount_cell_class="discount-cell-light-green"
            else: 
                discount_cell_class="discount-cell-yellow"
            link = offerTargDf.loc[row]["Link"]
            html_content += f"""
            <tr>
              <td>{item}</td>
              <td>{price}</td>
              <td class ={discount_cell_class}>{discount}</td>
              <td><a href="{link}">Link</a></td>
            </tr>
            """

        # Close the table and HTML body
        html_content += """
          </table>
        </body>
        </html>
        """
        email.attach(MIMEText(html_content,"html")) 
        context = ssl.create_default_context()

        for address in emailAddresses:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(myEmail, password)
                smtp.sendmail(myEmail,address,email.as_string())
    print("Email sent successfully")
    
    

# if __name__ == "__main__":
#     items = pd.DataFrame(columns = ["Title", "Price","Discount","Link"])
#     items["Title"]=pd.Series(data=["Anthony volpe"])
#     items["Price"]=pd.Series(data=[10])
#     items["Discount"]=pd.Series(data=[50])
#     items["Link"]=pd.Series(data=["https://www.ebay.com/itm/264963280910?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D260885%26meid%3D3df643734d2e423594572ef6ba8f43af%26pid%3D101875%26rk%3D2%26rkt%3D12%26sd%3D196250216985%26itm%3D264963280910%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedV3MskuWithLambda85KnnRecallV1V2V4ItemNrtInQueryAndCassiniVisualRankerAndBertRecallWithVMEV3CPCAutoWithCassiniEmbRecallManual&_trksid=p4429486.c101875.m1851&itmprp=cksum%3A2649632809103df643734d2e423594572ef6ba8f43af%7Cenc%3AAQAIAAABQKAO6YGL7I8ZT6VFWcHmDuKm898HGH9cNRsnG%252Fep%252BzC3UPHwPSmfpPq3b41cHxht%252FCiwo5DdbtiFsRNqRhAUlK8x2MLrmISu5pnzSn%252FhiW3P7y%252BKcxGllTjL%252BG3bIP4k8fGgzCrVY1dxXbjuBFp3vefxTYgjBXBRUWQBgGciI%252FuQ5Mjsfl%252B%252FiL4cv70dT88jK1pljjSZyaCIIbAW6GYGqwxdGKs4tc%252BjbPOi6oqX393QDbrxGSAbe61t2Q6vT4EDLkQFzUtAWP8shAv5WRmJrn9%252Bbp5m5DNz%252Bfz4w7b21nuEMc3tNTWr%252BZnaTgO16A1mzQ%252BCeYgin1ezKvkbSOT1IbNr3FJ%252FuUn2FPF%252BCuAuI2nuf%252F36%252BG%252BXObkJLy5ljPvNyqnOy4CGg1cNn1GMMENn30D7%252F6yvCMAV1obaSXievLNR%7Campid%3APLP_CLK%7Cclp%3A4429486&itmmeta=01HQE758NAR1Q9QK8QA5XHEAEN"])
#     email(["abby.samson@richmond.edu"], items)