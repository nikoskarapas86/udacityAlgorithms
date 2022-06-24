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
mapper ={}  #O(1)
for getter, reciever, timest, duration in calls:  # O(n)
    if getter not in mapper:  # O(1)
        mapper[getter] = int(duration)  # O(1)
    else:
        mapper[getter] += int(duration)  # O(1)

    # Receiver telephone
    if reciever not in mapper:  # O(1)
        mapper[reciever] = int(duration)  # O(1)
    else:
        mapper[reciever] += int(duration)  # O(1)

print('%s spent the longest time, %s seconds, on the phone during'
      ' September 2016.' % ((max(mapper.items(), key=lambda it: it[1]))[0], (max(mapper.items(), key=lambda x: x[1]))[1]))#O(n)

