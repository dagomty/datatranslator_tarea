# 1. Multiplication can be thought of as repeated additions. Write a script that takes as input two positive integers, `a` and `b`, and returns `a * b`. Do this without using the `*` operator. 

print("# 1 Multiplication Game")
a = int(input("Please enter a number"))
b = int(input("Please enter a number"))
x=0
y=0
total=0

for x in range(0,a):
    total = total + b

print("Multiplication: " + str(total))

# 2. Integer division can be done with repeated substraction, similar to how multiplication can be done with addition. Write a script that takes as input two positive integers, `a` and `b`, and returns `a / b`. Do this without using the `/` operator.

print("# 2 Integer division Game")
a = int(input("Please enter a number"))
b = int(input("Please enter a number"))
x=0
y=0
total=1
remanente=0

for x in range(0,a):
    a = a - b
    if a<=0:
        if a==0:
            remantente=0
            break
        remanente=-a
        break
    else:
        total=total+1

z=remanente*10

residue=0

for x in range(0,z):
    z = z - b
    if z<0:
        break
    else:
        residue = residue + 1

print("Division: " + str(total) + "." + str(residue))

#3. Exponentiation is repeated multiplication. Write a script that takes as input two positive integers, `a` and `b`, and returns `a ** b`. Do this without using the `**` operator.

print("# 3 Exponentiation Game")
a = int(input("Please enter a number a: "))
b = int(input("Please enter a number b: "))
x=0
total=1
for x in range(0,b):
    total = total * a
print("Exponentiation: " + str(total))

#4. For two integers, `a` and `b`, `b` divides `a` if `a / b` has no remainder. Write a script that takes as input two positive integers, `a` and `b`, and says whether `b` divides `a`.

print("# 4 a and b, divides a if a/b no remainder")
a = int(input("Please enter a number a: "))
b = int(input("Please enter a number b: "))

remainder = a % b

if remainder == 0:
    total = b/a
    print("B divides A")

#5 5. `while` loops and conditionals give you a lot of power. Try and create a game where a user is repeteadly asked to guess a number. If they get it wrong, they are asked to guess again, and if they are correct, they are told and the game ends. For extra credit, have the game tell the user whether their guess was high or low.

print("# 5 Guess Game")
import random


y = random.randint(1,100)
x = int(input("Please enter a number 1 and 100: "))
count = 1
print(y)
while x != y:
    if x > y:
        print("You are too high.")
    elif x < y:
        print("You are too low.")
    x = int(input("Please enter another number: "))
    count += 1
print("You are correct! That only took " + str(count) + " guesses!")
