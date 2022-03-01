import nlp.load as load
import dust, err
import spellcheck as spell

def not_in_word(text, to_replace):
    if not text.replace(to_replace, ""): return True
    if text.replace(to_replace, "")[0] == " ": return True

def match(words, wdict):
    for (i, j) in wdict.items():
        
        if words.startswith(i) and not_in_word(words, i): return (i, i)
        else:
            for k in j:
                if words.startswith(k) and not_in_word(words, k):
                    print(i)
                    return (i, k)
        
def parse_dt(words, word_to_remove, wtm_type, error_message, data):
    if word_to_remove == None: 
        err.arg_err(error_message)
        return
    
    data << dust.Dust(wtm_type, word_to_remove[0])
    return words.replace(word_to_remove[1], "").strip()

def parse(c):
    words = spell.auto(c.strip().lower())
    data = dust.DustStr()
    
    if words in load.SHORTHAND:
        data << load.SHORTHAND[words]
        return data
        
    words = parse_dt(words, # VERB
             match(words, load.VERB),
             "verb",
             "You forgot to use a verb in your command",
             data)
    
    words = parse_dt(words, # NOUN
             match(words, load.NOUN),
             "noun",
             "You forgot to use a noun in your command",
             data)
        
    return data