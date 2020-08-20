import sys
import time

def search_dictionary(word, dictionary_word_list):
    start_time = time.process_time()
    find_anagrams(list(word), 0, len(word) - 1)
    final_anagrams = []
    for _ in set(anagrams):
        for element in dictionary_word_list:
            if _ == element.decode('utf-8').rstrip('\n'):
                final_anagrams.append(element.decode('utf-8').rstrip())
    if len(final_anagrams) == 0:
        print(
            "No anagrams found for " + str(word) + " in " + str(int((time.process_time() - start_time) * 1000)) + " ms")
    else:
        print(str(len(final_anagrams)) + " Anagrams found for " + str(word) + " in " + str(
            int((time.process_time() - start_time) * 1000)) + " ms")
        print(', '.join(final_anagrams))

def find_anagrams(word, l, r):
    if l == r:
        anagrams.append(''.join(word))
    else:
        for _ in range(l, r + 1):
            word[l], word[_] = word[_], word[l]
            find_anagrams(word, l + 1, r)
            word[l], word[_] = word[_], word[l]


def load_dictionary(file):
    with open(file, "rb") as dict_file:
        dictionary_words = dict_file.readlines()
    return dictionary_words

def driver_function(arguments):
    start_time = time.process_time()
    dictionary_word_list = load_dictionary(str(arguments[1]))
    print("Dictionary loaded in " + str(int((time.process_time() - start_time) * 1000)) + " ms")
    while True:
        print("AnagramFinder>")
        word = input().strip()
        anagrams.clear()
        if str(word) == "exit":
            return exit(0)
        search_dictionary(word, dictionary_word_list)


def main():
    print("Welcome to the Anagram Finder")
    print("-----------------------------")
    driver_function(sys.argv)



if __name__ == "__main__":
    anagrams = []
    main()
