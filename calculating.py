# Define employment position constants
class EmploymentPosition:
    REGULAR = 1
    CONTRACT = 2

# Define organization type constants
class OrganizationType:
    GOVERNMENT = 1
    PRIVATE = 2
    CORPORATE = 3

# Class to calculate taxable income
class TaxableIncome:
    # Initialize salary, deductions, bonus, number of children, and child education allowance
    def __init__(self, salary, deductions, bonus=0, num_children=0, child_education_allowance=0):
        self.salary = salary
        self.deductions = deductions
        self.bonus = bonus
        self.num_children = num_children
        self.child_education_allowance = child_education_allowance
    
    def calculate(self):
        if self.num_children > 0:
            # Calculate taxable income, ensuring it's not negative
            taxable_income=self.salary + self.bonus - self.deductions - self.child_education_allowance * self.num_children
            return max(taxable_income,0)
        else:
            return self.salary + self.bonus- self.deductions

# Class to calculate personal income tax
class PersonalIncomeTax:
    # Initialize age, taxable income, employment position, organization type, number of children, and child education allowance
    def __init__(self, age, taxable_income, employment_position, organization_type, num_children=0, child_education_allowance=0):
        self.age = age
        self.taxable_income = taxable_income
        self.employment_position = employment_position
        self.organization_type = organization_type
        self.num_children = num_children
        self.child_education_allowance = child_education_allowance
        self.deductions = deductions
        self.bonus = bonus

    def calculate(self):
        # Check if the person is under 18, not liable to pay tax
        if self.age < 18:
            return "Not liable to pay tax as you are under age."
            exit()  # Exit the program if age is below 18

        # Initialize tax to 0
        tax = 0.0

        # Calculate taxable income
        taxable_income = self.taxable_income.calculate()
        
        # Special case for contract employees in government organizations
        if self.employment_position == EmploymentPosition.CONTRACT and self.organization_type == OrganizationType.GOVERNMENT:
            print(f"{self.num_children} child(ren) education allowance: {self.child_education_allowance}")
            taxable_income += self.child_education_allowance
            print(f"As a contract employee in a government organization, GIS and PFF deductions are not allowed for tax deductions.")

        # Calculate tax based on taxable income brackets
        if taxable_income <= 300000:
            tax = 0
        elif taxable_income <= 400000:
            tax = (taxable_income - 300000) * 0.1
        elif taxable_income <= 650000:
            tax = 10000 + (taxable_income - 400000) * 0.15
        elif taxable_income <= 1000000:
            tax = 37500 + (taxable_income - 650000) * 0.2
        elif taxable_income <= 1500000:
            tax = 97500 + (taxable_income - 1000000) * 0.25
        else:
            tax = 197500 + (taxable_income - 1500000) * 0.3

         # Apply surcharge if tax exceeds 1 million
        if tax >= 1000000:
            tax *= 1.1

        # Deduct child education allowance from tax
        if self.num_children > 0:
            tax -= self.child_education_allowance
        
        # Return tax, ensuring it's not negative and formatted to 2 decimal places
        return f"Tax: {max(tax, 0):.2f}"  # Ensure tax is not negative and format to 2 decimal places

# Get employee individual information
name = input("Enter your name: ")
age = int(input(f"Your age: "))

if age < 18:
    print("Not liable to pay tax as you are under age.")
    exit()

employment_position = int(input(f"Enter your employment position, 1=Regular,2=Contract: "))
organization_type = int(input(f"Enter your organization type (1=Government, 2=Private,3=Corporate): "))
salary = float(input(f"Enter your salary per annual: "))
deductions = float(input(f"Enter your total PFF and GIS per annual: "))
bonus = float(input("Enter your bonus per annual: "))

#To qualify for child(ren) education allowance, individual must be married and have school going child(ren)
status = input("Enter your status (Single=1 or Married=2): ")

if status == "2":
    num_children = int(input("Enter the number of children goingf to school: ")) #Only school going ones
    #.Education allowance up to a max of Nu. 350,000 per child.
    child_education_allowance = float(input("Enter the child education allowance per child max 350000: "))
else:
    #IF the individual is single, it means no child and not qualify for child education allowance
    num_children = 0
    child_education_allowance = 0

# Create TaxableIncome and PersonalIncomeTax objects
taxable_income = TaxableIncome(salary, deductions, bonus, num_children, child_education_allowance * num_children)

personal_income_tax = PersonalIncomeTax(age, taxable_income, employment_position, organization_type, num_children, child_education_allowance)

print(personal_income_tax.calculate())
