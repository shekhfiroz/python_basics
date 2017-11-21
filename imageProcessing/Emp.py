class Emp():
	def  __init__(self,n='',m[]):
		self.name=n
		self.marks=m
	def calculate(self):
		print('Your name:',self.name)
		sum_of_marks=sum(self.marks)
		print("Total Marks=",sum_of_marks)
		avg=sum_of_marks/len(self.marks)
		print("Average marks",avg)
s1=Emp()
s1.calculate('firoz',[9,8,7,6,5,4,3,2,1])