#def my_function(n):
#    if n > 10:
#        for _ in range(n - 9):
#            print('I love Python!!!')
#    else:
#        for _ in range(n):
 #           print('I love Python so much!!!')
#
#inn = int(input("Number: "))
#my_function(inn)

#Biblioteca = []
#Libros = []#

#def update_library(books, library):
#    new_books = []
#    for book in books:
#        print('The book, {} is new!'.format(book))
#        new_books.append(book)
#        library.add(book)
#    print(library)
#    return new_books
    

# Piedra papel o tijera

#def play_rock_paper_scissors(n_rounds):
#    for _ in range(n_rounds):
#        player_1 = input('Player 1 play (r/p/s): ')
#        player_2 = input('Player 2 play (r/p/s): ')
 #   if player_1 == player_2:
 #       print("It's a tie!")
 #   elif player_1 == 'r' and player_2 == 's':
 #       print('Player 1 wins!')
 #   elif player_1 == 'r' and player_2 == 'p':
 #       print('Player 2 wins!')
 #   elif player_1 == 'p' and player_2 == 'r':
  #      print('Player 1 wins!')
   # elif player_1 == 'p' and player_2 == 's':
   #     print('Player 2 wins!')
   # elif player_1 == 's' and player_2 == 'r':
   #     print('Player 2 wins!')
  #  elif player_1 == 's' and player_2 == 'p':
  #      print('Player 1 wins!')
  #  else:
  #      print("Someone didn't play right!")

#play_rock_paper_scissors(1)

#TEXT

 def repeat_list_of_file_line(file_name, line_num, num_copies):
     line = None
     with open(file_name) as f:
         for i, file_line in enumerate(f,1):
            if i == line_num:
                 line = file_line.strip()
    if not line:
        copies_of_line = 'There were not {} lines in the document'.format(line_num)
        else:
            copies_of_line=[line for _ in range(num_copies)]
        return copies_of_line
