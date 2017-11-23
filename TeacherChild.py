#Using the teacher class
from Teacher import Teacher
t=Teacher()
t.setId(10)
t.setName("shekh")
t.setAddress('1-A,Ameerpet,Hyderbad')
t.setSal(100000)

print("ID=",t.getId())
print("NAME=",t.getName())
print("ADDRESS=",t.getAddress())
print("SALARY=",t.getSal())