import sys
from collections import Counter
import json
import re
import csv
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))
import config


def get_json_name(old_name):
    return old_name.split(".")[0] + ".json"

def english_words(txt_file):
    try:
        # TODO: Take out words with less than 3 letters?
        all_words = {}
        with open(txt_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                all_words[line.strip()] = 0.0
        # Write data to new file
        with open(os.path.join(config.PROCESSED, config.WORD_DICT), 'w') as outfile:
            json.dump(all_words, outfile)
    except:
        print 'error loading words'
        exit()

def movie_lines(lines, dest_name):
    with open(lines,'rb') as tsv_in, open(os.path.join(config.PROCESSED, dest_name), 'wb') as out:
        tsv_in = csv.reader(tsv_in, delimiter='\t')
        for row in tsv_in:
            try:
                out.write(row[4] + '\n')
            except:
                pass

def word_freq(text):
    english_words = json.load(open(os.path.join(config.PROCESSED, config.WORD_DICT)))
    with open(text, 'r') as f:
        for line in f.readlines():
            clean_line = re.sub(r'[^a-zA-Z]', ' ', line)
            words = clean_line.split()
            for word in words:
                if word in english_words:
                    english_words[word.lower()] += 1.0
    # Normalize to obtain probabilities
    wordcount = sum(english_words.values())
    for word in english_words:
        english_words[word] /= wordcount

    with open(os.path.join(config.PROCESSED, config.WORD_DICT), 'w') as outfile:
        json.dump(english_words, outfile)
