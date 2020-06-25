def prints_hello_world():
  print('Hello world from Python')



prints_hello_world()


def prints_something(something):
  return something + ' from Python'


print(prints_something("passed in to python function"))

# If you pass wrong number of arguments like two or three arguments to this function then Python will throw an error.
# print(prints_something())


# Default parameter. I think its common in most languages now.
def prints_default(something = 'default msg'):
  print(something + ' from Python')

prints_default()


# keyword arguments. You can pass explicitly which parameter should be matched. In this way, you don't have to send the arguments in order just explicitly mention the parameter name.
def movie_info(title, director_name, ratings):
  print(title + " - " + director_name + " - " + ratings)

movie_info(ratings='9/10', director_name='David Fincher', title='Fight Club')



# Arbitrary number of arguments
# Sometimes, you dont know how many arguments are passed. In that case, you have ask Python to accept as many arguments as possible.

def languages(*names):
  print(names) # ('Python', 'Ruby', 'JavaScript', 'Go'). This is a tuple.
  return 'You have mentioned '+ str(len(names))+ ' languages'

print(languages('Python', 'Ruby', 'JavaScript', 'Go', 'more names')) # You have mentioned 4 languages


def languages2(fav_language, *names):
  print(names) # ('Ruby', 'JavaScript', 'Go')
  return 'My favorite language is ' + fav_language+ '. And Im planning to learn others ' + str(names) + 'thats ' + str(len(names))+ ' other languages!'

print(languages2('Python', 'Ruby', 'JavaScript', 'Go')) # My favorite language is Python. And Im planning to learn other 3 languages too



def user_info(id, name, **info):
  print(info) # {'fav_language': ['Python', 'Ruby'], 'twitter_handle': '@srebalaji'}

user_info(1, 'Srebalaji', fav_language=['Python', 'Ruby'], twitter_handle=['Python', 'Ruby'])
