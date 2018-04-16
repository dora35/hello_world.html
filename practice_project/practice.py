class Food(object):
	def __init__(self, name, price, taste):
		self.name = name
		self.price = price
		self.taste = taste
cherry = Food(name ="Cherry", price ="10yuan", taste ="Sweet")	


	
	def get_name(self):
        return self.name + " " + self.price
	
	def get_intro(self):
		message = "The food taste is "
		return message


name = "Cherry"
price = "10yuan"
taste = "Sweet"		
Things_fall_apart = Food(name=name, price=price, taste=taste)
print(Things_fall_apart.get_intro())