from string import ascii_lowercase as alphabet
import config
import os
import json
import heapq
from preprocess import load


def possible_errors(word, english_words):
	possible = set()
	deletions = [word[:i] + word[i+1:] for i in range(len(word)) if word[:i] + word[i+1:] in english_words]
	for i in range(len(word)+1):
		# Add possible additions
		possible.update([word[:i] + letter + word[i:] for letter in alphabet if word[:i] + letter + word[i:] in english_words])
		if i < len(word)-1:
			deletion = word[:i] + word[i+1:]
			if deletion in english_words: possible.add(deletion)
			transposition = word[:i] + word[i+1] + word[i] + word[i+2:]
			if transposition in english_words: possible.add(transposition)
			# Add possible substitutions
			possible.update([word[:i] + letter + word[i+1:] for letter in alphabet if word[:i] + letter + word[i+1:] in english_words])
			# Add possible transpositions
	return possible

def topK(elements, k):
	priority_q = []
	for el in elements:
		if len(priority_q) < k:
			heapq.heappush(priority_q, el)
		elif el[0] > priority_q[0][0]: # Check to replace smallest value
			heapq.heappushpop(priority_q, el)
	return sorted(priority_q, key=lambda x: x[0])


def spell_check(word, english_words):
	if word not in english_words:
		possible = [(english_words[word], word) for word in possible_errors(word, english_words)]
		num_results = 5
		return sorted(topK(possible, num_results), key=lambda x:x[0])
	else:
		return 'The word is properly spelled \n ________'

if __name__ == "__main__":
	dict_file = os.path.join(config.PROCESSED, config.WORD_DICT)
	# if not os.path.exists(dict_file):
		# load.english_words()
	english_words = json.load(open(dict_file))
	while True:
		print "Type in a misspelled word"
		# Possibly limit all words to greater than 3 letters?
		word = raw_input().lower()
		print spell_check(word, english_words)