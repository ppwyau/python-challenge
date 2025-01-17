#import csv
import csv
csvpath="Resources\\election_data.csv"

#read files
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csvheader=next(csvreader)
    data=list(csvreader)

#calculate total votes
total_votes=len(data)

#identify candiates
candidates=list(set(row[2] for row in data))

#calculate votes
vote_counts={candidate: 0 for candidate in candidates}
for row in data:
    vote_counts[row[2]] += 1

#calculate vote percentages
vote_percentages = {candidate: (vote_counts[candidate] / total_votes) * 100 for candidate in candidates}

#identify winner
winner=max(vote_counts, key=vote_counts.get)

#generate report
report = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]
for candidate in candidates:
    report.append(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})")
report.extend([
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------"
])
report_str = "\n".join(report)

print(report_str)

#export report_str to text file
with open('election_results.txt', 'w') as file:
    file.write(report_str)
