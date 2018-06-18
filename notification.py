from twilio.rest import Client
class Notification():
	def __init__(self, messege, mobile):
		self.messege = messege
		self.mobile = mobile

	def send_text_message(self):
		account_sid = 'AC216e909db0a5397974838b688bc264a5'
		auth_token = '0738be85785d827bcab50b8c2f908381'
		client = Client(account_sid, auth_token)
		message = client.messages.create(
			body = messege,
			from_ = '+13158885133',
			to = mobile)
		message.sid



