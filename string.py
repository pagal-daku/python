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

#find position

print(a.find('n'))

print(a.rfind('q'))
print(a.rfind('n'))

print(a.find('training'))