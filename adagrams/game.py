import random



LETTER_SCORE_CHART = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D","G"],
    3: ["B","C","M","P"],
    4: ["F","H","V","W","Y"],
    5: ["K"],
    8: ["J","X"],
    10:["Q","Z"]
}


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
    # convert the LETTER_POOL into a letter_list which contains all the available letters
    letter_list = []
    for (letter, letter_freq) in LETTER_POOL.items():
        letter_list += letter * letter_freq
    
    # * pop one random letter from the letter_list and append it to the newly created list(letters), repeat for 10 times.
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
    # if word is empty string, return 0
    if word == "":
        return 0
    
    # caculate the score according to the LETTER_SCORE_CHART
    total_score = 0
    for letter in word.upper():
        for (score, letters) in LETTER_SCORE_CHART.items():
            if letter in letters:
                total_score += score
    # add 8 more points if the length of word is more than 7
    if len(word) >= 7:
        total_score += 8
        
    return total_score


def get_highest_word_score(word_list):
    # create a dictionary(scores) in which the key is the word, value is its score. 
    # find out the highest score of all the scores by using max()
    scores = {}
    for word in word_list:
        scores[word] = score_word(word)
    highest_score = max(scores.values())
    
    # find out all the words whose scores are the same as the highest score, and put them in a list.
    highest_score_words = []
    for word, score in scores.items():
        if score == highest_score:
            highest_score_words.append(word)

    #check the length of all the highes score words and return the correct one
    for target_word in highest_score_words:
    #loop through all the words, any word that has a length of 10 will be the highest score word, or the first length-10 one if there are multiple
        if len(target_word) == 10:   
            return (target_word, highest_score)
    # if none of the words has a length of 10, the one of shorest length is the highest score word.
    # I googled the following way to find the shortest word of a list. 
    return (min(highest_score_words, key =len),highest_score)





