#Program 3:

#Write a python program to read two numbers and find the sum of their cubes

number = float(input("enter the number"))

cube =  number * number * number

print("Cube of a given number {} = {}".format(number,cube))



# using def

def calCube(number):
    return  number * number * number

number = float(input("enter the number"))

cube = calCube(number)
print("Cube of a given number {} = {}".format(number,cube))