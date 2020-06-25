a = 5
b = 10

# See for the indentation. Indentations are very important in Python. Python will throw error if indentations are proper.
if a == 5:
  print('Awesome')


# and is equivalent to && 
if a == 5 and b == 10:
  print('A is five and b is ten')

  # if else statement. This is same as most of the languages.
if a == 5:
  print('A is five')
elif a == 6:
  print('A is six')
elif a == 7:
  print('A is seven')
else:
  print('A is some number')

# or is equivalent to ||
if a < 6 or a == 10:
  print('A should be less than 6 or should be equal to ten')

# not is equivalent to !
if not a == 10:
  print('A is not equal to 10')

# This is the short-hand notation of if statement.
if a == 5: print('A is five short')
