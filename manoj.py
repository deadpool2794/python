# def maximumTeams(t):
#     for _ in range(t):
#         n, x = map(int, input().split())
#         a = list(map(int, input().split()))
#         a.sort()  # Sort the skill levels in non-decreasing order

#         team_count = 0
#         min_skill = float('inf')

#         for i in range(n):
#             if a[i] * (i + 1) >= x:
#                 team_count += 1
#                 min_skill = float('inf')
#             else:
#                 min_skill = min(min_skill, a[i])

#         print(team_count)


# # Read the number of test cases
# t = int(input())

# # Call the maximumTeams function
# maximumTeams(t)



    
