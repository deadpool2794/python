# # import re


# # num = input()
# # req = 0
# # for i in num:
# #     i = int(i)
# #     if i > req:
# #         req = i
# # print(req)

# # arr = [int(x) for x in input().split()]
# # nature = input()
# # length = int(input())
# # tot_charge = 0
# # for i in range(length):
# #     if nature[i] == "N":
# #         tot_charge -= arr[i]
# #     else :
# #         tot_charge += arr[i]
# #     tot_charge = abs(tot_charge)
# # print(tot_charge * 100)

# # n = int(input())
# # arr = [int(x) for x in input().split()]
# # arr.sort(reverse=True)
# # pen = []
# # for i in range(n-1):
# #     pen.append(arr[i] - arr[i+1])
# # print(sum(pen))


# # s = "11111010010101001010010001010111110101010101010100101001010101010101010101010101011010101101001010011010101010101000101010001010101010101011111111010010110101011010010101010100101010010100100101001010100101010111110100101010010100100010101111101010101010101001010010101010101010101010101010110101011010010100110101010101010001010100010101010101010111111110100101101010110100101010101001010100101001001010010101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111000000001111101001010100101001000101011111010101010101010010100101010101010101010101010101101010110100101001101010101010100010101000101010101010101111111101001011010101101001010101010010101001010010010100101010010101011111010010101001010010001010111110101010101010100101001010101010101010101010101011010101101001010011010101010101000101010001010101010101011111111010010110101011010010101010100101010010100100101001010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111100000000"
# # s = '1111111111111111111111111111111111111100'
# # print(len(s))

# def convert(s):
#     dec = 0
#     n = len(s)-1
#     for i in s:
#         dec += int(i) * 2**(n)
#         n -= 1
#     return dec


# s = []
# for i in range(31):
#     s.append(input())

# s2 = sorted(s)

# for i in range(31):
#     print(s[i], ' - ',  s2[i])


# # 00001
# # 00010
# # 00011
# # 00100
# # 00101
# # 00110
# # 00111
# # 01000
# # 01001
# # 01010
# # 01011
# # 01100
# # 01101
# # 01110
# # 01111
# # 10000
# # 10001
# # 10010
# # 10011
# # 10100
# # 10101
# # 10110
# # 10111
# # 11000
# # 11001
# # 11010
# # 11011
# # 11100
# # 11101
# # # 11110
# # # 11111
# n = int(input())
# names = []
# votes = []
# for _ in range(n):
#     name, vote = input().split()
#     names.append(name)
#     votes.append(int(vote))

# mx = max(votes)
# mn = min(votes)
# mx_arr = []
# mn_arr = []
# for i in range(n):
#     if votes[i] == mn:
#         mn_arr.append(names[i])
# for i in range(n):
#     if votes[i] == mx:
# #         mx_arr.append(names[i])

# # mx_arr.sort()
# # mn_arr.sort()
# # print("{},{}".format(mn_arr[0], mx_arr[0]))

# # l, s = map(int, input().split())
# # stars = '*' * l
# # space = ' '
# # for i in range(l):
# #     print((s*(l-i-1)) , end = '')
# #     print((s*(l-i-1)) * space + stars)


# t = int(input())
# for _ in range(t):
#     n, s = map(int, input().split())
#     arr = []
#     for i in input().split():
#         arr.append(int(i))
#     arr.sort()
#     ct, books = 0, 0
#     for i in range(n):
#         books += arr[i]
#         if books <=s:
#             ct += 1
#         else:
#             break
#     print(ct)

# n = int(input())
# d = {}
# for i in range(1, 27):
#     d[i] = chr(64+i)
# st = ''
# while(n):
#     st = d[n%26] + st
#     n //= 26
# print(st)


# insert into travel_payment values(1,	656,	503	,to_date('21-DEC-17 09.15.15 AM','DD-MON-YY HH.MI.SS AM'),	505	,to_date('21-DEC-17 09.45.15 AM','DD-MON-YY HH.MI.SS AM')  ,40.25);
# insert into travel_payment values(2,	653,	503	,to_date('22-DEC-17 11.20.15 AM','DD-MON-YY HH.MI.SS AM'),	504	,to_date('22-DEC-17 11.45.15 AM','DD-MON-YY HH.MI.SS AM')  ,29.75);
# insert into travel_payment values(3,	654,	501	,to_date('23-DEC-17 09.15.15 PM','DD-MON-YY HH.MI.SS PM'),	504	,to_date('23-DEC-17 09.50.15 PM','DD-MON-YY HH.MI.SS PM')  ,37.25);
# insert into travel_payment values(4,	656,	515	,to_date('22-DEC-17 12.30.15 PM','DD-MON-YY HH.MI.SS PM'),	511	,to_date('22-DEC-17 12.55.15 PM','DD-MON-YY HH.MI.SS PM')  ,36.75);
# insert into travel_payment values(5,	659,	516	,to_date('21-DEC-17 10.15.15 AM','DD-MON-YY HH.MI.SS AM'),	518	,to_date('21-DEC-17 11.15.15 AM','DD-MON-YY HH.MI.SS AM')  ,22.25);
# insert into travel_payment values(6,	657,	520	,to_date('21-DEC-17 09.30.15 AM','DD-MON-YY HH.MI.SS AM'),	516	,to_date('21-DEC-17 09.43.15 AM','DD-MON-YY HH.MI.SS AM')  ,45.5);
# insert into travel_payment values(7,	660,	521	,to_date('23-DEC-17 11.15.25 AM','DD-MON-YY HH.MI.SS AM'),	525	,to_date('23-DEC-17 11.57.25 AM','DD-MON-YY HH.MI.SS AM')  ,37.45);
# insert into travel_payment values(8,	663,	522	,to_date('21-DEC-17 09.15.15 AM','DD-MON-YY HH.MI.SS AM'),	524	,to_date('21-DEC-17 09.30.15 AM','DD-MON-YY HH.MI.SS AM')  ,39.35);
# insert into travel_payment values(9,	660,	506	,to_date('22-DEC-17 02.30.15 PM','DD-MON-YY HH.MI.SS PM'),	510	,to_date('22-DEC-17 02.50.15 PM','DD-MON-YY HH.MI.SS PM')  ,30);
# insert into travel_payment values(10,	653,	512	,to_date('21-DEC-17 09.15.15 AM','DD-MON-YY HH.MI.SS AM'),	514	,to_date('21-DEC-17 09.40.15 AM','DD-MON-YY HH.MI.SS AM')  ,25.75);
# insert into travel_payment values(11,	654,	513	,to_date('21-DEC-17 10.15.20 AM','DD-MON-YY HH.MI.SS AM'),	511	,to_date('21-DEC-17 10.40.20 AM','DD-MON-YY HH.MI.SS AM')  ,32.65);
# insert into travel_payment values(12,	655,	507	,to_date('22-DEC-17 09.15.15 AM','DD-MON-YY HH.MI.SS AM'),	510	,to_date('22-DEC-17 09.50.15 AM','DD-MON-YY HH.MI.SS AM')  ,38.25);
# insert into travel_payment values(13,	651,	517	,to_date('23-DEC-17 11.15.15 AM','DD-MON-YY HH.MI.SS AM'),	519	,to_date('23-DEC-17 11.40.15 AM','DD-MON-YY HH.MI.SS AM')  ,19.5);
# insert into travel_payment values(14,	658,	525	,to_date('23-DEC-17 12.45.15 PM','DD-MON-YY HH.MI.SS PM'),	523	,to_date('23-DEC-17 01.15.20 PM','DD-MON-YY HH.MI.SS PM')  ,41.25);
# insert into travel_payment values(15,	662,	506	,to_date('23-DEC-17 03.40.15 PM','DD-MON-YY HH.MI.SS PM'),	509	,to_date('23-DEC-17 04.00.25 PM','DD-MON-YY HH.MI.SS PM')  ,25);
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'
# ,'DD/MM/YYYY HH:MI:SS'


# insert into station_route values(101,	501,	1,	1);
# insert into station_route values(102,	502,	1,	2);
# insert into station_route values(103,	503,	1,	3);
# insert into station_route values(104,	504,	1,	4);
# insert into station_route values(105,	505,	1,	5);
# insert into station_route values(106,	506,	2,	1);
# insert into station_route values(107,	507,	2,	2);
# insert into station_route values(108,	508,	2,	3);
# insert into station_route values(109,	509,	2,	4);
# insert into station_route values(110,	510,	2,	5);
# insert into station_route values(111,	511,	3,	1);
# insert into station_route values(112,	512,	3,	2);
# insert into station_route values(113,	513,	3,	3);
# insert into station_route values(114,	514,	3,	4);
# insert into station_route values(115,	515,	3,	5);
# insert into station_route values(116,	516,	4,	1);
# insert into station_route values(117,	517,	4,	2);
# insert into station_route values(118,	518,	4,	3);
# insert into station_route values(119,	519,	4,	4);
# insert into station_route values(120,	520,	4,	5);
# insert into station_route values(121,	521,	5,	1);
# insert into station_route values(122,	522,	5,	2);
# insert into station_route values(123,	523,	5,	3);
# insert into station_route values(124,	524,	5,	4);
# insert into station_route values(125,	525,	5,	5);


def isPalindrome(s):
    i = 0
    j = 4
    while(i < j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

arr = []
for i in range(10000, 100000):
    if isPalindrome(str(i)):
        arr.append(str(i))
ct = 0

print(arr[1])