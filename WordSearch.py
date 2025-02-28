import time
import itertools

with open("words.txt") as file:
    word_set = set(file.read().split())


def search_words(chars: list[str], n: int) -> None:
    for combination in itertools.combinations(chars, n):
        candidate = "".join(combination)
        if candidate in word_set:
            print(candidate)


def main():
    input_chars = input("Characters: ")
    chars = list(input_chars.lower())
    input_size = input("Length of word: ")
    n = int(input_size)
    print("All possible words: ")
    start_time = time.time()
    search_words(chars, n)
    runtime = time.time() - start_time
    print(f"Runtime = {runtime} seconds")


if __name__ == '__main__':
    main()
