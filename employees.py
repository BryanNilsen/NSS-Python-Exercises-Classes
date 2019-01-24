# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

class Employee:
  def __init__(self, name, job_title, start_date, company):
    self.name = name
    self.job_title = job_title
    self.start_date = start_date
    self.company = company

  def __str__(self):
    return f"{self.name} is a {self.job_title} and started working on {self.start_date}."

# Copy this Company class into your module.
class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def add_employee(self, employee):
      """Returns the employee set with added employee"""
      return self.employees.add(employee)

    def get_employees(self):
      employee_names = []
      for employee in self.employees:
        name_title = f"{employee.name} - {employee.job_title} - Started: {employee.start_date}"
        employee_names.append(name_title)
        """Returns a list of employee names and titles"""
      return ("\n  ").join(employee_names)


    def get_company_name(self):
        """Returns the name of the company"""
        return self.company_name

    def __str__(self):
      return f"====== {self.company_name} =======\nFounded {self.date_founded}\nEmployees:\n  {self.get_employees()}"

# # Add the remaining methods to fill the requirements above


# Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

# Create a company, and three employees, and then assign the employees to the company.

PW = Company("Prestige Worldwide", "January 1st, 2019")

Bryan = Employee("Bryan", "Developer", "March 23rd", "PW")
print(Bryan)

Sebastian = Employee("Sebastian", "Developer", "April 1st", "PW")
print(Sebastian)

Dale = Employee("Dale Doback", "CEO", "May 4th, 1998", "PW")
Brennan = Employee("Brennan Huff", "CEO", "May 4th, 1998", "PW")

PW.add_employee(Bryan)
PW.add_employee(Sebastian)
PW.add_employee(Dale)
PW.add_employee(Brennan)
print(PW)

