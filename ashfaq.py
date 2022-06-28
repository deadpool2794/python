# s = sys.argv[1]
# d = {}
# l = list(range(65, 91))
# l += list(range(97, 123))

# for ind,i in enumerate(s):
#     if ord(i) not in l:
#         d[ind] = i
# s = list(s)[::-1]
# for i in d:
#     s[i] = d[i]
# print(''.join(s))

# s = sys.argv[1]
# s = s.split('_')
# d = {}
# for i in s:
#     i.lower()
#     d[i] = len(i)
# mx = max(d.values())
# arr = []
# for i in d:
#     if d[i] == mx:
#         arr.append(i)
# arr.sort()
# print('_'.join(arr))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# n = int(sys.argv[1])
# head = Node(1)
# temp = head
# for i in range(2, n+1):
#     temp.next = Node(i)
#     temp = temp.next
# temp.next = head
# temp = head
# arr = []
# while(True):
#     if len(arr) == n-1:
#         break
#     arr.append(temp.next.data)
#     temp.next = temp.next.next
#     temp = temp.next
# print(temp.data)


# n = int(input())
# tot = 0

# for i in range(2, n+1):
#     tot += n // i
# print(tot)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None



# n = int(input())
# s = input()
# k = int(input())
# vowels = [ 'a', 'e', 'i', 'o', 'u']
# vow, con, coins  = 0, 0, 0
# ind_con , ind_vow = [], []


# for ind,i in enumerate(s):
#     if i in vowels:
#         vow += 1
#         ind_vow.append((i, ind))
#     else:
#         con += 1
#         ind_con.append((i, ind))
# if vow == 0 or con == 0:
#     print(0)
# else:
#     if s[k-1] in vowels:
#         coins += vow
#         for i in range(len(ind_vow)):
#             if ind_vow[0][0] == s[k-1]:
#                 break
#             ind_vow = ind_vow[-1] + ind_vow[:-1]
#         for i in range(1,len(ind_vow)):
#             coins += abs(ind_vow[i-1] - ind_vow[i])

#         print(coins)
#     else:
#         coins += con
#         for i in range(len(ind_vow)):
#             if ind_con[0][0] == s[k-1]:
#                 break
#             ind_con = ind_con[-1] + ind_con[:-1]
#         for i in range(1,len(ind_con)):
#             coins += abs(ind_con[i-1] - ind_con[i])
#         print(coins)


n = int(input())
