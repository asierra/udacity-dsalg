"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
telephone_numbers = set()
count = 0
for t in texts:
    telephone_numbers.add(t[0])
    telephone_numbers.add(t[1])
    count += 2
for c in calls:
    telephone_numbers.add(c[0])
    telephone_numbers.add(c[1])
    count += 2
print("There are {} different telephone numbers in the records.".format(len(telephone_numbers)))
#print(count)


