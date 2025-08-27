first = "bob"
last = "boberts"
# print(type(first))
# print(type(first)==str)
# print(isinstance(last,str))

#constructor

# pizza = str("peppernoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))

#concat
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like the year " + decade + "s"
print(statement)

multiline = '''
Hey, how are you                                         

I'm was just checking in

                                    all good?

'''
print(multiline)


Specials = 'I\'m back at work! \tHey! \n\nWhere\'s this at\\located'
print(Specials)

#methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace('good' , 'all ok?'))
print(len(multiline))
multiline += '                                                                       '
multiline = '                                                                        ' + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("<>")
#build menu

title = "Menu".upper()
print(title.center(20, '='))

print("coffee".ljust(20, '.') + "£2.00".rjust(4))
print("latte".ljust(20, '.') + "£3.00".rjust(4))
print("espresso".ljust(20, '.') + "£7.00".rjust(4))

print("")

print(first[1])  
print(first[-1])  
print(first[0:])  

# boolean methods

print(first.startswith("b"))
print(first.endswith("b"))

#boolean data types
myvalue = True
x = bool(False)
print(type(myvalue))
print(isinstance(myvalue, bool))

#numeric data types
#integer types

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float types
gpa = 3.28
y = float(1.14)
print(type(gpa))

#complex types
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built in functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))    

import math 

print(math.pi)
print(math.sqrt(16))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number   
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#errors for incorrect data
#zip_value =  int("NYC")

