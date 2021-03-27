a = "python string practice"

#length of particular string
print(len(a))

#
print(max(a))
print(min(a))

#position in string
print(a[0])

#from to to position string
print(a[0:2])

#concat string
string1 = 'python'
string2 = ' tutorial'

print(string1 + string2)

#print same string multiple times
t = "demo "
print(t  * 2)

#check value present in the string
if 'x' in a:
    print("true")
else:
    print("false")

# String count

print(a.count('p'))
print(a.count('y'))
print(a.count('a'))
print(a.count('t'))

#string count first veriable , start position , end position
print(a.count('t',6,22))

#find position using find and index method

print(a.find('n'))

print(a.rfind('q'))
print(a.rfind('n'))

print(a.find('training'))

print(a.index('n'))

print(a.rindex('n'))

#ValueError: substring not found
#a.index('q')

#split with paramter like , . etc
a="192,168,1,1"
print(a.split(','))
#output - ['192', '168', '1', '1']

a = "this is example of split statement in python"
print(a.split('i'))
#output - ['th', 's ', 's example of spl', 't statement ', 'n python']

print(a.split('i',maxsplit = 1))
#output - ['th', 's is example of split statement in python']

print(a.split('i',maxsplit = 3))
#output - ['th', 's ', 's example of spl', 't statement in python']


#join

a = ['192', '168', '1', '1']
b = ","

print(b.join(a))  #output - 192,168,1,1


statment = '''up arrow click down 
arrow click
left arrow click 
right arraow click'''

print(statment)

print(statment.splitlines())

#strip

a = "-----remove dash-------"

print(a.strip('-'))
#output = remove dash

print(a.lstrip('-'))
#output = remove dash-------

print(a.rstrip('-'))
#output = -----remove dash

#remove space between the words

a = "    remove blank spaces     "

print(a.strip())
#output = remove blank spaces


#string replace

stringNew = "This is string replace statement"

print(stringNew.replace('s','S'))
#output = ThiS iS String replace Statement

print(stringNew.replace('s','S',1))
#output = ThiS is string replace statement

print(stringNew.replace('This is','Use'))
#output = Use string replace statement

#case conversions
#inlude capitalize() , title(), upper(),lower()

string = "python case conversion excerises"

print(string.capitalize())
# output = Python case conversion excerises (0th postion value change to capital)
# eg - string[0] here its P

print(string.title())
#output = Python Case Conversion Excerises (first letter capital in each word)

print(string.upper())
#output = PYTHON CASE CONVERSION EXCERISES ( all letter capital format)

stringForLower = string.upper()
print(stringForLower.lower())

#output = python case conversion excerises

