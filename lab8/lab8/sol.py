import nltk
from nltk import bigrams
from nltk.corpus import brown
from collections import Counter

my_words = ['there', 'are', 'too', 'much', 'people']
my_letters = ['c', 'o', 'l', 'l', 'e', 'c', 't', 'i', 'o', 'n', 's']
br_words = brown.words()

#unigrams 
freq_dist = nltk.FreqDist([w.lower() for w in br_words])
total = 0
for word in my_words:
    if word in freq_dist:
    	total = total + freq_dist[word]
print('Unigrams:')
for word in my_words:
    if word in freq_dist:
        print('(' + word + '):', '  freq:', freq_dist[word], '   prob:', freq_dist[word]/total)
    else:
        print('(' + word + '):', '  freq:', 0, '   prob:', 0)
    
# bigrams
bigrams = []
for sent in brown.sents():
	bigrams.extend(nltk.bigrams(sent, pad_left=True, pad_right=True))

bigram_cnt = Counter(bigrams)
bi_total = len(brown.words()) - len(brown.sents())
bigrams = nltk.bigrams(my_words, pad_left=True, pad_right=True)

print('Bigrams:')
for bg in bigrams:
	if bg[0] != None and bg[1] != None:
		prob = bigram_cnt[bg] / bi_total
		print(str(bg), "prob:", str(prob))

#trigrams: computes the frequency of my_letters' triples in leading 100 words
trigrams = []
tr_total = 0
for word in brown.words()[:100]:
	trigrams.extend(nltk.trigrams(word))
	if len(word) >= 3:
		tr_total = tr_total + len(word) - 2

trigram_cnt = Counter(trigrams)
trigrams = nltk.trigrams(my_letters)

print('Trigrams:')
for tr in trigrams:
	if tr[0] != None and tr[1] != None and tr[2] != None:
		prob = trigram_cnt[tr] / tr_total
		print(str(tr), "prob:", str(prob))
