

# Tuples are just like lists but they are immutable. you cant add or update, only read. like lists Tuples are also sequential

nums = (1, 2, 3)

print(nums) # (1, 2, 3)

print(nums[0]) # 1

print(len(nums)) # 3


empty_tuple = () # empty tuple. Length is zero.

num = (1, ) # Note the trailing comma. When defining a single element in the tuple, consider adding a trailing comma.
print(type(num)) # <type 'typle'> It won't return a tuple. Because there is no trailing comma.

num = (1)
print(type(num)) # <type 'int'> It won't return a tuple. Because there is no trailing comma.

# Creating a new tuple from the existing tuple
nums = (1, 2, 3)
char = ('a', )
new_tuple = nums + char
print(new_tuple) # (1, 2, 3, 'a')



#Sets are unordered collections with no duplicates (unordered meaning you can NOT do set[1] set[3])
print('************ SETS **********')
alpha = {'a', 'b', 'c', 'a'}
print(alpha) # set(['a', 'c', 'b']) As you can see, duplicates are removed in sets. And also the output is not ordered.

# Accessing items in set
# You can't access by index because Sets are unordered. You can access it only by loop. Don't worry about the for loop, we will get that in-depth in the following section.
for ele in alpha:
  print(ele)


print(len(alpha), 'the length')

alpha.add('k')
print(alpha)

alpha.update(['a', 'x', 'z'])
print(alpha)

alpha.discard('a')
print(alpha)
