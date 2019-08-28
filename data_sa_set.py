
#3. Set warm up:

#    1. Run `warmup3.py`. Why are we able to use a `for` loop to print out the elements of `my_set`?

print("- - - - SET PROBLEMS- - - - - - - - ")

my_set = {2, 3, 5}
for num in my_set:
    print(num)


#    2. On the second line, create a new set (you'll have to move the `for` and everything below it down one line). Call it `my_fav_primes`, and enter 3 of your favorite prime numbers.

my_fav_primes = {2,3,5}
my_set = {2, 3, 5}
for num in my_set:
    print(num)


#    3. Now, move everything down one more line, and create a third set that gives the numbers that `my_set` and `my_fav_primes` have in common. Alter the `for` loop to print out the numbers in this new `set`. 

my_fav_primes = {2,3,7}
my_set = {2, 3, 5}
in_common = {}
in_common = my_fav_primes & my_set

print("in common: ",in_common)
 
#    4. Change your code to get only the numbers that are in `my_set` but aren't in `my_fav_primes`. Store these in a third set, and alter the `for` loop to print out the numbers in this third set.

print("Ex 4-----")
my_set = {2, 3, 5,9,13}
my_fav_primes = {2,3,7}

insetnotinmyfav = {}
insetnotinmyfav = my_set - my_fav_primes & my_set

print(insetnotinmyfav)

#    5. Create a new set with the elements from both `my_fav_primes` and `my_set`, and name it `my_tot_primes`. Alter the `for` loop to print out its values.
print("Ex 5----- Both ")
my_set = {2, 3, 5,9,13}
my_fav_primes = {2,3,7}

my_tot_primes = {}
my_tot_primes = my_set| my_fav_primes

print(my_tot_primes)

#    6. Now, modify `warmup3.py` to take in a user inputted prime, and then add it to `my_tot_primes`.

print("Ex 6----- INPUT ")

inus = input("Dime número primo")

my_tot_primes.add(str(inus))


print(my_tot_primes)
