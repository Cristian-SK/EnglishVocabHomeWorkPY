#English Vocabulary Homework
#add "un"

def add_prefix_un(a):
    return ''.join(['un',a])



print(add_prefix_un("happy"))

#adds prefix, to the words that follow

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return '::'.join([prefix]+[prefix + word for word in vocab_words[1:]])


print(make_word_groups(['en','close','joy','lighten']))


#Removes Suffix
def remove_suffix_ness(word):
    if word.endswith('iness'):
        return word[:-5] + 'y'
    elif word.endswith('ness'):
        return word[:-4] + 'y '
    else:
        return word

print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("Sadness"))

#Extract and transform a word

def adjective_to_verb(sentence,index):
    sentsplit = sentence.split()
    return sentsplit[index] + 'en'

print(adjective_to_verb('I need to make that bright', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))
