c=(2,1,3,4,5,6)
try:
    c.remove(5)
except AttributeError as e:
    print("AttributeError",e)
else:
    print("Process 1")
try:
    c=5+'str'
except TypeError as e:
    print("TypeError",e)
else:
    print("Process 2")

try:
    c=float('Hello')
except ValueError as e:
    print("ValueError",e)
finally:
    print("Process Complete")
