from twilio.rest import Client
hotels_list = []
customers_list = []
reservation_list = []
def add_hotel(number, hotel_name, city, total_rooms, empty_rooms):
	for hotel in hotels_list:
		if hotel[1] == hotel_name:
			return "the hotel in list"
	hotels_list.append([number, hotel_name, city, total_rooms,
		empty_rooms])
	return hotel_name
def add_customer(customer_name):
	for customer in customers_list:
		if customer == customer_name:
			return "the customer in list"
	customers_list.append([customer_name])
	return customer_name
def reserve_room(hotel_name, customer_name, mobile):
	for name_hotel in hotels_list:
		if name_hotel[1] == hotel_name :
			if name_hotel[4] == 0:
				return "sorry no rooms available"
			else:
				reservation_list.append([hotel_name, customer_name, mobile])
				name_hotel[4] -= 1
				return "confirmation"

def send_text_message(messege, mobile):
	account_sid = 'AC216e909db0a5397974838b688bc264a5'
	auth_token = '0738be85785d827bcab50b8c2f908381'
	client = Client(account_sid, auth_token)

	message = client.messages.create(
		body = message,
		from_ = '+13158885133',
		to = mobile)
	print message.sid


def add_new_reservation(hotel_name, customer_name, mobile):
	if reserve_room(hotel_name, customer_name, mobile) == "confirmation":
		send_text_message("confirmation", mobile)
		print "confirmation"
	else:
		print "no rooms available"

def list_hotels_in_city(city_name):
	x = 0
	for name_city in hotels_list:
		if city_name in name_city:
			print hotels_list[x][1] + " " + str(hotels_list[x][4])
		x += 1

def list_reservation_in_hotel(hotel_name):
	y = 0
	for reservation in reservation_list:
		if hotel_name in reservation:
			print reservation_list[y][1]
		y += 1
add_hotel(1, "sraya", "Aqaba", 250, 50)
add_hotel(2, "royal", "Amman", 300, 60)
add_hotel(3, "dalas", "Amman", 200, 0)
print reserve_room("royal", "hassan", "+962779148786")
#print reserve_room("dalas", "mohammad")
#print reserve_room("sraya", "ahmad")
#list_hotels_in_city("Amman")
#list_hotels_in_city("Aqaba")
#list_hotels_in_city("Irbid")
#list_reservation_in_hotel("sraya")
#list_reservation_in_hotel("dalas")
#list_reservation_in_hotel("royal")





