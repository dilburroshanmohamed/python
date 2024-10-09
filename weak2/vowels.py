text = input('Enter text: ')
print("The vowels are:")
for letter in text:
    if letter in 'aeiouAEIOU':  
        print(letter)
