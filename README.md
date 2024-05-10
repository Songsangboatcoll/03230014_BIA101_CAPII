#BIA101 CAP II
#PIT(Personal Income Tax) CALCULATOR

##Submisssion by Chandri Maya Subba, 03230014

#ASSUMPTIONS to be considered in this assignment:
1. Assume individuals have only one source of income, namely Salary.

2. Incorporate functionality to discern between Contract and Regular employee positions within organisations. Note: Government organisations typically do not offer pension(PF) schemes to contract employees, whereas certain corporations and private entities do.

3. Integrate functionality to account for different types of organisations where individuals are employed, such as Government, Private, and Corporate sectors.

Deductibles:
NPPF: Deductible for Pension Scheme/Provident Fund (PF).
Tax deductions for children, whether they are in school or not.
GIS: Deductible for Group Insurance Scheme.


#My understanding of the assumptions given for instructions:
1. Individuals have only one source of income, namely salary: This assumption simplifies the model 
but might not reflect real-world scenarios where individuals may have multiple sources of income. However, 
for the sake of simplicity and focusing on the core logic, we'll proceed with this assumption.


2. Discern between contract and regular employee positions: Differentiating between contract and regular 
employee positions is important for handling deductions such as Pension Scheme/Provident Fund (PF). 
Since government organizations do not offer PF to contract employees, we need to incorporate logic to handle 
this distinction. One way to achieve this is by introducing a field in the EmploymentIncome class to denote the 
type of employment (contract or regular). Then, when calculating deductions, we can apply PF deductions only for 
regular employees.


3. Account for different types of organizations: To accommodate different types of organizations (government, 
private, corporate), we can introduce an Organization class or enum with different organization types. Then, 
when calculating taxes or deductions, we can consider the organization type to apply relevant rules or exemptions 
specific to each type.


4. Deductibles (NPPF, GIS): NPPF (Pension Scheme/Provident Fund) and GIS (Group Insurance Scheme) are 
deductible contributions that individuals make towards their retirement and insurance, respectively. 
These deductions should be accounted for when calculating taxable income. We can create fields in the 
Deductions class to represent these contributions, and when calculating taxes, subtract them from the 
total income to arrive at the taxable income.

#Specific deductions from salary income is Less PF and GIS contributions and in addition general exemption should be considered as below:
a.Education allowance up to a max of Nu. 350,000 per child.
b.Life insurance premium.
c.Self education allowance up to a max Nu. 350,000 per taxpayer.
d.Donations up to a max of 5% of the total adjusted gross income.
e.Sponsored children education expense up to max of Nu. 350,000 per child.

PIT Tax Rates: 
Sl No. :	Income Slab	Tax Rate
1	Up to Nu. 300,000	                   0%
2	Nu.300,001 to Nu. 400,000	           10%
3	Nu. 400,001 to Nu. 650,000	           15%
4	Nu. 650,001 to Nu. 1,000,000	       20%
5	Nu. 1,000,001 to Nu. 1,500,000	       25%
6	Nu. 1,500,001 and up	               30%
Surcharge at the rate of 10% shall be levied on (PIT)	Personal Income Tax, if the annual Personal Income Tax	is equal to or more than Nu. 1,000,000.

#The 10% of the taxable income is allowed for bonus allowances and 2% of the GIS and PFF is allowed for deduction in tax calculations.

#Formula: Personal Income Tax= Taxable income from salary -(NPPF+GIS+Tax deductions for children education+ allowances)

#References
