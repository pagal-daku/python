# tuples - placing all the items /elements /value inside parentheses () seperated by comma
# tuple can have any number of items
# they may be of different types (integer, float, list, string, etc datatypes)
# Tuples are immutable

t = ()
print(t)
print(type(t))

#output :
#()
#<class 'tuple'>

t = ('apple','mango','london','river',1,2.5,1.000)
print(t)

#output :
#('apple', 'mango', 'london', 'river', 1, 2.5, 1.0)

print(t[0])
#output :
#apple

print(t[5])
#output :
#2.5

print(t[2:5])
#output :
#('london', 'river', 1)

print(t[-1])
#output:
#1.0

print(t[::-1])
#output :
#(1.0, 2.5, 1, 'river', 'london', 'mango', 'apple')

t[0] = 'pineapple'

#output: (tuple is immutable) you can not change value base on index
# Traceback (most recent call last):
#  File "/home/sumit/python practice/python_with_git/python/topic/data_type/tuples.py", line 36, in <module>
#    t[0] = 'pineapple'
# TypeError: 'tuple' object does not support item assignment

a = "pagal"
b = "daku"

print(a,3.15,b)

#output :
#pagal 3.15 daku



