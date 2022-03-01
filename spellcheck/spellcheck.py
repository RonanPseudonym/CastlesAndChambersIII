from cgitb import small

from numpy import isin
import spellcheck.levenshtein as lev
import spellcheck.soundex as soundex
import nlp.load as load

words = []

for tl in [load.NOUN, load.VERB]:
    for (i, j) in tl.items():
        words.append(i)
        words += j
        
for i in words:
    if " " in i:
        words.remove(i)
        words += i.split(" ")
        
    if not i.strip():
        words.remove(i)
            
def autoword(word):
    sdx_words = []
    sdx_word = soundex(word)
    
    for i in words:
        if word == i: return i
        elif soundex(i) == sdx_word:
            sdx_words.append(i)
            
    choose_from = sdx_words if sdx_words else words
    
    smallest = {"word":None, 
                "diff":None}
    
    for i in choose_from:
        diff = lev.leven(i, word)
        if smallest["diff"] == None or diff < smallest["diff"]:
            smallest["word"] = i
            smallest["diff"] = diff
            
    return smallest["word"]
       
def auto(*args):
    if len(args) == 1 and isinstance(args[0], str):
        words = args[0].split(" ")
        for i, j in enumerate(words): words[i] = autoword(j)
        return " ".join(words)