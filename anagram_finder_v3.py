import sys
import time
from collections import defaultdict, Counter



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

def find_anagrams(word, t):

    def recursive_call(letter_counts, anagram_letter_list, root, word_len):
        if "done" in root.keys() and len(anagram_letter_list) == word_len:
            word = ''.join(anagram_letter_list)
            yield word
        for letter, trie_dict in root.items():
            count = letter_counts.get(letter, 0)
            if count == 0:
                continue
            letter_counts[letter] = count - 1
            anagram_letter_list.append(letter)
            for word in recursive_call(letter_counts, anagram_letter_list, trie_dict, word_len):
                yield word
            anagram_letter_list.pop()
            letter_counts[letter] = count

    letter_counts = Counter(word)
    for _ in recursive_call(letter_counts, [], t.root, len(word)):
        yield _


def load_dictionary(file):
    dictionary_words = []
    dict_file = open(file, "rb")
    for line in dict_file:
        dictionary_words.append(line.decode("utf-8").rstrip("\n").lower())
    return dictionary_words

def driver_function(arguments):
    start_time = time.process_time()
    dictionary_word_list = load_dictionary(str(arguments[1]))
    t = Trie()
    for word in dictionary_word_list:
        t.insert(word)
    print("Dictionary loaded in " + str(int((time.process_time() - start_time) * 1000)) + " ms")
    while True:
        print("AnagramFinder>")
        start_time = time.process_time()
        word = input().strip()
        final_anagrams.clear()
        if str(word.lower()) == "exit":
            return exit(0)
        for _ in find_anagrams(word, t):
            final_anagrams.append(_)
        if len(set(final_anagrams)) == 0:
            print(
                "No anagrams found for " + str(word) + " in " + str(
                    int((time.process_time() - start_time) * 1000)) + " ms")
        else:
            print(str(len(set(final_anagrams))) + " Anagrams found for " + str(word) + " in " + str(
                int((time.process_time() - start_time) * 1000)) + " ms")
            print(', '.join(set(final_anagrams)))



def main():
    print("Welcome to the Anagram Finder")
    print("-----------------------------")
    driver_function(sys.argv)



if __name__ == "__main__":
    anagrams = []
    final_anagrams = []
    main()

# Bug fixes from Version - 2
# 1. The approach in this version is totally different in finding the anagrams in dictionary. The previous version performed bad when the length of the word exceeds 10. I changed the approach of finding the anagrams and this has drastically reduced the search time.
#
# Test Case
# 1. aploperistomatous - Code takes ~15ms to find the anagrams of this word in the dictionary.
