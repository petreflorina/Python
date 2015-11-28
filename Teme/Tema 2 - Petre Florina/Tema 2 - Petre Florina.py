from datetime import date, timedelta
   
class DateRange(object):

	def __init__(self, start, end):

		self.start = start
		self.end = end

	def get_days(self):
		return (self.end - self.start).days

	def contains(self, data):

		if data >= self.start and data <= self.end:
			return True
		else:
			return False

	def anniversary_ok(self, data):

		if data.day >= self.start.day and data.day <= self.end.day:
			if data.month >= self.start.month and data.month <= self.end.month:
				return True
			else:
				return False

	days = property(get_days)


class Car(object):

	def __init__(self, brand, model, daily_price):
		
		self.brand = brand
		self.model = model
		self.daily_price = daily_price
	
	def __str__(self):
		return "Acesta este un " + "{}".format(self.brand) +" "+ "{}".format(self.model) + " si pretul la inchiriere este " + "{}".format(self.daily_price)
   	
   	def get_rental_price(self, period):

		 return period.days * self.daily_price

class Limousine(Car):

    def __init__(self, brand, model, daily_price, driver_salary):
        
        self.driver_salary = driver_salary
        super(Limousine, self).__init__(brand, model, daily_price, )

    def get_rental_price(self, period):

        return (period.days * self.daily_price) + self.driver_salary

class Person(object):

	def __init__(self, first_name, last_name, birthday):

	    self.first_name = first_name
	    self.last_name = last_name
	    self.birthday = birthday


class CarRental(object):

	cars = []

	def add_car(self, car):
		self.cars.append(car)

	def get_cars(self, brand_filter="", price = 0, max_price = 0):

		a = []

		if brand_filter == "" and price == 0 and max_price == 0:
			for elem in self.cars:
				a.append(elem)
			return a

		if brand_filter != "" and price > 0:
			for elem in self.cars:
				if elem.brand == brand_filter and elem.daily_price == price:
					a.append(elem)
			return a
			
		if brand_filter != "" and price == 0:
			for elem in self.cars:
				if elem.brand == brand_filter:
					a.append(elem)
			return a

		if brand_filter == "" and price != 0:
			for elem in self.cars:
				if elem.daily_price == price:
					a.append(elem)
			return a
		if max_price > 0:
			for elem in self.cars:
				if elem.daily_price < max_price:
					a.append(elem)
			return a


	def __str__(self):

		return "cars = {}".format(self.cars)


	def get_price(self, customer, car, period):

		if period.anniversary_ok(customer.birthday):
			return car.get_rental_price(period) - 0.1 * car.get_rental_price(period)
		else:
			return car.get_rental_price(period)


class Point(object):


    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def test(got, expected):
	if got == expected:
	    prefix = ' OK '
	else:
	    prefix = '  X '
	print '{0} got: {1}, expected: {2}'.format(prefix, got, expected)

def main():
    from datetime import date, timedelta
    print "\nTeste pentru clasa DateRange"
    start = date(2012, 6, 24)
    end = date(2014, 1, 1)
    dr = DateRange(start, end)

    test(dr.contains(date(2012, 6, 24)), True)
    test(dr.contains(date(2014, 1, 1)), True)
    test(dr.contains(date(2013, 6, 24)), True)
    test(dr.contains(date(2014, 6, 24)), False)
    test(dr.days, 556)

    print "\nTeste pentru clasa Car"
    c = Car('Volvo', 'S60', 500)
    dr = DateRange(date.today(), date.today()+timedelta(days=7))
    test(c.get_rental_price(dr), 3500)
    test(str(c), "Acesta este un Volvo S60 si pretul la inchiriere este 500")

    print "\nTeste pentru clasa Limousine"
    l = Limousine('Mercedes', 'Diplomat Edition', 1200, 800)
    dr = DateRange(date.today(), date.today()+timedelta(days=3))
    test(l.get_rental_price(dr), 4400)

    print "\nTeste pentru clasa CarRental"
    c2 = Car('Mercedes', 'C-Class', 700)
    cr = CarRental()
    cr.add_car(c)
    cr.add_car(l)
    cr.add_car(c2)

    test(cr.get_cars(), [c, l, c2])
    test(cr.get_cars('Mercedes'), [l, c2])
    test(cr.get_cars('Mercedes', 700), [c2])
    test(cr.get_cars(max_price=600), [c])
    test(cr.get_cars(max_price=400), [])

    p = Person('Jane', 'Geller', date(1992, 12, 5))
    p2 = Person('John', 'Stain', date(1990, 12, 15))
    dr = DateRange(date(2015, 12, 1), date(2015, 12, 10))
    test(cr.get_price(p, c, dr), 4050)
    test(cr.get_price(p2, c2, dr), 6300)

    print "\nTeste pentru clasa Point"
    p1 = Point(1, 2)
    p2 = Point(3, 3)

    p3 = p1 + p2
    test(p3.x, p1.x + p2.x)
    test(p3.y, p1.y + p2.y)

    p3 = p1 - p2
    test(p3.x, p1.x - p2.x)
    test(p3.y, p1.y - p2.y)

if __name__ == '__main__':
    main()