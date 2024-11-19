import os, env, requests

APIKEY =  os.getenv('SECRET_KEY')
CLIENT_ID = os.getenv('CLIENT_ID')

print("test")

from linkedin_api.clients.restli.client import RestliClient

restli_client = RestliClient()

response = restli_client.get(
  resource_path = "/userinfo",
  access_token = "AQUU2C5deKhB8O48eq-T1Vj7dv2vKLcvUZCHG2PicPXeohuQAB_27Mb_8ONet8anwYIDqD3-Jew9ETgLYM7tz9oVlinvvtEzSpxPYwt30q2bAmJMUsMUNfMlFTmvLsoErMNVjTU7Wu1IUfTeT4n5vFi3XITu_ZYBy-eIla_aU46rshNO-6lHu7mdWujO25oOyjqwUbbdkmqLbe17TH7F_F7zmrm1DKvjMv2Cl1iXhafywIoYDoTl7spXQJZOKb043tuxBd7_ukPQS9DkcOtKeeQe9DFfudzA9b7osZGzqfuC60hFvEvgMqFi75fKgPPJyZ6Iek9_uOX-WgRnHkHJlXL3wMJ7bQ"
)
print(response.entity)