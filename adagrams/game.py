import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letter_list = []
    for (letter, letter_freq) in LETTER_POOL.items():
        letter_list += [letter] * letter_freq

    letters =[]
    for i in range(10):
        letter = letter_list.pop(random.randrange(len(letter_list)))
        letters.append(letter)
    return letters


def uses_available_letters(word, letter_bank): 
    # create two empty dictionaries, in order to convert both the word and letter_bank into dictionaries.
    letter_bank_dict = {}
    word_dict ={}
    # convert letter_bank(list) into a dictionary
    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1
        else:
            letter_bank_dict[letter] = 1
    
    # convert word(string) into a dictionary
    for char in word.upper():
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1
    
    # check if every letter in the word is also in the dictionary and of right quantity. 
    for word_letter in word_dict:
        if word_letter not in letter_bank_dict or word_dict[word_letter] > letter_bank_dict[word_letter]:
            return False
    return True



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


