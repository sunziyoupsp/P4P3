from Sun_Employee import Employee
class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, annual_production_bonus):
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__annual_production_bonus = annual_production_bonus
        
    def get_annual_salary(self):
        return self.__annual_salary
    
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary
        
    def get_annual_production_bonus(self):
        return self.__annual_production_bonus
    
    def set_annual_production_bonus(self, annual_production_bonus):
        self.__annual_production_bonus = annual_production_bonus
        

# create a ShiftSupervisor object
name = input("Enter shift supervisor name: ")
number = input("Enter shift supervisor number: ")
annual_salary = float(input("Enter annual salary: "))
annual_production_bonus = float(input("Enter annual production bonus: "))

supervisor = ShiftSupervisor(name, number, annual_salary, annual_production_bonus)

# display the object's attributes
print("Shift supervisor name:", supervisor.get_name())
print("Shift supervisor number:", supervisor.get_number())
print("Annual salary:", supervisor.get_annual_salary())
print("Annual production bonus:", supervisor.get_annual_production_bonus())