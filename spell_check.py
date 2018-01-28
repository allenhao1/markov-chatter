from string import ascii_lowercase as alphabet
import config
import os


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

def load_dict(all_words, txt_file):
	try:
		with open(txt_file, 'r') as f:
			lines = f.readlines()
			for line in lines:
				all_words[line.strip()] = 0.0
	except:
		print 'error loading words'
		exit()

def spell_check(word, english_words):
	if word not in english_words:
		return possible_errors(word, english_words)
	else:
		return 'The word is properly spelled'

if __name__ == "__main__":
	english_words = {}
	load_dict(english_words, os.path.join(config.PROCESSED, 'wordsEn.txt'))
	while True:
		print "Type in a misspelled word"
		word = raw_input().lower()
		print spell_check(word, english_words)