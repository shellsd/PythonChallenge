# Import Dependencies
import os
import csv

# Set Variables
TotalMonths = 0
Total = 0
PreviousRow = 0
RowChange = 0
TotalChange = 0
AverageChange = 0
MaxIncrease = 0
MaxDecrease = 0
MaxIncreaseMonth = ""
MaxDecreaseMonth = ""
Date = 0
Amount = 1

#Set variables for csv paths 
csvpath = os.path.join('Resources', 'budget_data.csv')
outputpath = os.path.join('Resources', 'Output.txt')

with open(csvpath, newline='') as budget_data:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_data, delimiter=',')
    # Read the header row 
    csv_header = next(csvreader)


    # Loop though rows and perform calcs
    for row in csvreader:

        # Increment Month
        TotalMonths = TotalMonths +1

        # Increment Total
        Total = Total + int(row[Amount])

        # Calculate TotalChange
        RowChange = int(row[Amount]) - PreviousRow
        TotalChange = TotalChange + RowChange
        PreviousRow = int(row[Amount])

        # Calculate MaxIncrease
        if RowChange > MaxIncrease:
            MaxIncrease = RowChange
            MaxIncreaseMonth = row[Date]

        # Calculate MaxDecrease
        if (MaxDecrease > RowChange):
            MaxDecrease = RowChange
            MaxDecreaseMonth = row[Date]

    # Calculate AverageChange 
    if (TotalMonths != 1): 
        AverageChange = round((TotalChange/(TotalMonths -1)), 2)

    # CreateOutput
    Output=(
    "Financial Analysis \n"
    "------------------------------- \n"
    f"Total Months: {TotalMonths} \n"
    f"Total: ${Total} \n"
    f"Average Change: ${AverageChange} \n"
    f"Greatest Increase in Profits: {MaxIncreaseMonth} ({round(MaxIncrease, 0)}) \n"
    f"Greatest Decrease in Profits: {MaxDecreaseMonth} ({round(MaxDecrease, 0)}) \n")


    #Print Output
    print(Output)

    #Create Output File
    with open(outputpath, "w") as OutputFile:
        OutputFile.write(Output)