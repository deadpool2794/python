# def  solve(N,C,W):
#     totalCap = sum(C)
#     totalWat = sum(W)
#     C.sort(reverse = True)
#     tankersReq = 0
#     for i in range(N):
#         if totalWat > 0:
#             totalWat -= C[i]
#             tankersReq+=1
#     return tankersReq

# N = int(input())
# C = list(map(int, input().split()))
# W = list(map(int, input().split()))
# out_ = solve(N,C, W)
# print(out_)


# K, T = map(int, input().split())
# T += 1
# a = [0]*T
# b = [0]*T
# a[0] = 1
# b[0] = 2
# mod = 3001

# for i in range(1, T):
#     a[i] = ((K*b[i-1])%mod+(a[i-1]*a[i-1])% mod) % mod
#     b[i] = (((K*a[i-1])%mod)+b[i-1]) % mod
# print(a[-1], b[-1])

# def sumOfDigits(num):
#     num = str(num)
#     tot = 0
#     for i in num:
#         tot += int(i)
#     return tot


# temp = input1+1
# while True:
#     if(sumOfDigits(temp) == input1 and temp%input1 == 0 ):
#         break
#     temp += 1
# print(input1, temp)

# for i in range(1, 101):
#     print(i)

# Python3 implementation of the approach

# Array that stores visited digits
# visited = [[0 for x in range(501)]
# 			for y in range(5001)]

# Structure for queue Node.
# class Node:
# 	def __init__(self, a, b, string):
# 		self.a = a
# 		self.b = b
# 		self.string = string

# # Function to return the minimum number
# # such that it is divisible by 'a' and
# # sum of its digits is equals to 'b'
# def findNumber(a, b):

# 	# Use list as queue
# 	q = []

# 	# Initially queue is empty
# 	temp = Node(0, 0, "")

# 	# Initialize visited to 1
# 	visited[0][0] = 1

# 	# Push temp in queue
# 	q.append(temp)

# 	# While queue is not empty
# 	while len(q) > 0:

# 		# Get the front of the queue
# 		# and pop it
# 		u = q.pop(0)

# 		# If popped element is the
# 		# required number
# 		if u.a == 0 and u.b == b:

# 			# Parse int from string
# 			# and return it
# 			return int(u.string)

# 		# Loop for each digit and check the sum
# 		# If not visited then push it to the queue
# 		for i in range(0, 10):
# 			dd = (u.a * 10 + i) % a
# 			ss = u.b + i
			
# 			if ss <= b and visited[dd][ss] == False:
# 				visited[dd][ss] = 1
# 				q.append(Node(dd, ss, u.string + str(i)))

# 	# Required number not found return -1.
# 	return -1

# # Driver code.
# if __name__ == "__main__":

# 	a, b = 100,100
# 	print(findNumber(a, b))
	
# # This code is contributed by Rituraj Jain

tc = int(input())
for _ in range(tc):
    n = int(input())
    i = 1
    flag = 0
    while i < 10000000:
        if i == n:
            i = i + 1
            continue
        if i % n == 0:
            x = [int(a) for a in str(i)]
            b = sum(x)
            if b == n:
                print("Value is:", i)
                flag = 1
                break
        i = i + 1
    if flag == 0:
        print(-1)
