#print(x) # go to W3 Schools to see the error page to see the exceptions and built in ones
class JustnotcoolError(Exception):
    pass

x = 2
try :
    raise JustnotcoolError("This is a custom exception")
    # #print(x/1)
    # if not type(x) is str:
    #     raise TypeError("TypeError: x should be a string")
except NameError:
    print("NameError: Variable 'x' is a test for this code, it isn't defined")
except ZeroDivisionError:
    print("ZeroDivisionError: You can't divide a number by zero")
except Exception as error:
    print("Exception:", error)
else:
    print("No errors: No exceptions were raised")
finally:
    print("I'm going to print with or without an error")