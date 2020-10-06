#import modules
import os
import csv

#set path for csvfile
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#establishing variables
total_votes = 0
candidates = []
#vote_count = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#open and read csvfile
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    #read each row of data after the data
    for row in csvreader:

        #calculate total num of votes
        total_votes += 1

        #adding canidates to list
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            #print(candidates)

        #adding votes to candidate list
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1 
        else:
            otooley_votes += 1


#calculating percentage for each candidate
percent_khan = khan_votes / total_votes
percent_correy = correy_votes / total_votes
percent_li = li_votes / total_votes
percent_otooley = otooley_votes / total_votes


output = ""
output += (f'')
output += ('Election Results')
output += ('--------------------')
output += (f'Total Votes: {total_votes}')
output += ('--------------------')
output += (f'Khan: {round(percent_khan * 100)}% ({khan_votes})')
output += (f'Correy: {round(percent_correy * 100)}% ({correy_votes})')
output += (f'Li: {round(percent_li * 100)}% ({li_votes})')
output += (f"O'Tooley: {round(percent_otooley * 100)}% ({otooley_votes})")
output += ('--------------------')

print(output)

#print statements
print(f'')
print('Election Results')
print('--------------------')
print(f'Total Votes: {total_votes}')
print('--------------------')
print(f'Khan: {round(percent_khan * 100)}% ({khan_votes})')
print(f'Correy: {round(percent_correy * 100)}% ({correy_votes})')
print(f'Li: {round(percent_li * 100)}% ({li_votes})')
print(f"O'Tooley: {round(percent_otooley * 100)}% ({otooley_votes})")
print('--------------------')

#path to output file
data_output = os.path.join('Analysis', 'pypoll.txt')


with open(data_output, 'w', newline='') as txtfile:
    txtfile.write(output)

