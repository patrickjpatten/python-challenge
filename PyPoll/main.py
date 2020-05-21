# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Analysis", "pypoll.txt")
#lists to hold the candidates
candidates = []
candidateslist = []
totalvote = 0

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    next(csvreader)
    # Start the problem
    for row in csvreader:
        #count will equal number of votes total
        totalvote = totalvote + 1
        #create a list of all the votes by name
        candidates.append(row[2])
#pulled in this from the internet, but it sets up dictionaries
from collections import Counter
results = Counter(candidates)
dict(results)

print("--------------------")
print("Election Results")
print("--------------------")
print("Total Votes: "+ str(totalvote))
print("--------------------")
#using the dictionary i print out differnt parts in the string and then go back and do it again. 
for key,value in results.items():
        print(key+ " received " +str(value)+" votes or "+str("{:.0%}".format(value/totalvote))+" of the total vote")
print("--------------------")
maxvotes = max(results, key=results.get)
print("The winner of the vote is " + maxvotes)  
print("--------------------")      

with open('pypoll.txt', 'w') as text:
    text.write("--------------------\n")
    text.write("Election Results\n")
    text.write("--------------------\n")
    text.write("Total Votes: "+ str(totalvote)+"\n")
    text.write("--------------------\n")
    text.write("--------------------\n")
    text.write("The winner of the vote is " + maxvotes+"\n")  
    text.write("--------------------\n")  
    for key,value in results.items():
        text.write(key+ " received " +str(value)+" votes or "+str("{:.0%}".format(value/totalvote))+" of the total vote\n")
