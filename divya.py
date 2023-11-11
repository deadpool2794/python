# def solve():
#     n = int(input())
#     arr =[int(x) for x in input().split()]
#     target = int(input())

#     d = {}

#     for i in arr:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1

#     triplets = []
#     unq = list(d)
#     unq = sorted(unq)
#     l = len(unq)

#     for i in range(l-2):
#         temp = target
#         temp -= unq[i]
#         l, r = i+1, l-1
#         while(l < r):
#             if unq[l] + unq[r] == temp:
#                 triplets.append((unq[i], unq[l], unq[r]))
#                 break 
#             elif unq[l]+unq[r] > temp:
#                 r-=1
#             else:
#                 l+=1    
#     print(triplets)

# t = int(input())
# while(t):
#     solve()
#     t-=1




# def contains(s, t):
#     return f(0, 0)

# def f(i, j):
#     if i == len(s):
#         return j == len(t)
#     if(j == len(t)):
#         return True
#     if(s[i] == t[j]):
#         return f(i+1, j+1)
#     return f(i+1, j)

# s, t = input(), input()
# print(contains(s, t))



# def g(ind, x, lft):
#     if (ind==len(lft)):
#         return x==0 
#     l = g(ind+1, x, lft)
#     r=False 
#     if (x-lft[ind] >= 0):
#         r = g(ind+1, x-lft[ind], lft)
#     return l or r


# def split(arr,i,sm):
#     print(arr)
#     s=sum(arr)
#     if (s%2==1):
#         return False
#     else:
#         grp1, grp2, lft = [], [], []
#         for i in arr:
#             if i%5 == 0:
#                 grp1.append(i)
#             elif i%3 == 0:
#                 grp2.append(i)
#             else:
#                 lft.append(i)
#         sgrp1, sgrp2, lim = sum(grp1), sum(grp2), s/2
#         if (sgrp1 > lim or sgrp2 > lim):
#             return False
#         if (g(0, lim-sgrp1, lft)):
#             return True 
#     return False
    
# n = input()
# arr = [int(ele) for ele in input().split()]
# ans = split(arr,0,0)
# if ans is True:
#     print('true')
# else:
#     print('false')

# from bisect import bisect_left
# n = int(input())
# arr = sorted([int(x) for x in input().split()])
# ans = 0
# for i in range(arr[0], arr[n-1]+1):
#     ans = max(ans, (i*(n-bisect_left(arr, i))))
# print(ans)


    

# from sys import stdin, setrecursionlimit
# import queue

# setrecursionlimit(10 ** 6)


# #Following is the structure used to represent the Binary Tree Node
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None



# def buildTree(postOrder, inOrder, n) :
#     if len(postOrder)==0:
#         return None 
#     rootData = postOrder[-1]
#     root=BinaryTreeNode(rootData)
#     rootIndexInorder=-1
#     for i in range(len(inOrder)):
#         if inOrder[i]==rootData:
#             rootIndexInorder=i
#             break
#     if rootIndexInorder==-1:
#         return None
#     leftInorder=inOrder[:rootIndexInorder]
#     rightInOrder=inOrder[rootIndexInorder+1:]
    
#     lenLeftSubtree=len(leftInorder)
#     leftPostorder=postOrder[:rootIndexInorder]
#     rightPostorder=postOrder[rootIndexInorder:n-1]
    
#     leftChild=buildTree(leftPostorder,leftInorder,len(leftPostorder))
#     rightChild=buildTree(rightPostorder,rightInOrder,len(rightPostorder))
    
#     root.left = leftChild
#     root.right = rightChild

#     return root
	


# def printLevelWise(root):
#     if root is None :
#         return

#     pendingNodes = queue.Queue()
#     pendingNodes.put(root)
#     pendingNodes.put(None)

#     while not pendingNodes.empty(): 
#         frontNode = pendingNodes.get()
    
#         if frontNode is None :
#             print()
            
#             if not pendingNodes.empty() :
#                 pendingNodes.put(None)
                
#         else :
#             print(frontNode.data, end = " ")
            
#             if frontNode.left is not None :
#                 pendingNodes.put(frontNode.left)
                
                
#             if frontNode.right is not None :
#                 pendingNodes.put(frontNode.right)


# #Taking level-order input using fast I/O method
# def takeInput():
#     n = int(stdin.readline().strip())

#     if n == 0 :
#         return list(), list(), 0

#     postOrder = list(map(int, stdin.readline().strip().split(" ")))
#     inOrder = list(map(int, stdin.readline().strip().split(" ")))

#     return postOrder, inOrder, n

# # Main
# postOrder, inOrder, n = takeInput()
# # print(postOrder, inOrder, n)
# root = buildTree(postOrder, inOrder, n)
# printLevelWise(root)

# def f(a, b, c, a_, b_):
#     if(c > max(a, b)):
#         return False
#     if(a_ == c or b_ == c):
#         return True
#     cur = False
#     if(a_ == 0):
#         cur = cur or f(a, b, c, a, b_)
#     if(b_ == 0):
#         cur = cur or f(a, b, c, a_, b)
#     if(a_ != 0):
#         cur = cur or f(a, b, c, 0, b_)
#     if(b_ != 0):
#         cur = cur or f(a, b, c, a_, b)
    
    
    

# t = int(input())
# for _ in range(t):
#     a, b, c = [int(x) for x in input().split()]
#     if(a < b):
#         a, b = b, a
#     print('Yes') if(f(a, b, c, 0, 0)) else print("No")

# n = int(input())
# arr = [int(x) for x in input().split()]
# mat = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(arr[(i*n)+j])
#     mat.append(row)
# print(mat)

# from queue import Queue
# class BTN:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def change_node_to_head(self, target_node):
#         # print(target_node.val)
#         if target_node is self.root:
#             return
#         parent = self.find_parent(self.root, target_node)
#         if parent.left is target_node:
#             parent.left = None
#         else:
#             parent.right = None
#         target_node.left = self.root
#         target_node.right = self.root.right
#         self.root = target_node


#     def find_parent(self, current, target):
#         if current is None or current is target:
#             return None
#         if current.left is target or current.right is target:
#             return current
#         left_result = self.find_parent(current.left, target)
#         if left_result is not None:
#             return left_result
#         return self.find_parent(current.right, target)


# def prt(tree):
#     queue = Queue()
#     queue.put(tree.root)
#     queue.put(None)
#     row, lvls = [], []
#     while(not queue.empty()):
#         cur = queue.get()
#         if(cur == None):
#             if(len(row) != 0):
#                 lvls.append(row)
#             row = []
#             if(queue.qsize() > 1):
#                 queue.put(None)
#             continue
#         if(cur.val != -1):
#             row.append(cur.val)
#         if(cur.left):
#             queue.put(cur.left)
#         if(cur.right):
#             queue.put(cur.right)
#     for i in lvls:
#         j = sorted(i)
#         print(*j)


# def find(root, target):

#     if(root and root.val == target):
#         return root
#     if(root.left):
#         lft = find(root.left, target)
#         if(lft and lft.val == target):
#             return lft
#     if(root.right):
#         rgt = find(root.right, target)
#         if(rgt and rgt.val == target):
#             return rgt
#     return None
        

# def solve():
#     nodes = [int(x) for x in input().split()]
#     n = len(nodes)
#     target = int(input())
#     queue = Queue()
#     i = 0
#     tree = BinaryTree()
#     tree.root = BTN(nodes[i])
#     queue.put(tree.root)
#     while(not queue.empty()):
#         cur = queue.get()
#         if(i+1 < n):
#             cur.left = BTN(nodes[i+1])
#         if(i+2 < n):
#             cur.right = BTN(nodes[i+2])
#         i+=2
#         if cur.left is not None:
#             if  cur.left.val != -1:
#                 queue.put(cur.left) 
#         if cur.right is not None:
#             if cur.right.val != -1:
#                 queue.put(cur.right)
#     tree.change_node_to_head(find(tree.root, target))
#     prt(tree)

# t = int(input())
# for _ in range(t):
#     solve()



t = int(input())
while t != 0:
    t -= 1
    n = int(input())
    manholes = [int(x) for x in input().split()]
    dp = [[-1, -1, -1, -1] for i in range(n+1)]

    def f(ind, cur, dp):
        if(ind == n):
            return 0
        if(dp[ind][cur] != -1):
            return dp[ind][cur]
        mn = 1e7
        if(manholes[ind+1] != cur):
            mn = min(mn, f(ind+1, cur, dp))
        else:
            for i in range(1, 4):
                if(i != cur and manholes[ind] != i):
                    mn = min(mn, 1 + f(ind, i, dp))
        dp[ind][cur] = mn
        return mn

    print(f(0, 2, dp))




















































































