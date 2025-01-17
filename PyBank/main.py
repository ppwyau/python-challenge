#import csv
import csv
csvpath="Resources\\budget_data.csv"

#calculate total months
total_months=len(data)

#calculate net profit/losses
net_total=sum(int(row[1]) for row in data)

#calculate changes
changes=[int(data[i][1])-int(data[i-1][1])
         for i in range (1, total_months)]
average_change=sum(changes)/len(changes)

#find greatest increase and decrease in profits
greatest_increase=max(changes)
greatest_decrease=min(changes)
greatest_increase_date=data[changes.index(greatest_increase) +1][0]
greatest_decrease_date=data[changes.index(greatest_decrease) +1][0]

#review financial analysis result
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#consolidate result into report.
report=[
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change}",
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})",
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
]
report_str="\n".join(report)
#error with write()in testing, argument must be str, google found "\n" to join list

print(report_str)

with open('financial_analysis.txt','w') as file:
    file.write(report_str)