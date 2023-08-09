# This function gives the Highest Overhead
def overheads():     
     from pathlib import Path
     import csv

     # Create a file to csv file for Overheads
     fp = Path.cwd()/"csv_reports/Overheads.csv"

     # Read the csv file to append Overhead Category and Overhead Value from the csv
     with fp.open(mode="r", encoding="UTF-8", newline="") as file:
          reader = csv.reader(file)
          next(reader) # Skip header

     # Create an empty list to store Overhead Category and Overhead Value
          Overhead_Records = []

     # Append Overhead Category and Overhead Value into the Overhead_Records list
          for row in reader:
               Overhead_Records.append([row[1],row[3]])
          print(Overhead_Records)
          print()

     # Append all Overhead Category to Overhead_Category list
     Overhead_Category = []
     for i in range(len(Overhead_Records)):
          Overhead_Category.append(Overhead_Records[i][0])

     # Append the different types of Overhead Category into a list called OC
     OC = []
     for i in Overhead_Category:
          if i not in OC:
               OC.append(i)
     print(OC)
     print()

     # Create lists to store each type of Overhead Category values
     Human_Resource_Expense = []
     Marketing_Expense = []
     Salary_Expense = []
     Shipping_Expense = []
     Depreciation_Expense = []
     Rental_Expense = []
     Maintenance_Expense = []
     Interest_Expense = []
     Overflow_Expense_Warehouse = []
     Penalty_Expense = []
     Overflow_Expense_Retail = []

     # Create a list to store all the Overhead values
     Total_Overhead_Expense = []

     # Append Overhead Values into their respective Overhead Category lists
     for i in range(len(Overhead_Records)):
          Total_Overhead_Expense.append(float(Overhead_Records[i][1])) # Append all Overhead values into Total_Overhead_Expense list
          if Overhead_Records[i][0] == "Human Resource Expense":
               Human_Resource_Expense.append(float(Overhead_Records[i][1])) # Append Human Resource Expense values into Human_Resource_Expense list
          elif Overhead_Records[i][0] == "Marketing Expense":
               Marketing_Expense.append(float(Overhead_Records[i][1])) # Append Marketing Expense values into Marketing_Expense list
          elif Overhead_Records[i][0] == "Salary Expense":
               Salary_Expense.append(float(Overhead_Records[i][1])) # Append Salary Expense values into Salary_Expense list
          elif Overhead_Records[i][0] == "Shipping Expense":
               Shipping_Expense.append(float(Overhead_Records[i][1])) # Append Shipping Expense values into Shipping_Expense list
          elif Overhead_Records[i][0] == "Depreciation Expense":
               Depreciation_Expense.append(float(Overhead_Records[i][1])) # Append Depreciation Expense values into Depreciation_Expense list
          elif Overhead_Records[i][0] == "Rental Expense":
               Rental_Expense.append(float(Overhead_Records[i][1])) # Append Rental Expense values into Rental_Expense list
          elif Overhead_Records[i][0] == "Maintenance Expense":
               Maintenance_Expense.append(float(Overhead_Records[i][1])) # Append Maintenance Expense values into Maintenance_Expense list
          elif Overhead_Records[i][0] == "Interest Expense ":
               Interest_Expense.append(float(Overhead_Records[i][1])) # Append Interest Expense values into Interest_Expense list
          elif Overhead_Records[i][0] == "Overflow Expense - Warehouse":
               Overflow_Expense_Warehouse.append(float(Overhead_Records[i][1])) # Append Overflow Expense (Warehouse) values into Overflow_Expense_Warehouse list
          elif Overhead_Records[i][0] == "Penalty Expense":
               Penalty_Expense.append(float(Overhead_Records[i][1])) # Append Penalty Expense values into Penalty_Expense list
          elif Overhead_Records[i][0] == "Overflow Expense - Retail":
               Overflow_Expense_Retail.append(float(Overhead_Records[i][1])) # Append Overflow Expense (Retail) values into Overflow_Expense_Retail list
          
     print(Human_Resource_Expense) # Observe Human_Resource_Expense list
     print()
     print(Marketing_Expense) # Observe Marketing_Expense list
     print()
     print(Salary_Expense) # Observe Salary_Expense list
     print()
     print(Shipping_Expense) # Observe Shipping_Expense list
     print()
     print(Depreciation_Expense) # Observe Depreciation_Expense list
     print() 
     print(Rental_Expense) # Observe Rental_Expense list
     print()
     print(Maintenance_Expense) # Observe Maintenance_Expense list
     print()
     print(Interest_Expense) # Observe Interest_Expense list
     print()
     print(Overflow_Expense_Warehouse) # Observe Overflow_Expense_Warehouse list
     print()
     print(Penalty_Expense) # Observe Penalty_Expense list
     print()
     print(Overflow_Expense_Retail) # Observe Overflow_Expense_Retail list
     print()

     # Calculate the percentage for each Overhead Category values and append it to Overhead_Percentage list
     Overhead_Percentage = []
     Human_Resource_Expense_P = (sum(Human_Resource_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Human Resource Expense
     Overhead_Percentage.append(Human_Resource_Expense_P) # Append Human Resource Expense percentage into Overhead_Percentage list
     Total_Marketing_Expense_P = (sum(Marketing_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Marketing Expense
     Overhead_Percentage.append(Total_Marketing_Expense_P) # Append Marketing Expense percentage into Overhead_Percentage list
     Total_Salary_Expense_P = (sum(Salary_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Salary Expense
     Overhead_Percentage.append(Total_Salary_Expense_P) # Append Salary Expense percentage into Overhead_Percentage list
     Total_Shipping_Expense_P = (sum(Shipping_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Shipping Expense
     Overhead_Percentage.append(Total_Shipping_Expense_P) # Append Shipping Expense percentage into Overhead_Percentage list
     Total_Depreciation_Expense_P = (sum(Depreciation_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Depreciation Expense
     Overhead_Percentage.append(Total_Depreciation_Expense_P) # Append Depreciation Expense percentage into Overhead_Percentage list
     Total_Rental_Expense_P = (sum(Rental_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Rental Expense
     Overhead_Percentage.append(Total_Rental_Expense_P) # Append Rental Expense percentage into Overhead_Percentage list
     Total_Maintenance_Expense_P = (sum(Maintenance_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Maintenance Expense
     Overhead_Percentage.append(Total_Maintenance_Expense_P) # Append Maintenance Expense percentage into Overhead_Percentage list
     Total_Interest_Expense_P = (sum(Interest_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Interest Expense
     Overhead_Percentage.append(Total_Interest_Expense_P) # Append Interest Expense percentage into Overhead_Percentage list
     Total_Overflow_Expense_Warehouse_P = (sum(Overflow_Expense_Warehouse) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Overflow Expense (Warehouse)
     Overhead_Percentage.append(Total_Overflow_Expense_Warehouse_P) # Append Overflow Expense (Warehouse) percentage into Overhead_Percentage list
     Total_Penalty_Expense_P = (sum(Penalty_Expense) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Penalty Expense
     Overhead_Percentage.append(Total_Penalty_Expense_P) # Append Penalty Expense percentage into Overhead_Percentage list
     Total_Overflow_Expense_Retail_P = (sum(Overflow_Expense_Retail) / sum(Total_Overhead_Expense)) * 100 # Calculate percentage of the total Overflow Expense (Retail)
     Overhead_Percentage.append(Total_Overflow_Expense_Retail_P) # Append Overflow Expense (Retail) percentage into Overhead_Percentage list
     print(Overhead_Percentage) # Observe Overhead_Percentage list
     print()
     
     # Find the posititon of the highest overhead in Overhead_Percentage list
     Position = Overhead_Percentage.index(max(Overhead_Percentage))
     print(f'[HIGHEST OVERHEAD] {(OC[Position]).upper()}:{max(Overhead_Percentage):.2f}%')

     # Print Highest Overhead into summary_report.txt file
     with open("summary_report.txt","w") as file:
          file.write(f'[HIGHEST OVERHEAD] {(OC[Position]).upper()}:{max(Overhead_Percentage):.2f}%\n')
     return(f'[HIGHEST OVERHEAD] {(OC[Position]).upper()}:{max(Overhead_Percentage):.2f}%\n')

