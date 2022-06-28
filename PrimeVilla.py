from datetime import datetime,timedelta

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head = Node(2)
temp = head
for i in range(3, 50000):
    temp.next = Node(i)
    temp = temp.next
temp = head
for _ in range(225):
    prev = temp
    curr = prev.next
    a = prev.data
    while True:
        try:
            curr = prev.next
            if curr.data % a == 0:
                prev.next = curr.next
            prev = prev.next
        except:
            break
    temp = temp.next
    
temp = head
prime_arr = []
while True:
    try:
        prime_arr.append(temp.data)
        temp = temp.next
    except:
        break


date, day, n = input().split()
n = int(n)
date = datetime.strptime(date, "%Y%m%d")
days = timedelta(days = 5)
date_day = date.strftime("%a")
if date_day == day:
    print('NO', 0)
else:
    for i in prime_arr:
        days = timedelta(days = i)
        next_date = date + days
        next_day = next_date.strftime('%a')
        month = next_date.strftime('%m')
        month = int(month)
        if month in [2,3,5,7,11]:
            if next_day == day:
                if int(n) > i:
                    print("YES", i)
                else :
                    print("NO", i)
                break

    