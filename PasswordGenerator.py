import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
     
print("Welcome to the PyPassword Generator!")
random_leght=int(input("Would you like random length? Press 1 Yes or 0 for No\n"))

if random_leght==0:
    num_letters= int(input("How many letters would you like in your password?\n")) 
    num_symbols = int(input("How many symbols would you like in your password?\n"))
    num_numbers = int(input("How many numbers would you like in your password??\n"))
else:
    num_letters=6
    num_symbols=6
    num_numbers=6
for letter in letters:
  rand_letter = random.sample(letters,num_letters)  
     
for symbol in symbols:
  rand_symbol = random.sample(symbols, num_symbols)
     
for number in numbers:
  rand_number = random.sample(numbers, num_numbers)

password_list = (rand_letter + rand_symbol + rand_number)
random.shuffle(password_list)     
     
final_password = ''.join(password_list)
print(final_password)
