import sys
import time
from collections import defaultdict



class Trie:

    def __init__(self):
        self.root = defaultdict()

    def insert(self, word):
        current = self.root
        for _ in word:
            current = current.setdefault(_, {})
        current.setdefault("done")

    def search(self, word):
        current = self.root
        for _ in word:
            if _ not in current:
                return False
            current = current[_]
        if "done" in current:
            return True
        return False


def search_trie(word, t):
    start_time = time.process_time()
    find_anagrams(list(word), 0, len(word) - 1)
    final_anagrams = []

    for _ in set(anagrams):
        if t.search(_):
            final_anagrams.append(_)
    if len(set(final_anagrams)) == 0:
        print(
            "No anagrams found for " + str(word) + " in " + str(int((time.process_time() - start_time) * 1000)) + " ms")
    else:
        print(str(len(set(final_anagrams))) + " Anagrams found for " + str(word) + " in " + str(
            int((time.process_time() - start_time) * 1000)) + " ms")
        print(', '.join(set(final_anagrams)))

def find_anagrams(word, l, r):
    if l == r:
        anagrams.append(''.join(word))
    else:
        for _ in range(l, r + 1):
            word[l], word[_] = word[_], word[l]
            find_anagrams(word, l + 1, r)
            word[l], word[_] = word[_], word[l]


def load_dictionary(file):
    dictionary_words = []
    dict_file = open(file, "rb")
    for line in dict_file:
        dictionary_words.append(line.decode("utf-8").rstrip("\n").lower())
    return dictionary_words

def driver_function(arguments):
    start_time = time.process_time()
    dictionary_word_list = load_dictionary(str(arguments[1]))
    print("Dictionary loaded in " + str(int((time.process_time() - start_time) * 1000)) + " ms")
    t = Trie()
    for word in dictionary_word_list:
        t.insert(word)
    while True:
        print("AnagramFinder>")
        word = input().strip()
        anagrams.clear()
        if str(word.lower()) == "exit":
            return exit(0)
        search_trie(word.lower(), t)



def main():
    print("Welcome to the Anagram Finder")
    print("-----------------------------")
    driver_function(sys.argv)



if __name__ == "__main__":
    anagrams = []
    main()

# Bug fixes from Version - 1
# 1. Didn't convert the words in the dictionary to lower cases. Now the words in the dictionary.txt file are first converted into lower case, and then stored in the python dictionary.
# 2. If the word is found twice in the dictionary, the code printed the word twice. But we need to print it only once.

# Sample Test Cases
# 1. z - we have Z and z in the dictionary file.
# 2. aa - There are two anagrams for this word 'aa'. 'aa' and 'aa'. These are formed by swapping two letters. But we just need to consider them as one anagram.
