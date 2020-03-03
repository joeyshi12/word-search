import enchant
import time
from collections import deque
from exception.InvalidInputException import InvalidInputException

def is_valid_word(word: str) -> bool:
    """returns true if word is in the Canadian english dictionary; else, returns false"""
    if word == '':
        return False
    else:
        dictionary = enchant.Dict("en_CAN")
        return dictionary.check(word)

def search_words(chars: list, n: int) -> list:
    """returns a list of all possible words from chars with length n
    raise InvalidInputException if chars is not a list of characters"""
    for char in chars:
        if len(char) != 1:
            raise InvalidInputException
    retVal = []
    visited = set()
    queue = deque([{'word' : '', 'chars' : chars}])
    while queue:
        t = queue.pop()
        if len(t['word']) == n:
            if is_valid_word(t['word']):
                print(t['word'])
                retVal.append(t['word'])
        else:
            for i in range(len(t['chars'])):
                next_word = t['word'] + t['chars'][i]
                next_chars = t['chars'][:i] + t['chars'][i+1::]
                if next_word not in visited:
                    visited.add(next_word)
                    queue.appendleft({'word' : next_word, 'chars' : next_chars})
    return retVal

if __name__ == '__main__':
    while True:
        input_chars = input("Input Spaced Out Characters: ")
        chars = input_chars.split()
        input_int = input("Input Length of Word: ")
        n = int(input_int)

        print("All possible words:")
        start_time = time.time()
        search_words(chars, n)
        end_time = time.time()
        print("Runtime = %f seconds" %(end_time - start_time))
