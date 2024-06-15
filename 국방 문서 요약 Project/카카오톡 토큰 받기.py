import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "	b90bcd4487987b6694eaed507e2f0859",
    "redirect_uri" : "https://localhost.com",
    "code"         : 'Z3DlnEBnJK-okRansYU-1sjP-G3PB7i8VgOGa1Rho6NVsDwjCMnr8lRL1mMKPXOaAAABjUorHNGoblpFv_zasg'
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)