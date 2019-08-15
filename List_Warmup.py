#List Warm-up
#1. Look at the code in `warmup2.py`. What is going to be #printed to the console? Change the print statement so that the first element in `my_list`, `1`, is printed. What's the reason that we have to make this change?

my_list = [1, 'hello', 2, 'there', 3, 'list']
print("When you put 1 is printed hello because No=0 si 1 and No=1 is hello")
print(my_list[0])


#2. Now change the print statement so that only the words `"hello"`, `"there"`, and `"list"` are grabbed from `my_list` and printed. You should do this with indexing. What do you expect the type of the thing that is printed to be?

my_list = [1, 'hello', 2, 'there', 3, 'list']
print(my_list[1::2])


#3 3. Put a line between lines 1 and 2 that adds the number `4` to the end of `my_list`.

my_list = [1, 'hello', 2, 'there', 3, 'list']
my_list.insert(7,4)
print(my_list)

#4. Change the print statement so that only the numbers in `my_list` are printed. Again, do this with indexing.

print(my_list[0::2])

# 5. Add another line after the one with `append()` that [removes](https://docs.python.org/3/tutorial/datastructures.html) the word "list" from `my_list`. What do you think `my_list` looks like now? Print it to check.

my_list = [1, 'hello', 2, 'there', 3, 'list']
my_list.append(4)
my_list.remove(3)
print(my_list)

# 6. Now, using indexing, print only the elements in `my_list` at odd indices. You should see: `['hello', 'there', 4]` Is this what you'd expect? If not, consider how you've transformed `my_list`, and convince yourself that this makes sense.

print(my_list[1::2])

# 7. Remove the lines that modify `my_list`. Now add the line `user_input = input('Add the number 4 to mylist (y/n)? ')` at the top of `warmup2.py`. Modify the rest of `warmup2.py` so that if the user inputs a `y`, it will add the number 4 to the end of `my_list`, and otherwise it will do nothing. At the end, print `my_list`. Play around with different inputs. Do they work the way you'd expect?

my_list = [1, 'hello', 2, 'there', 3, 'list']
user_input = input('Add the number 4 to mylist (y/n)')
if user_input=="y":
    print("Yes")
    my_list.append("4")
print(my_list)

# 8. Modify `warmup2.py` so that it will accept any user inputted string. If the length of that string is less than 8, your script should add it to `my_list`, and other wise it should add the number 4 to the list. Print `my_list` at the end to see what it is.

my_list = [1, 'hello', 2, 'there', 3, 'list']
user_input = input('Add the number 4 to mylist (y/n)')
if len(user_input)<8:
    my_list.append(user_input)
else:
    my_list.append("4")
print(my_list)