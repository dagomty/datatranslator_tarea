# Part4.ipynb Construction Questions

#Take the following for loop, and translate it into a list. comprehensions:
print("Hello World")

odds = []
for num in range(10): 
    if num % 2 != 0: 
        odds.append(num)
print(odds)

my_odds = [num for num in range(10) if num %2 !=0]
print(my_odds)

cubes = {}
for num in range(1, 6):
        cubes[num] = num **  3
cubes

cubes = {num:num**3 for num in range(1,6)}

