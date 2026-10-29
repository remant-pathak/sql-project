# 151. Remove all occurrences of a specified value from a list. 
# b=[88,77,77,88,99,45,55,41,11,12,25,25,25,25,25,78,78,8]

# c=b.copy()

# while 77 in c:
#     c.remove(77)

# print(c)

# 152. Remove all even numbers from a list. 
# b=[88,77,77,88,99,45,55,41,11,12,25,25,25,25,25,78,78,8]

# b=[x for x in b if x%2!=0]   

# print(b)

# i=0
# while i<len(b):
#     if b[i]%2==0:
#         b.remove(b[i])
#     else:
#         i=i+1

# print(b)            

# Remove all odd numbers from a list.

b=[1,2,3,4,5,6,7,8,9,10,11,12,13,45,55,66,7,88,97,787,585,101]

# b=a.copy()

# b=[x for x in b if x%2==0]
# print(b)

# i=0

# while i< len(b):
#     if b[i]%2!=0:
#         b.remove(b[i])
#     else:
#         i=i+1

# print(b)

#154. Insert an element into a sorted list while preserving ascending order. 

# a=[66,55,77,88,9898,2,1,0,557,121,2225,88888,14545,6868,12,21,25,25,36,65,0]

# a.sort()
# print(a)
# a.insert(0,45)
# a.sort()
# print(a)
# 155. Merge two lists using list methods. 
# a=[66,55,77,88,9898,2,1,0,557,121,2225,88888,14545,6868,12,21,25,25,36,65,0]
# b=[88,77,77,88,99,45,55,41,11,12,25,25,25,25,25,78,78,8]
# a.extend(b)
# a.sort()
# print(a)

# 156. Create a list of unique values from another list. 



# b=list(set(a))

# print(b)


# 157. Remove duplicate values while preserving the original order.
# a=[1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,7,7,7,7]
# i=0
# while i< len(a)-1:
#     if a[i]==a[i+1]:
#         a.remove(a[i])
#     else:
#         i=i+1

# print(a)

b=[4,9,2,88,12,65,47,85,98,78,0,2,44,44,45,45,65,65,87,87,85,85,48]

c=list(set(b))
print(c)
