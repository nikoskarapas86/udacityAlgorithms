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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# space complexity is O(1) constant time complexity
def getFirtAndLastRecord(listOfTexts,listOfCalls):
   firstRecord = listOfTexts[0]
   lastRecord =calls[len(listOfCalls)-1]
   print(lastRecord[2])
   s='''\
... First record of texts, {firstIncoming} texts {firstSending}vat time {firstTimestamp}.
... Last record of calls, {lastIncoming}  calls {lastSending} at time {lastTimestamp}, lasting {duration} seconds\
... '''.format(firstIncoming=str(firstRecord[1]), firstSending=str(firstRecord[0]),firstTimestamp=str(firstRecord[2]),
               lastIncoming =lastRecord[1], lastSending=str(lastRecord[0]),lastTimestamp=str(lastRecord[2]),duration=str(lastRecord[3])
               )
   return s
    


print(getFirtAndLastRecord(texts,calls))
