while True:
    word = input("Enter a word (or type 'quit' to exit): ")
    if word == "quit":
        print("Exiting the program.")
        break
    length = 0
    for _ in word:
        length += 1
    print("The length of the word is:", length)
