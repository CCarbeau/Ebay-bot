import json
import requests
import base64 

def getToken():
    credential_file = open("config.json","r")
    creds = json.load(credential_file)
    production_login_endpoint = "https://api.ebay.com/identity/v1/oauth2/token"

    ci_cs = "Christia-search-PRD-baea55215-54624b13:PRD-aea55215cf88-b713-4a4d-9f3d-1968"
    encode = ci_cs.encode()
    auth = base64.b64encode(encode).decode()
    
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic '+auth,
    }
    scopes = "https://api.ebay.com/oauth/api_scope"
    data = {
        "grant_type":"client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }

    response = requests.post(production_login_endpoint, headers=headers, data=data).json()

    return response["access_token"]