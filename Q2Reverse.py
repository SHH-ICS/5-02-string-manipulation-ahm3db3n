word = input("Enter a word: ")
reversed_word = "" 
for char in word:  
    reversed_word = char + reversed_word
for char in reversed_word:
    print(char)
