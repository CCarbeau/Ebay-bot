import stripe

stripe.api_key = "sk_test_51OvrCKLyOx9flSI1e6P9SaoZMQvHzwwIH90pIET6dB5cmaDoPWVeLULlAcCewOboFyCoQcTpAlRviv2lFxiYSBCh00w6pMZW6x"

test = stripe.checkout.Session.create(
  success_url="https://kryptoscards.com",
  line_items=[{"price": "price_1OzggiLyOx9flSI1bomDOYA9", "quantity": 2}],
  mode="subscription",
)

print(test["url"])