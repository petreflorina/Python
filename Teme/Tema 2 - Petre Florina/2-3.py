

class Car(object):

	def __init__(self, brand, model, daily_price):
		
		self.brand = brand
		self.model = model
		self.daily_price = daily_price
	
	def get_rental_details(self):
		s = "Acesta este un " + str(self.brand) +" "+ str(self.model) + " si pretul la inchiriere este " + str(self.daily_price)
		return s  		

	def get_rental_price(self, period):

		 return (period.days).days * self.daily_price
	
	details = property(get_rental_details) 

class CarRental(object):

	def __init__(self):
		self.cars = []

	def __str__(self):
		return 'self.cars'.format(self.cars) 

	def __repr__(self):
		return self.cars

	def add_car(self, car):
		self.cars.append(car)
		


cr = CarRental()
c = Car('mercedes','40o',400)
cr.add_car(c)
print cr