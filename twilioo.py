from twilio.rest import Client
from credentials import your_account_sid, your_auth_token, your_cell, your_twilio_number
import requests



# You can find these values from the official Twilio website https://twilio.com/user/account
account_sid = your_account_sid
auth_token = your_auth_token

client = Client(account_sid, auth_token)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

number_iss = people['number']

Message = 'Hi, this is how you use twilio using Python'+str(number_iss)

message = client.messages.create(
	to=your_cell,
	from_=your_twilio_number,
	body=Message
	)
print(message.sid)
