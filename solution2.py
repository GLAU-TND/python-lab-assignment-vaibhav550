c=(2,1,3,4,5,6)
try:
    #c.remove(5)
    
    #c=5+'sj'
    
    #c=float('hello')

except AttributeError as e:
    print("AttributeError",e)
except TypeError as e:
    print("TypeError",e)
except ValueError as e:
    print("ValueError",e)
finally:
    print("Process Complete")