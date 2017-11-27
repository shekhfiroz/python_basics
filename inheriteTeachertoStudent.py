#inherite code from teacher to student
from Teacher import Teacher
class inheriteTeachertoStudent(Teacher):
	def setMarks(self,marks):
		self.marks=marks
	def getMarks(self):
		return marks
