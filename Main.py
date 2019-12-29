import WordSearch as Ws

if __name__ == '__main__':
    while True:
        input_chars = input("Input Spaced Out Characters: ")
        chars = input_chars.split()

        input_int = input("Input Length of Word: ")
        n = int(input_int)

        print("All possible words:")
        Ws.search_words(chars, n)
