drop = "aeiouyhw"

digit_hierarchy = ["bfpv",
                   "cgjkqsxz",
                   "dt",
                   "l",
                   "mn",
                   "r"
]

def get_from_hierarchy(letter):
    for i, j in enumerate(digit_hierarchy):
        if letter in j: return i + 1
        
    raise ValueError(f"Letter '{letter}' not in digit hierarchy")

def soundex(word, digit_count = 10):
    first = word[0].upper()
    word = word[1:]
    
    for i in drop:
        word = word.replace(i, "")
                        
    word = "".join(list(map(lambda x: str(get_from_hierarchy(x)), word)))
    word = first + word
    
    return word + "0"*(digit_count-len(word))

def soundex_iterable(iterable, digit_count = 10):
    i2 = []
    
    for i, j in enumerate(iterable):
        i2.append(soundex(j, digit_count=digit_count))
        
    return i2
        
def soundex_dict(dictionary, digit_count=10):
    keys = soundex_iterable(list(dictionary.keys()), digit_count=digit_count)
    
    d2 = {}
    counter = 0
    for i in dictionary.values():
        d2[keys[counter]] = i
        counter += 1
                
    return d2