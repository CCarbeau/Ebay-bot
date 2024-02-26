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
def email(emailAddresses,targets):
    if(targets.size != 0):
        myEmail ="christiancarbeau@gmail.com"
        password = "ezcx vfwc sbae ohpk"

        time = datetime.now().strftime("%m/%d/%y %H:%M")
        
        subject = time + " Targets:"
        
        email = MIMEMultipart("mixed")
        email["From"]=myEmail
        email["Subject"]=subject
        
        # Create body of the email: 
        header = """\
<html>
  <body>
    <table>
      <tr>
        <th style="width:70%"><b>Item:</b></th>
        <th><b>Price:</b></th>
        <th><b>Discount:</b></th>
        <th><b>Link:</b></th>
      </tr>
    </table>
  </body>
</html>
"""
        email.attach(MIMEText(header,"html"))
        for row, value in targets.iterrows():
            item = targets.loc[row]["Title"]
            price = targets.loc[row]["Price"]
            discount = targets.loc[row]["Discount"]
            link = targets.loc[row]["Link"]
            
            linkHTML= f"""\
<html>
  <body>   
    <tr>
        <td style="width:70%">{item}</td>
        <td>{price}</td>
        <td>{discount}</td>
        <td><a href="{link}">Link</a></td>
      </tr>
  </body>
</html>
"""
            email.attach(MIMEText(linkHTML,"html")) 
            
        
        context = ssl.create_default_context()

        for address in emailAddresses:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(myEmail, password)
                smtp.sendmail(myEmail,address,email.as_string())
    
    

if __name__ == "__main__":
    items = pd.DataFrame(columns = ["Title", "Price","Discount","Link"])
    items["Title"]=pd.Series(data=["Anthony Volpe Bowman Chrome 1st"])
    items["Price"]=pd.Series(data=[10])
    items["Discount"]=pd.Series(data=[50])
    items["Link"]=pd.Series(data=["https://www.ebay.com/itm/264963280910?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D260885%26meid%3D3df643734d2e423594572ef6ba8f43af%26pid%3D101875%26rk%3D2%26rkt%3D12%26sd%3D196250216985%26itm%3D264963280910%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedV3MskuWithLambda85KnnRecallV1V2V4ItemNrtInQueryAndCassiniVisualRankerAndBertRecallWithVMEV3CPCAutoWithCassiniEmbRecallManual&_trksid=p4429486.c101875.m1851&itmprp=cksum%3A2649632809103df643734d2e423594572ef6ba8f43af%7Cenc%3AAQAIAAABQKAO6YGL7I8ZT6VFWcHmDuKm898HGH9cNRsnG%252Fep%252BzC3UPHwPSmfpPq3b41cHxht%252FCiwo5DdbtiFsRNqRhAUlK8x2MLrmISu5pnzSn%252FhiW3P7y%252BKcxGllTjL%252BG3bIP4k8fGgzCrVY1dxXbjuBFp3vefxTYgjBXBRUWQBgGciI%252FuQ5Mjsfl%252B%252FiL4cv70dT88jK1pljjSZyaCIIbAW6GYGqwxdGKs4tc%252BjbPOi6oqX393QDbrxGSAbe61t2Q6vT4EDLkQFzUtAWP8shAv5WRmJrn9%252Bbp5m5DNz%252Bfz4w7b21nuEMc3tNTWr%252BZnaTgO16A1mzQ%252BCeYgin1ezKvkbSOT1IbNr3FJ%252FuUn2FPF%252BCuAuI2nuf%252F36%252BG%252BXObkJLy5ljPvNyqnOy4CGg1cNn1GMMENn30D7%252F6yvCMAV1obaSXievLNR%7Campid%3APLP_CLK%7Cclp%3A4429486&itmmeta=01HQE758NAR1Q9QK8QA5XHEAEN"])
    email(["cikoticz24@gmail.com"], items)