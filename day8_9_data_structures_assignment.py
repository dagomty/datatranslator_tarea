#data_structures_assignment.md

#1. Tuple warm up:
#    1. Look at the code in `warmup1.py`. What do you think this `tuple` is storing? If I tell you it is storing the four suits of a standard card deck, can you tell me why it's appropriate that I use a `tuple` for this?

my_tup = ('diamond', 'club', 'spade', 'heart',[])
print(my_tup[::2])
print("#Tuple is storing the kinds of cards, and it's appropriate to use concept of tuple because there are classifications")

#    2. Run `warmup1.py`, and note what it originally prints.

print("#Tuple prints 'diamond', 'spade'")

#    3. Now, change the print statement to print out the 1st element in the `tuple` (e.g. `diamond`).

print(my_tup[0])

#    4. Now, change the print statement to print out every other element.

print(my_tup)

#    5. Why are we able to grab individual elements (or every other element) from the `tuple` just as if it is a `list`?

print("# Just as a list, we can store anything, and tuples elements can be accesed by indexing, and using loops.")

#    4. Now, alter it so that it prints out each of the elements, one at a time on a new line. Use a `for` loop to do this. Why are we able to use a `for` loop on the `tuple` like this?

for x in range(0, len(my_tup)):
    print("#Element No. "+str(x)+" "+str(my_tup[x]))

#    5.  Now, say that I want to add a new suit to my card deck. Let's call it `gorilla` (who doesn't like a gorilla suit). How would I do this? Why can't we use `append` on a `tuple` like we can on a `list`?

my_tup[4].append("new suit: ")
my_tup[4].insert(1,"gorilla")
print(my_tup)

#2. Dictionary warm up:
#    1. Don't run the code yet! First, examine the code in `warmup2.py`. What do you think it will print when run? Why does it print this?

print(" - - - - - - - - DIctionary Warm Up - - - - - - - - - - ")
my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'New York City'}
for element in my_dct:
    print(element)

print("I think code will print Texas, Austin, Indiana, Indianapolis,,, and each element in the list")

#    2. Why is it appropriate to use a dictionary in this scenario?

print("Because it is a list with states and we want to associate each one with the name of its capitals ")


#    3. Okay, so you will by now have noticed what it printed. Change the `element` variable that is storing the key through each iteration of the loop to be a more descriptive variable name.
    
print("Diccionario es: "+str(my_dct))
for element in range(8):
    my_dct.update({"name of state":element})
print("Diccionario cambió a: "+str(my_dct))

#    4. Now, change the loop so that it not only prints the `key` at every iteration, but both the `key` and `value` (i.e. print the state as well as the city in the loop).


#    5. Build another dictionary that stores the state and capital of the state you grew up in, as well as the state and capital of the state your neighbor grew up in. Call this `neighbor_dct`, and put it on the second line of the `warmup2.py` script (before the `for` loop).
#    6. Now, add a line before the for loop that adds the key-value pairs in `neighbor_dct` to `my_dct`. `my_dct` should now have the contents from it's previous state and also `neighbor_dct`.
#    7. Modify `warmup2.py` to take in a user inputted state. Then, take that user inputted state, and if it is in `my_dct`, print out it's capital. If it's not, then print out 'Capital not found!'.
#    8. Now, modify `warmup2.py` to ask the user for a state name. If it is not already in `my_dct`, have your script prompt the user for a capital to associate with that state name.