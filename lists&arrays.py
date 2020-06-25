# lists = arrays

numbers = ["one", "two", "three"]

print(numbers[0])# one

print(numbers[-1]) # three. This is awesome. If we pass negative value Python will start from the end.

print(numbers[-2]) # two

print(len(numbers), "the length of the numbers list") # 3. It just returns the length

numbers.append(5)
print(numbers)

numbers.insert(1, "wrong_one") # Insert will insert the particular value to the appropiate position. ["one", "wrong_one", "two", "three", "four"]

print(numbers, 'after inserting')
del numbers[1]
print(numbers, 'after delete')

popped_element = numbers.pop()

print(popped_element, 'popped off number')

numbers.sort()
print(numbers)

num = [1,4,2,3,5,22,111,123]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

alpha = ["z", "c", "a"]
print(sorted(alpha)) # ["a", "c", "z"] This will just return the sorted array. It wont save the sorted array to the variable itself.

print(alpha) # ["z", "c", "a"] As you can see, it's not sorted


# reverse array/list
# Reversing an array
nums = [10, 1, 5]
nums.reverse()
print(nums) # [5, 1, 10] It just reverses an array. It means it reads from last. It's not sorting it. It's just changing the chronological order.

alpha[:] # ['a', 'b', 'c', 'd', 'e'] There is no starting or ending index. So you know what happens. And this helps you in copying the entire array. I think I don't have to explain that if you copy the array, then any changes in the original array won't affect the copied array.

another_alpha = alpha # This is not copying the array. Any changes in alpha will affect another_alpha too. 


#concat lists
a=[1,2,3]
b=[4,5,6]
ab=a+b
print(ab)


