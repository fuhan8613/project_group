def cash_on_hand():   
    from pathlib import Path
    import csv

    # Create a file to csv file
    fp = Path.cwd()/"csv_reports/Cash_on_Hand.csv"

    # Read the csv file to append Day and Amount from the csv
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # Skip header

    # Create an empty list to store Day and Amount values
        Cash_on_Hand_Records = []

    # Append Day and Amount values into the Cash_on_Hand_Records list
        for row in reader:
            Cash_on_Hand_Records.append([row[0],row[3]])

    # Create a list that contains the Day from Cash_on_Hand_Records
    Cash_on_Hand_Days = []
    for i in range(len(Cash_on_Hand_Records)):
        Cash_on_Hand_Days.append(Cash_on_Hand_Records[i][0])

    # Create a unique list of Day from Cash_on_Hand_Records
    COH_Days = []
    for i in Cash_on_Hand_Days:
        if i not in COH_Days:
            COH_Days.append(i)

    # Sum up the total Cash on Hand gain/loss for each day
    COH_list = []
    for i in COH_Days:
        COH_sum = 0
        for k in Cash_on_Hand_Records:
            if i == k[0]:
                COH_sum += int(k[1])
        COH_list.append(COH_sum)
    print(COH_list)

    # Calculating the Cash on Hand for each day
    def COHED(ValueED):
        global COH_Each_Day
        COH_Each_Day = []
        COH_ED = 0
        for i in range(len(COH_list)):
            COH_ED += COH_list[len(COH_list)-i-1]
            COH_Each_Day.append(COH_ED)
        print(COH_Each_Day)
        return COH_ED
    COHED(ValueED=0)

    # Calculating the gain/loss in Cash on Hand for each day
    COH_difference = []
    # Create seperate lists for Cash on Hand increment and Cash on Hand deficit
    COH_increment = []
    COH_deficit = [] 
    Count = 0
    for i in range(len(COH_Each_Day)-1):
        Difference = COH_Each_Day[len(COH_Each_Day)-i-1] - COH_Each_Day[len(COH_Each_Day)-i-2]
        if Difference < 0:
            Count += 1
            COH_deficit.append(Difference) # Append Cash on Hand difference to COH_deficit if there is a deficit
        elif Difference > 0:
            COH_increment.append(Difference) # Append Cash on Hand difference to COH_increment if there is an increment
            COH_difference.append(Difference)
    print(COH_difference)

    # Calculating the gain/loss in Cash on Hand for each day
    COH_difference2 = []
    for i in range(len(COH_Each_Day)-1):
        Difference = COH_Each_Day[i] - COH_Each_Day[i+1]
        COH_difference2.append(Difference)
    print(COH_difference2)

    # Print Highest Cash Surplus Day and Amount
    print(f'[HIGHEST CASH SURPLUS] DAY: {COH_difference2.index(-(max(COH_increment)))+1} , AMOUNT: USD{max(COH_increment)}')

    # Print Cash Deficit Day and Amount
    for i in range(len(COH_deficit)):
        print(f'[CASH DEFICIT] DAY: {COH_difference2.index(-COH_deficit[i])+1} , AMOUNT: USD{-COH_deficit[i]}')

    # Write the calculated info to the summary_report.txt file. 
    with open("summary_report.txt","a") as file:
        if Count == 0:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write(f'[HIGHEST CASH SURPLUS] DAY: {COH_difference2.index(-(max(COH_increment)))+1} , AMOUNT: USD{max(COH_increment)}\n')
        else:
            for i in range(len(COH_deficit)):
                file.write(f'[CASH DEFICIT] DAY: {COH_difference2.index(-COH_deficit[i])+1} , AMOUNT: USD{-COH_deficit[i]}\n')
    return()
