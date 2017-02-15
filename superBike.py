class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	
	def displayinfo(self):
		return "Price:{}, Max Speed:{}, Miles:{}".format(str(self.price), self.max_speed, str(self.miles))


	def ride(self):
		self.miles += 10
		return self 

	def reverse(self):
		self.miles -= 5
		if self.miles <= 0:
			self.miles = 0 
		return self



red_bike = Bike(200, "10mph")

print red_bike.ride().ride().ride().ride().reverse().reverse().reverse()


print red_bike.displayinfo()