#conditional statment

#assign value
a,b,c = 5,10,15


#if condition example

if a == 5:
    print("this is == example")
#output = this is == example

if a == 5 and b < 12:
    print("this is and operator example")
#output = this is and operator example

if a == 8 or b < 14:
    print("this is or operator example")
#output = this is or operator example


#if - else condition example
if a > 10:
    print("true")
else:
    print("fasle")
#output = fasle

#if-elif-else condition example

if a > 10:
    print("a is greater than 10")
elif a > 20:
    print("a is greater than 20")
else:
    print("a is having different value")

#output - a is having different value ( a value is 5 )


#another example

if a==5 and b<=9:
	print ("hello")
	if c < 150:
		print ("hello world")
	else:
		print ("hi")

#output is blank

if a==5 and b<=10:
	print ("hello")
	if c < 14:
		print ("hello world")
	else:
		print ("hi")

#output -
#hello
#hi