# pyhton has 2 types of loops, for and while loop

# WHILE loops
# The following while print till 5. Remember the indentation.
i = 0
while i <= 5:
  print(i)
  i += 1

  if i == 2:
    break # You can try using continue here


# Here comes the interesting part. While loop has else part. Else part will execute once the entire loop is completed.
i = 10
while i <= 15:
  print(i)
  i += 1
else:
  print('after the loop')

  # But if you are using break in the loop, then Python will break out of the entire loop and it won't execute else part.
i = 10
while i <= 15:
  print(i)
  i += 1
  if i == 13:
    break
else:
  print('Completed')


# for loops
print("************ for loops ******************")
# For loops like for(i=0; i<5; i++) are not mostly used in Python. Instead, Python insists on iterating over items

arr = ['a', 'b', 'c', 'd', 'e']
for ele in arr: # Prints every element in an array
  print(ele)

# range(start, stop, step)
print('range loop')
for i in range(0,len(arr)-1, 2):
  print(arr[i])



# loop though dictionary
print('********looop though dictionary ************')
dict = {'name': 'John wick', 'age': '22', "gener":"male"}

# You can iterate through a dictionary. items() will return both keys and values. You can also use keys() and values() if needed. 
for key, value in dict.items():
  print(key + " is " + value)


# You can also use a built-in function enumerate(). enumurate() will return a tuple with index. It is mostly used to add a counter to the iterable objects in Python.
for value in enumerate(arr):
  print(str(value) + " is present in ")