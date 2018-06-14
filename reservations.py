from hotel import Hotel
from customer import Customer
class Reservation():
	reservations_list = []
	def __init__(self, hotel_name, customer_name, mobile):
		self.hotel_name = hotel_name
		self.customer_name = customer_name
		self.mobile = mobile

	def reserve_room(self):
		i = 0
		for reserve in Hotel.hotels:
			if self.hotel_name in reserve:
				if Hotel.hotels[i][4] == 0:
					return "sorry no rooms"
				else:
					Reservation.reservations_list.append([self.hotel_name,
						self.customer_name, self.mobile])
					Hotel.hotels[i][4] -= 1
					return "confirmation"
			i += 1

	def reservation_list_in_hotel(self):
		reservation_list = []
		x = 0
		for hotel in Reservation.reservations_list:
			if self.hotel_name in hotel:
				reservation_list.append(Reservation.reservations_list[x][1])
			x += 1
		return reservation_list




