class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):	
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		return "Name: {}, Health: {}".format(self.name, self.health)

animal = Animal("peter")

print animal.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

dog = Dog("chippers")

print dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self 

	def displayHealth(self):
		return "This is a dragon!!!! Name: {}, Health: {}".format(self.name, self.health)

dragon = Dragon("Flibert")

print dragon.walk().walk().run().run().fly().fly().fly().displayHealth()