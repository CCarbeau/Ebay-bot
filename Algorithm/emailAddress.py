import stripe

products = {"Rookie":"prod_Pp5P4nQMTD30PC", "AS":"prod_PpAhRSfxR0qmZ9", "HOF":"prod_PpAmq5Ijb9XgbF"}

def getEmailAddresses():
    stripe.api_key = "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"
    # stripe.api_key = "sk_test_51OvrCKLyOx9flSI1e6P9SaoZMQvHzwwIH90pIET6dB5cmaDoPWVeLULlAcCewOboFyCoQcTpAlRviv2lFxiYSBCh00w6pMZW6x"
    
    ret = {"Rookie":["christiancarbeau@gmail.com"],"AS":["christiancarbeau@gmail.com"], "HOF":["christiancarbeau@gmail.com","dominicpiz2@gmail.com"]}
    
    subscriptions = stripe.Subscription.list()

    for sub in subscriptions.data:
        customer = sub.customer
        email = stripe.Customer.retrieve(customer).email

        if(sub["plan"].active):
            plan = sub["plan"].product
            if(plan == products["Rookie"]):
                ret["Rookie"].append(email)
            elif(plan == products["AS"]):
                ret["AS"].append(email)
            elif(plan == products["HOF"]):
                ret["HOF"].append(email)
    
    return ret