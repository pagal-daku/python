# dictionary are mutable
# dictionary are dynamic


d =  {
        'key':'value',
        'key1':'value1'
     }

print(d)
print(type(d))

#output :

#{'key': 'value', 'key1': 'value1'}
#<class 'dict'>

print(d['key'])

#output:
#value

d['key1'] = "new value 1"
print(d)

#output:
#{'key': 'value', 'key1': 'new value 1'}

d['key2'] = "value2"
print(d)

#output:
#{'key': 'value', 'key1': 'new value 1', 'key2': 'value2'}



person = {}

print(type(person))

person['fname'] = 'joe'
person['lname'] = 'doe'
person['age'] = 35
person['spouse'] = "ida"
person['children'] = ['chis','devid','elena']
person['pets'] = {'cat':'mewo','dog':'spark'}

print(person)

#output:
{
    'fname': 'joe',
    'lname': 'doe',
    'age': 35,
    'spouse': 'ida',
    'children': ['chis', 'devid', 'elena'],
    'pets': {'cat': 'mewo', 'dog': 'spark'}
}



