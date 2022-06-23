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
def findDifferentPhones(calls):
    phoneNums = []
    for item in calls :  #O(n)
       inComingPhone = str(item[0]) #O(1)
       inComingPhone=inComingPhone.replace('(','').replace(')','') #O(1)
       sendingPhone = str(item[1]) #O(1)
       sendingPhone=sendingPhone.replace('(','').replace(')','') #O(1)
       if inComingPhone not in phoneNums: #O(1)
          phoneNums.append(inComingPhone ) #O(1)
       if sendingPhone not in phoneNums: #O(1)
        phoneNums.append(sendingPhone )   #O(1) 
    return len(phoneNums) #O(1)
#time complexity is O(n+ 1 + 1+1 +1+1 +1 +1 +1) ~~~~> O(n) , space complexity is O(n)
print(str(findDifferentPhones(calls)))