#FL_warmup
# 1. Look at the code in `warmup3.py`. As in `warmup2.py`, we are printing a list. This time, though, it is displayed differently. What do you think will be printed to the console? Why does it look like this, as opposed to the format we saw in `warmup2.py`?

print("#1 -------------------")
my_list = ['hello', 'there', 'python', list('list'), '!']
for element in my_list:
    print(element)

#   2. Change the code in `warmup3.py` so that it also prints the indices of the elements in `my_list`.

print("#2 -------------------")
my_list, idx = ['hello', 'there', 'python', list('list'), '!'],0
while idx < len(my_list):
    print(idx,my_list[idx])
    idx+=1
   
#3. Add an `if` to the for loop so that only the elements at odd indices are printed, along with their index.

print("#3 -------------------")
my_list, idx = ['hello', 'there', 'python', list('list'), '!'],0
while idx < len(my_list):
    if idx%2!=0:
        print(idx,my_list[idx])
    idx+=1

# 4. Change your if statement to only print the elements that are longer than 4 characters, again along with their index. Why can you just `len()` to do this?

print("#4 -------------------")
my_list, idx = ['hello', 'there', 'python', list('list'), '!',"asd"],0
while idx < len(my_list):
    if len(my_list[idx])>4:
        print(idx,my_list[idx])
    idx+=1

#5. Now, instead of just printing the elements to the console, change the script so that it adds the elements that are longer than 4 characters to a new list, called `longer_elements`. This means that you will have to create an empty list with that name before the list. Print `longer_elements` at the end of the script

print("#5 -------------------")
new_list=[]
my_list, idx = ['hello', 'there', 'python', list('list'), '!',"asd"],0
while idx < len(my_list):
    if len(my_list[idx])>4:
        new_list.append(my_list[idx])
    idx+=1
print(new_list)

# 6. Try printing `longer_elements` inside the for loop you created above. What do you expect to see when you run your script? Make sure you understand why you're getting this output.

print("#6 -------------------")
new_list=[]
my_list, idx = ['hello', 'there', 'python', list('list'), '!',"asd"],0
while idx < len(my_list):
    if len(my_list[idx])>4:
        new_list.append(my_list[idx])
    idx+=1
print(new_list)
print("The strings stored are only with len>4")


#7. Add the line `user_number = int(input('Min length to be printed: '))` to the top of `warmup3.py`. Now, change your script so that it only adds words that are longer than a user inputted number to `longer_elements`. You can include the statement printing `longer_elements` inside the loop if you want. Print `longer_elements` after the loop.

print("#5 -------------------")
new_list=[]
my_list, idx = ['hello', 'there', 'python', list('list'), '!',"asd"],0
while idx < len(my_list):
    if len(my_list[idx])>4:
        new_list.append(my_list[idx])
    idx+=1
print(new_list)