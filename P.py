#Oder of the object
class A(object):
    def method(self):
        print("A")
        super().method()
class B(object):
    def method(self):
        print("B")
        super().method()
        
class C(object):
    def method(self):
        print("C")
        super().method()
        
class X(A,B):
    def method(self):
        print('X')
        super().method()
        
class Y(B,C):
    def method(self):
        print('Y')
        super().method()
class P(X,Y,C):
    def method(self):
        print('P')
        super().method()
        
obj=P()
obj.method()

P.mro() #MRO is static method so class name with method name HOw to call MRO Method to get the order 
print(P.mro())