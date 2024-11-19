import os, env, requests

APIKEY =  os.getenv('SECRET_KEY')
CLIENT_ID = os.getenv('CLIENT_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

print("test")

from linkedin_api.clients.restli.client import RestliClient

restli_client = RestliClient()

response = restli_client.get(
  resource_path = "/userinfo",
  access_token = ACCESS_TOKEN
)
#print(response.entity)

response2 = restli_client.finder(
  resource_path="/adAccounts",
  finder_name="search",
  query_params={
    "search": {
      "status": {
        "values": ["ACTIVE", "DRAFT"]
      },
      "reference": {
        "values": ["urn:li:organization:123"]
      },
      "test": True
    }
  },
  version_string="202212",
  access_token= ACCESS_TOKEN
)
ad_accounts = response2.elements

print(ad_accounts)