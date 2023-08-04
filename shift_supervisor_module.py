# shift_supervisor_module.py

from employee_module import ShiftEmployee

class ShiftSupervisor(ShiftEmployee):
    def __init__(self, name, emp_number, shift_number, hourly_pay_rate, annual_salary, annual_production_bonus):
        super().__init__(name, emp_number, shift_number, hourly_pay_rate)
        self.annual_salary = annual_salary
        self.annual_production_bonus = annual_production_bonus

    def get_annual_salary(self):
        return self.annual_salary

    def set_annual_salary(self, annual_salary):
        self.annual_salary = annual_salary

    def get_annual_production_bonus(self):
        return self.annual_production_bonus

    def set_annual_production_bonus(self, annual_production_bonus):
        self.annual_production_bonus = annual_production_bonus

