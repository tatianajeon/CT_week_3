# Lucky Numbers
# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.



# def luckynum(num):
#     lucky_arr = []
#     for x in num:
#         if x == num.count(x):
#             lucky_arr.append(x)
#             lucky_num = max(lucky_arr)

#     return lucky_num



def lucky_number(lst):        
    return max([x if lst.count(x) == x else -1 for x in lst])

print(lucky_number([2,2,3,4]))



# def luckynum(array):
#     from collections import Counter
#     c = dict(Counter(array))
#     max = 0
#     for k,v in c.items():
#         if k == v:
#             if k > max:
#                 max = k
#         else:
#             return -1
#     return max

# print(luckynum([2,2,3,4]))