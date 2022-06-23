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
#time complexity is O(n) while space complexity is O(1)
def findLongestCall(calls): 
    longestPhone =[]
    for item in calls:
        if len(longestPhone) == 0 or item[3] > longestPhone[3]:
            longestPhone =item
    s = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(str(longestPhone[0]),str(longestPhone[3]))
    return s


print(findLongestCall(calls))
