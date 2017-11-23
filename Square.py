#Write a python programme to drive a rectange class from SQUARE class claculate are of square and rectangle
class Square:
	def __init__(self,x):
		self.x=x
		def area1(self):
			print('area of square',self.x*self.x)
			class Rectangle(Square):
	def __init__(self,x,y):
		super().__init__(x)
		self.y=y
		def area(self):
			print("Area of rectangle=",self.x*self.y)
			super().area1()
r=Rectangle(10,20)
r.area()