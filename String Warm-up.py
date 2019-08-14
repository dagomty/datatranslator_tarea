# String Warm-up
  #  1. Look at the code in `warmup1.py`. What is the letter at index 14 of `my_str`? Think about this first, then feel free to print just that letter to check your answer.
   
my_str = 'This String was not Chosen Arbitrarily...'
print(my_str.upper())
a=my_str[13]
print("Letter at index 14 is: "+str(a))

  
#2. In line 1 of `warmup1.py`, change the definition of `my_str` to use the contraction "wasn't" instead of "was not". What letter is at index 14 now?
   
my_str = "This String wasn't Chosen Arbitrarily..."
print(my_str.upper())
a=my_str[13]
print("Letter at index 14 is: "+str(a))

#3. Change `warmup1.py` to print `my_str` with only lowercase letters.

my_str = "This String wasn't Chosen Arbitrarily..."
print(my_str.lower())
a=my_str[13]
print("Letter at index 14 is: "+str(a))

# 4. Add a line between lines 1 and 2 that adds the string `"oR wAs it??"` to the end of `my_str`. When you print `my_str` with no uppercase letters now, it should display: `this string wasn't chosen arbitrarily...or was it??`. (**Hint**: use string concatenation with `+=` to redefine `my_str`)

my_str = "This String wasn't Chosen Arbitrarily..."
your_str="oR wAs it??"
sum_str=my_str+your_str
print(sum_str.lower())


#5. Using indexing, print only the `"oR wAs it"` in `my_str`. You're going to have to use `[start_index:end_index]` notation to do this.
print("Ex #5 ---------------")
my_str = "This String wasn't Chosen Arbitrarily..."
your_str="oR wAs it??"
sum_str=my_str+your_str
indexing_str=sum_str[40:52]
print(indexing_str)


#6. Find a different way to index into `my_str` to print only the `"oR wAs it"`. This time, though, print all the letters in uppercase.

print("Ex #6 ---------------")
print(sum_str[-11::].upper())


#7. Add the line `user_input = input('Add "oR wAs it??" (y/n)? ')` at the top of `warmup1.py`. This will prompt the user to enter a `y` or an `n`. Now add an `if` statement to your code that only adds the string `"oR wAs it??"` to `my_str` if the user inputs a `y`. If the user inputs an `n`, don't add `"oR wAs it??"` to `my_str`. Print `my_str` at the end of the script.

print("Ex #7 ---------------")
user_input = input('Add "oR wAs it??" (y/n)? ')

if user_input=="y":
    print(sum_str)
else:
    print(my_str)


#8. Change the first line of `warmup1.py` to `user_input = input('String to add to end of my_str: ')`. Add `user_input` to the end of `my_str` instead of `"oR wAs it??"` and print `my_str`. Note, you'll have to remove the `if` you have in your code from the previous question.

print("Ex #8 ---------------")
user_input = input('String to add to end of my_str: ')
print(my_str+user_input)


# #9. Now, only add `user_input` to `my_str` if it's shorter than 10 characters. No matter what, print `my_str`.

print("Ex #9 ---------------")
user_input = input('New user input: ')
if len(user_input)<10:
    print(my_str+user_input)
else:
    print(my_str)