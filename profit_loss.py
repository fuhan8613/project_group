# This function gives the Highest Net Profit Surplus and the Day or the Profit Deficit and the Day
def profit_loss():
    from pathlib import Path
    import csv

    # Create a file to csv file for Profit and Loss
    fp = Path.cwd()/"csv_reports/Profits_and_Loss.csv"

    # Read the csv file to append Day and Net profit from the csv
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # Skip header

    # Create an empty list to store Day and Net Profit values
        Profits_and_Loss_Records = []

    # Append Day and Net Profit values into the Profits_and_Loss_Records list
        for row in reader:
            Profits_and_Loss_Records.append([row[0],row[4]])

    # Append Net Profit values into Profits_and_Loss_Values list
    Profits_and_Loss_Values = []
    for i in range(len(Profits_and_Loss_Records)):
        Profits_and_Loss_Values.append(Profits_and_Loss_Records[i][1])

    Decreasing_Net_Profit = [] # Create a list to store decreasing net profit values
    Increasing_Net_Profit = [] # create a list to store inreasing net profit values
    Net_Profit_Difference = [] # Create a list to store both increasing and decreasing net profit values from Day 90 to Day 0
    # Calculating difference in net profits
    for i in range(len(Profits_and_Loss_Values)):
        Difference = float(Profits_and_Loss_Values[len(Profits_and_Loss_Values)-i-1]) - float(Profits_and_Loss_Values[len(Profits_and_Loss_Values)-i-2])
        if Difference < 0:
            Decreasing_Net_Profit.append(Difference) # Append net profit to Decreasing_Net_Profit if net profit is decreasing
            Net_Profit_Difference.append(Difference) # Append net profit to Net_Profit_Difference
        elif Difference > 0:
            Increasing_Net_Profit.append(Difference) # Append net profit to Increasing_Net_Profit if net profit is increasing
            Net_Profit_Difference.append(Difference) # Append net profit to Net_Profit_Difference

    Net_Profit_Difference2 = [] # Create a list to store both increasing and decreasing net profit values from Day 0 to Day 90
    Count = 0
    # Calculating difference in net profits
    for i in range(len(Profits_and_Loss_Values)-1):
        Difference = float(Profits_and_Loss_Values[i+1]) - float(Profits_and_Loss_Values[i])
        Net_Profit_Difference2.append(Difference) # Append net profit to Net_Profit_Difference2
        if Difference <= 0:
            Count += 1 # Add to Count if difference in net profits is decreasing
    print(Net_Profit_Difference2)

    # Print Highest Net Profit Surplus Day and Amount
    print(f'[HIGHEST NET PROFIT SURPLUS] DAY: {Net_Profit_Difference2.index(max(Increasing_Net_Profit))+1} , AMOUNT: USD{max(Increasing_Net_Profit)}')

    # Print Profit Deficit Day and Amount
    for i in range(len(Decreasing_Net_Profit)-1):
        print(f'[PROFIT DEFICIT] DAY: {Net_Profit_Difference2.index(Decreasing_Net_Profit[i])+1} , AMOUNT: USD{-Decreasing_Net_Profit[i]}')

    with open("summary_report.txt","a") as file:
        if Count == 0:
            file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write(f'[HIGHEST NET PROFIT SURPLUS] DAY: {Net_Profit_Difference2.index(max(Increasing_Net_Profit))+1} , AMOUNT: USD{max(Increasing_Net_Profit):.2f}\n') # Write the Highest Profit Surplus and the Day to the summary_report.txt file if the profit is always increasing
        else:
            for i in range(len(Decreasing_Net_Profit)-1):
                file.write(f'[PROFIT DEFICIT] DAY: {Net_Profit_Difference2.index(Decreasing_Net_Profit[i])+1} , AMOUNT: USD{-Decreasing_Net_Profit[i]}\n') # Write the Profit Deficit and the Day to the summary_report.txt file if the profit is not always increasing
    return()


    


    
