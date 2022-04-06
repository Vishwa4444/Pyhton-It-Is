class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def about(self,aadhar_no,pan_no):
        print("my name is :"+self.name)
        print("age :       "+str(self.age))
        print("Aadhar no.: "+aadhar_no)
        print("pan no. :   "+pan_no)
p1=Person("Vishwa",21)
p1.about("5316 6018 2896","DXUPA3881F")
