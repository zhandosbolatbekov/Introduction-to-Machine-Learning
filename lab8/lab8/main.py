from nltk.corpus import brown

cnt = dict()

for each in cnt:
	print(each, str(cnt[each]))

for fileid in brown.fileids()[:1]:
	words_count = len(brown.words(fileid))
	for i in range(0, words_count - 1):	
		x = brown.words(fileid)[i].lower()
		y = brown.words(fileid)[i+1].lower()
		count = cnt.get((x, y))
		if count == None:
			cnt.update([((x, y), 1)])	
		else:
			cnt.update([((x, y), count + 1)])
    
for each in cnt:
	print(each, str(cnt[each]))