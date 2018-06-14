from hotel import Hotel
from customer import Customer
from reservations import Reservation
from notification import Notification 
class Tester():

	hotel1 = Hotel(1, "Rotana", "Amman", 300, 50)
	hotel12 = Hotel(2, "Royal", "Amman", 250, 35)
	print hotel1.hotels
	print hotel1.list_hotels_in_city()

	customer1 = Customer("Yahya")
	print customer1.customers

	reservation1 = Reservation("Rotana", "Yahya", "+962779148786")
	messeag1 = Notification("confirmation", "+962779148786")
	print messeag1.send_message()
	print reservation1.reserve_room()
	print reservation1.reservation_list_in_hotel()
Tester()




