""" the hotel class """
class Hotel():
	hotels = []
	def __init__(self, number, hotel_name, city, total_rooms, empty_rooms):
		self.number = number
		self.hotel_name = hotel_name
		self.city = city
		self.total_rooms = total_rooms
		self.empty_rooms = empty_rooms
		for hotel in Hotel.hotels:
			if [number,hotel_name,city,total_rooms,empty_rooms] in Hotel.hotels:
				return None
		
		Hotel.hotels.append([self.number, self.hotel_name, self.city,
			 	self.total_rooms, self.empty_rooms])

			 

	def list_hotels_in_city(self):
		list_hotel = []
		i = 0
		for hotel in Hotel.hotels:
			if self.city in hotel:
				list_hotel.append(Hotel.hotels[i][1] + " " + str(Hotel.hotels[i][4]))
			i += 1
		return list_hotel





		               
	