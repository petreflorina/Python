class Car(object):

    def __init__(self, brand, model, daily_price):
        
        self.brand = brand
        self.model = model
        self.daily_price = daily_price
    
    def __str__(self):
        return "Acesta este un " + "{}".format(self.brand) +" "+ "{}".format(self.model) + " si pretul la inchiriere este " + "{}".format(self.daily_price)
        
    def get_rental_price(self, period):

         return (period.days).days * self.daily_price
    


"""
Ex. 5
Definiți clasa CarRental cu atributele: cars. Scrieți metodele:
    - add_car(car) - adaugă o mașină în centrul de închirieri
    - get_cars - returnează o listă cu mașinile filtrate după brand și preț
    maxim.
    - get_price(customer, car, period) - returnează prețul final al tranzacției.
      Dacă ziua de naștere a clientului este în intervalul închirierii, se
      aplică o reducere de 10%.

"""


class CarRental(object):

    cars = []

    def add_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        

