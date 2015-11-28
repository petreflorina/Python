class BankAccount:

	def __init__(self, total_cash, bank_name):
 		
 		self.total_cash = total_cash
 		self.bank_name = bank_name

 	def depository(self, cash):
 		self.total_cash += cash

 	def extract(self, cash):
 	
 		if cash > self.total_cash:
 			print 'Fonduri insuficiente!'
 		else:
 				self.total_cash -= cash
 	
 	def print_cash(self):
 		print self.total_cash


class Person:

 	def __init__(self, person_name, bank_account, salary=0):

 		self.person_name = person_name
 		self.bank_account = BankAccount(0, 'ing')
 		self.__salary = salary

 	def set_salary(self, value):
 		self.__salary = value
 	
 	def receive_salary(self):

 		print self.__salary
 		self.bank_account.depository(self.__salary)
 		print self.__salary
 		print self.bank_account.print_cash

 	def get_salary(self):
 		print 'Confidential!'

 	salary = property(get_salary)

b = BankAccount(0,'ing')
p = Person('ana',b)
p.set_salary(400)
p.receive_salary
