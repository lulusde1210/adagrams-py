import random

def draw_letters():
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
    letter_list = []
    for (letter, letter_freq) in LETTER_POOL.items():
        letter_list += letter * letter_freq
    
    letter_bank =[]
    for _ in range(10):
        random_index = random.randrange(len(letter_list))
        letter = letter_list.pop(random_index)
        letter_bank.append(letter)
    return letter_bank

def uses_available_letters(word, letter_bank): 
    letter_bank_dict = {}
    for letter in letter_bank:
        letter_bank_dict[letter] = letter_bank_dict.get(letter,0) +1

    word_dict ={}
    for char in word.upper():
        word_dict[char] = word_dict.get(char,0) + 1
    
    for letter in word_dict:
        word_letter_count = word_dict[letter]
        bank_letter_count = letter_bank_dict[letter] if letter in letter_bank_dict else 0
        if word_letter_count > bank_letter_count:
            return False
    return True

def score_word(word):
    LETTER_SCORE_CHART = {
    1: ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"),
    2: ("D", "G"),
    3: ("B", "C", "M", "P"),
    4: ("F", "H", "V", "W", "Y"),
    5: ("K"),
    8: ("J", "X"),
    10:("Q", "Z")
    }
    if word == "":
        return 0
    
    total_score = 0
    for letter in word.upper():
        for (score, letters) in LETTER_SCORE_CHART.items():
            if letter in letters:
                total_score += score
                break

    if len(word) >= 7:
        total_score += 8
        
    return total_score

def get_highest_word_score(word_list):
    highest_score = 0
    winner_list =[]
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            winner_list = [word]
        elif score == highest_score:
            winner_list.append(word)

    for winner in winner_list:
        if len(winner) == 10:   
            return (winner, highest_score)
    return (min(winner_list, key =len),highest_score)





