
import data import DICTIONARY, LETTER_SCORES

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY,'r') as f:
        word_list = f.readlines()
    word_list = [x.strip() for x in word_list]
    return word_list


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    total = 0
    for i in word:
        value = LETTER_SCORES.get(i.upper())
        total += value
    return total


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    new_dict={}
    for i in words:
        new_dict[i]=calc_word_value(i)
    keys = new_dict.keys()
    max_value = max(new_dict.values())
    key = [x for x in keys if new_dict[x] == max_value]
    return key[0]

if __name__ == "__main__":
    # run unittests to validate
    pass

