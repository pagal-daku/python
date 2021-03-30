#Program 1 - With Python inbuild method

#Write a python program find the number of characters present in a string with help of len()

findLengthWithLen = "This is find number of characters present in a string using len function"

print(len(findLengthWithLen))
#output = 72




#Program 1 -  Without  Python inbuild method

#Write a python program find the number of characters present in a string (with out using len())

#string
findLengthWithOutLen = "This is find number of characters present in a string without using len function"

#count = 0
#use for loop to travse the string

count = 0
for string in findLengthWithOutLen:
    count = count+1
print(count)
#output =  80


#using def function
def findLength(string):

    #count set to 0
    count = 0

    for i in string:
        count = count + 1
    return count

#pass the string as parameter
print(findLength(findLengthWithOutLen))