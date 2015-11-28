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


b = BankAccount(1000, 'ing')
b.depository(56)
b.extract(2000)
print b.total_cash

