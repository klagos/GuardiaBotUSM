import requests

app_properties = open("application.properties")
access_token = app_properties.readlines()[0].split("=")[1]

while True:
	message = input("Mensaje a postear: ")
	data = {'message': message, 'access_token': access_token}
	r = requests.post("https://graph.facebook.com/278468619769380/feed", data)
	print(r.status_code, r.reason)
