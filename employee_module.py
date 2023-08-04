class Employee:
    def __init__(self, name, emp_number):
        # Initialize data attributes for Employee class
        self.name = name
        self.emp_number = emp_number

    def get_name(self):
        # Accessor method to get employee name
        return self.name

    def set_name(self, name):
        # Mutator method to set employee name
        self.name = name

    def get_emp_number(self):
        # Accessor method to get employee number
        return self.emp_number

    def set_emp_number(self, emp_number):
        # Mutator method to set employee number
        self.emp_number = emp_number


class ShiftEmployee(Employee):
    def __init__(self, name, emp_number, shift_number, hourly_pay_rate):
        # Call the constructor of the base class (Employee) to initialize name and emp_number
        super().__init__(name, emp_number)

        # Initialize additional data attributes for ShiftEmployee class
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        # Accessor method to get shift number
        return self.shift_number

    def set_shift_number(self, shift_number):
        # Mutator method to set shift number
        self.shift_number = shift_number

    def get_hourly_pay_rate(self):
        # Accessor method to get hourly pay rate
        return self.hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        # Mutator method to set hourly pay rate
        self.hourly_pay_rate = hourly_pay_rate
