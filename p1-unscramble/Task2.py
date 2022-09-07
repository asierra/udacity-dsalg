"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Find the longest time
call_index = 0
total_time = 0
for i in range(len(calls)):
    t = int(calls[i][3])
    
    if t > total_time:
        total_time = t
        call_index = i 

longest_time_number = calls[call_index][0]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_time_number, total_time))
