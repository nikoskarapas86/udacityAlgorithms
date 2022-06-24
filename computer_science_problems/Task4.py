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

#time complexity is O(n+n+n+n+n+1+1+nlogn) ----> O(nlogn )   space compexity is O(n)
outgoingCalls =[call[0] for call in calls] #O(n)
inGoingCalls =[call[1] for call in calls] #O(n)
sendingtexts =[text[0] for text in texts] #O(n)
receivingtexts =[text[1] for text in texts] #O(n)
telemarketers =[] #O(1)

for phone in outgoingCalls:#O(n)
    if phone not in inGoingCalls and phone not in sendingtexts and phone not in receivingtexts:
        telemarketers.append(phone)#O(1)
        
telemarketers=sorted(set(telemarketers))#O(nlogn)
for telemarket  in telemarketers:#O(n)
    print(telemarket)


