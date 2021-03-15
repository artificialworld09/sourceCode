#class Mobile:
#	def __init__(self):
#		print("Mobile constructor called")
#realme = Mobile()


#class Mobile:
#	## constructor without parameter
#	def __init__(self):
#		self.model = "Realme X"
#	def show(self):
#		print("Model: ", self.model)
#realme = Mobile()
#realme.show()



#class Mobile:
#	def __init__(self, m, v=80):
#			self.model = m
#			self.volumn = v
#	def show(self, p):
#			price = p #local variable
#			print(f"Model: {self.model}\nVolumn: {self.volumn}\nPrice: {price}")

## passing argument to constructor
#realme = Mobile("Realme X")

## accessing method from outside class
#realme.show(5000)



#class Mobile:
#	def __init__(self, m, v=80):
#			self.model = m
#			self.volumn = v
#	def show(self, p):
#			price = p #local variable
#			print(f"Model: {self.model}\nVolumn: {self.volumn}\nPrice: {price}")

## passing argument to constructor
#realme = Mobile("Realme X", 90)

## accessing method from outside class
#realme.show(5000)




class Mobile:
	## constructor with parameter
	def __init__(self, m, p):
		self.model = m
		self.price = p
	def show(self):
		print(f"Model: {self.model}\nPrice: {self.price}")
realme = Mobile("Realme X", 5500)
nokia = Mobile("Nokia 3310", 2400)
realme.show()
nokia.show()