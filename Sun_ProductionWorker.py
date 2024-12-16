from Sun_Employee import Employee
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate
        
    def get_shift_number(self):
        return self.__shift_number
    
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
        
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate
        

# create an object of the ProductionWorker class
name = input("Enter employee name: ")
number = input("Enter employee number: ")
shift_number = int(input("Enter shift number (1 for day, 2 for night): "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))

worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)

# display the data using the accessor methods
print("Employee name:", worker.get_name())
print("Employee number:", worker.get_number())
if worker.get_shift_number() == 1:
    print("Shift: Day")
else:
    print("Shift: Night")
print("Hourly pay rate:", worker.get_hourly_pay_rate())