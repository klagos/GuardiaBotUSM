import requests

def getAccessToken(token):
	url = "https://graph.facebook.com/v3.3/10157188782874836/accounts?access_token={0}".format(token)
	print(url)
	r = requests.get(url)
	return r.json()["data"][0]["access_token"]

app_properties = open("application.properties")
arch = app_properties.readlines()
access_token = getAccessToken(arch[4].split("=")[1])
print(access_token)