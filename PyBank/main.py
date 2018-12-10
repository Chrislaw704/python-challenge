#Pybank challenge
import os
import csv


#csvpath = os.path.join('..', 'Resources', 'accounting.csv')
csvpath = os.path.join('budget_data.csv')

# Store the file path associated with the file (note the backslash may be OS specific)
budgetfile = 'budget_data.csv'

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header and print the row
    for row in csvreader:
        print(row)
    
    #number of lines variable defined
    numberoflines = sum(1 for line in open(budgetfile))

    #return number of lines to print the total of months
    print('')
    print('Financial Analysis')
    print('------------------')
    print(numberoflines)
    print('months')

    #Formula for total:  sum of entire column
    netprofitandlosses = sum 
    
    #Net amount of Profit/Losses over period

    #Average change in Profit/Losses between months over the period

    #The greatest increase in profits (date and amount) over the period

    #The greatest decrease in losses (date and amount) over the entire period




