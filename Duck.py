class Duck:
	def talk(self):
		print('Quack,Quack!')
class Dog:
	def talk(self):
		print('Bow,WOW')
	def call_talk(obj):
		obj.talk()
d=Duck()
call_talk(d)
dog=Dog()
call_talk(dog)
