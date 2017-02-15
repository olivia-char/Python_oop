class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

		if self.price >= 10000:
			self.tax = .15
		else:
			self.tax = .12

	def display_all(self):
		return "Price: {}, Speed: {}, Fuel: {}, Mileage: {}, Tax:{}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(11000, 55, 30, 100000)
print car1.display_all()
car2 = Car(1000, 5, 70, 18000)
print car2.display_all()
car3 = Car(11000, 35, 30, 80000)
print car3.display_all()
car4 = Car(700, 45, 30, 90000)
print car4.display_all()
car5 = Car(20000, 55, 30, 67000)
print car5.display_all()
car6 = Car(99000, 25, 30, 70000)
print car6.display_all()