from collections import OrderedDict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    #print(f"Word count: {word_count}")
    #print(f"Character count: {character_count}")
    print_data(text, book_path, word_count, character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(string):
    character_count_dict = {}

    for character in string:
        if character.isalpha():
            lowered = character.lower()
            character_count_dict[lowered] = character_count_dict.get(lowered, 0) + 1
    return character_count_dict
    
def sort_data(dict):
    sorted_dict = OrderedDict(sorted(dict.items()))
    return sorted_dict
    
def print_data(text, book_path, word_count, char_count):
    sorted_dict = sort_data(char_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")

    for char in sorted_dict:
        print(f"The '{char}' character was found {sorted_dict[char]} times")
    print("\n--- End report ---")

main()