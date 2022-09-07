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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoing_numbers = set()
receiving_numbers = set()

count = 0
for t in texts:
    receiving_numbers.add(t[0])
    receiving_numbers.add(t[1])
    count += 2
for c in calls:
    outgoing_numbers.add(c[0])
    receiving_numbers.add(c[1])
    count += 2

telemarketers = []
for n in outgoing_numbers:
    if not n in receiving_numbers:
        telemarketers.append(n)
telemarketers.sort()

print("These numbers could be telemarketers: ")
for n in telemarketers:
    print(n)

