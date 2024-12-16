class Person:
    def __init__(self, name, address, email):
        self.__name = name
        self.__address = address
        self.__email = email
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address
        
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email