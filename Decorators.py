
# Decorates or modify the function and methods
def greet(fx):
  def mfx(*args, **kwargs):  # *args takes the arguments as the tuple, **kwargs takes all arguments as the dictionaries.
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)
