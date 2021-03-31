
#list is like array
person = ["person1","person2","person3","person4"]

print(type(person))
print(person)

#output :

#<class 'list'>
#['person1', 'person2', 'person3', 'person4']


print(person[0])
print(person[1])

#output :

#person1
#person2


print(len(person))
#output : 4

print(person.count('person1'))
#output : 1    //check how many times same thing    present in the list

print(person.index('person1'))
#output : 0

#reverse

person.reverse()
print(person)

#output :
['person4', 'person3', 'person2', 'person1']

#append

person.append('person5')
print(person)

#output : [ in append value is added at last location in the list]
['person4', 'person3', 'person2', 'person1', 'person5']

#sort

person.sort()
print(person)

#outout :
['person1', 'person2', 'person3', 'person4', 'person5']

#pop

person.pop()
print(person)

#output:  [ in pop last value pop out from list]
['person1', 'person2', 'person3', 'person4']