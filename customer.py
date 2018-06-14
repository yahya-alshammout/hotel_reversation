class Customer():
	customers = []
	def __init__(self, customer_name):
		self.customer_name = customer_name
		for customer in Customer.customers:
			if [customer_name] in Customer.customers:
				return None
		Customer.customers.append([self.customer_name])
		

