# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Analysis", "pybank.txt")
#create lists to hold the data
dates = []
monthly_changes = []

#place to hold months
count = 0
total_profit = 0
# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    next(csvreader)
    # Start the problem
    for row in csvreader:
        count = count + 1
        monthly_changes.append(int(row[1]))
        total_profit = total_profit + int(row[1])
        avg_change_profit = round(total_profit/count,2)
        #create a list of dates
        dates.append(str(row[0]))
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
        increase_date = dates[monthly_changes.index(greatest_increase_profits)]
        decrease_date = dates[monthly_changes.index(greatest_decrease_profits)]
Format_total_profit = "{:,}".format(total_profit)
Format_avg_change_profit = "{:,.2f}".format(avg_change_profit)
Format_inc_prof = "${:,}".format(greatest_increase_profits)
Format_dec_prof = "${:,}".format(greatest_decrease_profits)


print("--------------------------------")
print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(count))
print("Total Profits: $" + str(Format_total_profit))
print("Average Change: $"+str(Format_avg_change_profit))
print("Greatest Increase in Profits: " + (str(increase_date))+ " " + str(Format_inc_prof))
print("Greatest Increase in Profits: " + (str(decrease_date))+ " " + str(Format_dec_prof))

with open('pybank.txt', 'w') as text:
    text.write("--------------------------------\n")
    text.write("Financial Analysis\n")
    text.write("--------------------------------\n")
    text.write("Total Months: " + str(count)+"\n")
    text.write("Total Profits: $" + str(Format_total_profit)+"\n")
    text.write("Average Change: $"+str(Format_avg_change_profit)+"\n")
    text.write("Greatest Increase in Profits: " + (str(increase_date))+ " " + str(Format_inc_prof)+"\n")
    text.write("Greatest Increase in Profits: " + (str(decrease_date))+ " " + str(Format_dec_prof)+"\n")



