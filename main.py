#!/usr/bin/env python3
import string

def word_count(book):
    return len(book.split())


def char_count(book):
    char_dict = {}
    for char in book:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1


    return char_dict

def alpha_count(book):
    characters = char_count(book)
    alphabets = string.ascii_lowercase
    alpha_list = list()
    for a in alphabets:
        alpha_list.append(a)


    for char,count in characters.items():
        if char in alpha_list:
            print(f"The '{char}' character was found {count} times")
    



def main():
    book = "./books/frankenstein.txt"

    with open(book) as file:
        book_content = file.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(book_content)} words found in the document")
    alpha_count(book_content)
    print("--- End report ---")
    

if __name__ == '__main__':
    main()
