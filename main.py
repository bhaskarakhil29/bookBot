def count_words(words):
    return len(words)

def words_in_book(fileContents):
    return fileContents.split()

def count_letters(words):
    letters_dict = {}

    for word in words:
        for ch in word.lower():
            if ch in letters_dict.keys():
                letters_dict[ch] += 1
            else:
                letters_dict[ch] = 1
    return letters_dict
    
def make_a_char_list(num_letters):
    char_count_list = []
    for letters in num_letters.keys():
        if (letters.isalpha()):
            char_count_list.append((letters,num_letters[letters]))
    return char_count_list

def generate_report(num_words, sorted_letter_list):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for letter_count_pair in sorted_letter_list:
        print(f"The {letter_count_pair[0]} character was found {letter_count_pair[1]} times")
    
    print(f"--- End report ---")
with open("books/frankenstein.txt") as f:
    fileContents = f.read()
    words = words_in_book(fileContents)
    num_words = count_words(words)
    num_letters = count_letters(words)
    only_alpha_letters = make_a_char_list(num_letters)
    only_alpha_letters.sort(key=lambda a:a[1],reverse=True)
    generate_report(num_words,only_alpha_letters)
    