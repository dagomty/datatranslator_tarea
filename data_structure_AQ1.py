#1. Write a script that prompts the user to input numbers separated by commas. Your script will then take these inputted numbers and store them as a list of tuples, two at a time. Finally, your script will print that list of tuples to the user. If the user inputs an odd number of numbers, then only make a list of the largest number of pairs of two that are possible.

#Example: If you inputted the numbers `1, 2, 3, 4, 5, 6`, your script should print `[(1, 2), (3, 4), (5, 6)]`. If you inputted the numbers `1, 2, 3, 4, 5`, your script should print `[(1, 2), (3, 4)]`.

#**Hint**: Check out the [zip](https://docs.python.org/3/library/functions.html#zip) function. While you don't have to use it, it could make things easier.

x =[input("Add numbers separated by ','")]
print(x)
pares=[]
nones=[]
cuenta=1
for x in range(1,7):
   if x % 2 == 0:
       pares.append(x)
   else:
       nones.append(x)
#cuenta=cuenta+1
zipped=zip(pares, nones)
list(zipped)