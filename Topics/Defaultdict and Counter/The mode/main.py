from collections import Counter

word_list = input().split()
freq_counter = Counter(word_list)
print(freq_counter.most_common(1)[0][0])