import enchant
import time
from exception.InvalidInputException import InvalidInputException

def is_valid_word(word: str) -> bool:
    """returns true if word is in the Canadian english dictionary; else, returns false"""
    if word == '':
        return False
    else:
        dictionary = enchant.Dict("en_CAN")
        return dictionary.check(word)

def next_words(word: str, chars: list) -> list:
    """returns a list of all unique next possible strings"""
    if not chars:
        return []
    else:
        if chars[0] in chars[1::]:
            return next_words(word, chars[1::])
        else:
            return [word + chars[0]] + next_words(word, chars[1::])

def list_minus(lox: list, loy: list) -> list:
    """returns lox - loy"""
    if not lox:
        return []
    if not loy:
        return lox
    else:
        if lox[0] in loy:
            return list_minus(lox[1::], loy)
        else:
            return [lox[0]] + list_minus(lox[1::], loy)

def search_words(chars: list, n: int) -> list:
    """returns a list of all possible words from chars with length n
    raise InvalidInputException if chars is not a list of characters"""
    def fn_for_word(word: str) -> list:
        if len(word) == n:
            if is_valid_word(word):
                print(word)
                return [word]
            else:
                return []
        else:
            return fn_for_words(next_words(word, list_minus(chars, [char for char in word])))
    def fn_for_words(words: list) -> list:
        if not words:
            return []
        else:
            return fn_for_word(words[0]) + fn_for_words(words[1::])
    for char in chars:
        if len(char) != 1:
            raise InvalidInputException
    return fn_for_word('')

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
