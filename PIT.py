class Individual:
    """An individual who is having only one source of income."""

    def __init__(self, name, income, contract_employee=False, organization_type="Private", children=0):
        self.name = name
        self.income = income
        self.contract_employee = contract_employee
        self.organization_type = organization_type
        self.children = children
        
    def calculate_taxable_income(self):
        """Calculation of tax on deductibles income."""
        deductions = 0
        if self.organization_type == "Government" and not "Private":
            # Government deducts both NPPF and GIS
            deductions += self.income * 0.076  # PF deduction rate of the government as per the taxation rule.
        elif self.contract_employee:
            # Contract employees only have GIS deduction as per the taxation rules.
            deductions += self.income * 0.02  # GIS deduction rate as per the taxation rules.
        else:
            # Standard PF deduction for private/corporate employees as per the taxation rules.
            deductions += self.income * 0.05 # 5% from the basic salary.

        deductions += min(self.children * 350000, self.income * 0.10)  # Deduction for children (Expenses upto Nu.350,000 if biological child and assume 10% deduction if the child is disabled.)

        return max(self.income - deductions, 0)  # Taxable income is should not be non-negative.

    def calculate_tax(self):
        """Calculation of income tax based on income slab of employees."""
        taxable_income = self.calculate_taxable_income()
        tax = 0

        if taxable_income <= 300000:
            pass  # Tax is not calculated below this threshold.
        elif taxable_income <= 400000:
            tax = (taxable_income - 300000) * 0.1 # Tax rate is 10% between Nu.300,001 to Nu.400,000.
        elif taxable_income <= 650000:
            tax = 10000 + (taxable_income - 400000) * 0.15 # Tax rate is 15% between Nu.400,001 to Nu.650,000. 
        elif taxable_income <= 1000000:
            tax = 52500 + (taxable_income - 650000) * 0.2 # Tax rate is 20% between Nu.650,001 to Nu.1,000,000.
        elif taxable_income <= 1500000:
            tax = 130000 + (taxable_income - 1000000) * 0.25 # Tax rate is 25% between Nu.1,000,001 to Nu.1,500,000. 
        else:
            tax = 255000 + (taxable_income - 1500000) * 0.3 # Tax rate is 30% above Nu.1,500,001.

        surcharge = 0
        if tax >= 1000000:
            surcharge = tax * 0.1 # Surcharge of 10% is levied if the income is equal to or more than Nu.1,000,000.

        return tax + surcharge

    def print_tax_summary(self):
        """ Summary of the calculated tax that should be printed."""
        taxable_income = self.calculate_taxable_income()
        tax = self.calculate_tax()
        print(f"Name: {self.name}")
        print(f"Income: Nu. {self.income:,.2f}")
        print(f"Taxable Income: Nu. {taxable_income:,.2f}")
        print(f"Income Tax: Nu. {tax:,.2f}")
        print(f"Surcharge (if applicable): Nu. [surcharge:,.2f]")
        print(f"Total Tax Payable: Nu. [(tax + surcharge):,.2f]")
        
        
def main():
    """ Request the user for input and creates an Individual object."""
    name = input("Enter individual's name: ")
    income = float(input("Enter annual income (Nu.): "))
    contract_employee = input("Is the individual a contract employee (Yes/No)? ").lower() == "Yes"
    organization_type = input("Enter organization type (Government, Private, Corporate): ")
    children = int(input("Enter the number of dependent children (if any): "))

    # The individual object.
    individual = Individual(name, income, contract_employee, organization_type, children)
    
    #Taxable income.
    taxable_income=individual.calculate_taxable_income()
    print('Taxable income is ',taxable_income)
    
    #calculation of tax.
    tax=individual.calculate_tax()
    print(name ,'has to pay total tax of Nu.',tax)
    
    #It prints the summary of the individual object.
    individual.print_tax_summary

if __name__ == "__main__":
    main()
