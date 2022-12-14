# Text Generator project
# Submitted by Chris Freeman
# Stage 5 - Generate Full Sentences

from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict, Counter
from random import choice, choices


# checks word and flags is capitalised.
def start_word(token):
    if token[0].isupper():
        return True
    else:
        return False


# checks word and flags if sentence-ending punctuation is present.
def end_word(token):
    if token[-1] in ".!?;:":
        return True
    else:
        return False


corpus_file = input()
with open(corpus_file, "r", encoding="utf-8") as f:
    raw_text = f.read()
token_list = WhitespaceTokenizer().tokenize(raw_text)
bigram_list = []
for i in range(len(token_list)-1):
    bigram_list.append((token_list[i], token_list[i+1]))
bigram_dict = defaultdict(list)
for head, tail in bigram_list:
    bigram_dict[head].append(tail)
model_dict = {}
for head in bigram_dict.keys():
    model_dict.setdefault(head, Counter(bigram_dict[head]))
word = choice(token_list)
for _ in range(10):
    sentence = []
    sentence_length = 0
    assembling = True
    while assembling:
        tail_dict = model_dict[word]
        tail_list = list(tail_dict.keys())
        tail_weights = list(tail_dict.values())
        next_word = choices(tail_list, weights=tail_weights, k=1)[0]
        if sentence_length == 0:        # starting a sentence?
            if not start_word(word):    # Yes, then is it Capitalised?
                word = next_word            # No - ignore and move on...
                continue
            else:
                if end_word(word):          # Yes - is it also punctuated?
                    word = next_word            # Yes - ignore and move on...
                    continue
            sentence.append(word)       # So, a start word has been found
            word = next_word            # OK to extend the sentence
            sentence_length += 1
        else:                           # Sentence has already started
            if sentence_length >= 4:    # is the sentence long enough yet?
                if end_word(word):      # Yes - then is this punctuated?
                    assembling = False      # Yes. End this sentence.
            sentence.append(word)       # extend the sentence some more
            word = next_word
            sentence_length += 1
    for w in sentence:
        print(w, end=' ')
    print()
