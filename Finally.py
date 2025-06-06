def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")   # ---
#                                       |----both statement is not sameas work is same for both line
# print("I am always executed")  --------        (it raise question when there is the function given in the given e.g.)


x = func1()
print(x)
