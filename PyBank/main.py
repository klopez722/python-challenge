print("Financial Analysis")
print("------------------------")

#import modules
import os
import csv


csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    cvsheader = next(csvreader)
    
    Total_months = []
    net_total = []
    change = []
    
    for row in csvreader:
        Total_months.append(row[0])
        net_total.append(int(row[1]))
    
    for i in range(len(net_total)-1):
        change.append(net_total[i+1]-net_total[i])
                      
#determine greatest increase/decrease
increase = max(change)
decrease = min(change)
greatest_increase = change.index(max(change))+1
greatest_decrease = change.index(min(change))+1


#print results
print(f"Total Months:{len(Total_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: ${round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {Total_months[greatest_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {Total_months[greatest_decrease]} (${(str(decrease))})")  
   
#tarsnfer results to txt file
txt= open("Results.txt", "w")
txt.write("Financial Analysis" + "\n")
txt.write("------------------------" + "\n")
txt.write(f"Total Months:{len(Total_months)}"+ "\n")
txt.write(f"Total: ${sum(net_total)}" + "\n")
txt.write(f"Average Change: ${round(sum(change)/len(change),2)}" + "\n")
txt.write(f"Greatest Increase in Profits: {Total_months[greatest_increase]} (${(str(increase))})" + "\n")
txt.write(f"Greatest Decrease in Profits: {Total_months[greatest_decrease]} (${(str(decrease))})" + "\n")


