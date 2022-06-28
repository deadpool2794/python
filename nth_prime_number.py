class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
arr = [i for i in range(2, 100000)]
head = Node(arr[0])
temp = head
for i in arr[1:]:
    temp.next = Node(i)
    temp = temp.next
temp = head
for _ in range(448):
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

# print(prime_arr)
    
# t = int(input())
# for i in range(t):
#     pos = int(input())
#     print(prime_arr[pos-1], end = ' ')