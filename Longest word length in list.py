def longest_word(word):
    key_len = len  # Define key_len as the len function
    word = max(word, key=key_len)  # Use key=key_len to compare lengths
    print("Longest word:", word)
    print("length of the longest word is:", len(word))


a = ["book", "calculator", "pen", "pencil", "bag"]
longest_word(a)
