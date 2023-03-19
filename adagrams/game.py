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

SCORE_CHART = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D","G"],
    3: ["B","C","M","P"],
    4: ["F","H","V","W","Y"],
    5: ["K"],
    8: ["J","X"],
    10:["Q","Z"]
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
    # if word is empty string, return 0
    if word == "":
        return 0
    
    # caculate the score according to the SCORE_CHART
    total_score = 0
    for letter in word.upper():
        for (score, letters) in SCORE_CHART.items():
            if letter in letters:
                total_score += score
    # add 8 more points if the length of word is more than 7
    if len(word) >= 7:
        total_score += 8
        
    return total_score


def get_highest_word_score(word_list):
    scores = {}
    for word in word_list:
        scores[word] = score_word(word)
    highest_score = max(scores.values())
    
    highest_score_words = []
    for word, score in scores.items():
        if score == highest_score:
            highest_score_words.append(word)
    
    for target_word in highest_score_words:
        if len(target_word) == 10:
            return (target_word, highest_score)
    return (min(highest_score_words, key =len),highest_score)





