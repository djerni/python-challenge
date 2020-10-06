#Import modules
import os 
import csv

#set path for csvfile
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#establishing variables
totalMonths = 0
netAmount = 0
#averageChange =
greatestIncrease = 0
greatestDecrease = 0


#Open and read csvfile
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 
    print(csv_header)
    firstRow = next(csvreader)
    #Calculate total months
    totalMonths += 1
    #Calculate total amount
    netAmount = netAmount + int(firstRow[1])
    #Calculate avg change
    averageChange = netAmount / totalMonths

      # Read each row of data after the header
    for row in csvreader:

        print(row)

        totalMonths = totalMonths + 1

        netAmount += int(row[1])
        

output = ""
output += (f'')
output += ('Financial Analysis')
output += ('-------------------------')
output += (f'Total Months: {totalMonths}')
output += (f'Net Amount: ${netAmount}')

print(output)



#print statements
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {totalMonths}')
print(f'Net Amount: ${netAmount}')


#path to output file
data_output = os.path.join('Analysis', 'pypbank.txt')


with open(data_output, 'w', newline='') as txtfile:
    txtfile.write(output)