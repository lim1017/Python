# Python is general purpose and also object oriented language.

# It's a convention that the class name starts with caps. But Python doesn't throw any error if you are not following it.
class Animal():
  # This is the constructor.
  # As you can see in every method of the class I have passed 'self' as the first parameter. The first parameter is always expected to be the current instance of the class and it is mandatory to pass the instance in the first parameter. And you can name that variable whatever you like.
  def __init__(self, name): 
    self.name = name

  def eat(self):
    print(self.name +' eats')

  def sleep(self):
    print(self.name+' sleeps')

  def printName(self):
    print(self.name + "is my name")

# Initiating a class

cat = Animal('willow')
cat.sleep()
cat.printName()

cat.name="bob"

cat.sleep()


print('******* starting person class ********')

# Technically there is no way to make private attrbiutes in Python. But there are some techniques Python devs are using it. I will try to list out some.

class Person():
  # You can see that I have used different name for the first parameter.
  def __init__(my_instance, name):
    # 'name' attribute is protected.
    my_instance._name = name

  def reads(my_instance):
    print(my_instance._name + ' reads')

  def writes(my_object):
    print(my_object._name + ' writes')

person1 = Person('Ramsy')

person1.reads()



print('********* Inheritance ********')

# But every dev know that accessing and modifying the private attributes is a bad practice. And Python doesn't really have a clear restriction to avoid it. So you got to trust your peers on this.

# Inheritance

class Animal():
  def __init__(self, name):
    self.name = name

  def eat(self):
    print('Animal eats')

  def sleep(self):
    print('Animal sleeps')

# Dog is a sub class of Animal
class Dog(Animal):
  def __init__(self, name):
    self.name = name

  def eat(self):
    print('Dog eats')

dog1 = Dog('harry')
dog1.eat()
dog1.sleep()
