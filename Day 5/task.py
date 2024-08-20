import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#easy password
#Choose x letters
range_letters = range(1, nr_letters + 1)
pass1 = ""
for letter in range_letters:
    pass1+=random.choice(letters)
#Choose x numbers
range_numbers=range(1,nr_numbers+1)
for number in range_numbers:
    pass1+=str(random.choice(numbers))
#Choose x symbols
range_symbols=range(1,nr_symbols+1)
for symbol in range_symbols:
    pass1+=str(random.choice(symbols))

print(pass1)

#difficult password
range_letters = range(1, nr_letters + 1)
pass1 = ""
for letter in range_letters:
    pass1+=random.choice(letters)
#Choose x numbers
range_numbers=range(1,nr_numbers+1)
for number in range_numbers:
    pass1+=str(random.choice(numbers))
#Choose x symbols
range_symbols=range(1,nr_symbols+1)
for symbol in range_symbols:
    pass1+=str(random.choice(symbols))

password=list(pass1)
password=print(''.join(random.sample(password,len(password))))

