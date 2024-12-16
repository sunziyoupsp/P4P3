class Pet:
    def __init__(self,name,type,age):
        self.__name = name
        self.__type = type
        self.__age = age
    
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type
    
    def getAge(self):
        return self.__age
    
    def setName(self,name):
        self.__name = name

    def setType(self,type):
        self.__type = type
    
    def setAge(self,age):
        self.__age = age

name = input("Enter the pet name: ")
type = input("Enter the pet's type: ")
age = input("Enter the pet's age: ")

pet1 = Pet(name,type,age)
print()
print("The pet's name",pet1.getName())
print("The pet's type is",pet1.getType())
print("The pet's age is",pet1.getAge())

        