import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_text = f.read()
    return file_text

def num_of_words():
    # text = get_book_text("./books/frankenstein.txt")
    text = get_book_text(sys.argv[1])
    words_list = text.split()
    return len(words_list)

def count_characters():
    # text_str = get_book_text("./books/frankenstein.txt").lower()
    text_str = get_book_text(sys.argv[1]).lower()
    final_dict = {}

    for character in text_str:
        if character not in final_dict:
            final_dict[character] = text_str.count(character)
    return final_dict

def sort_dictionaries():
    dict = count_characters()
    sorted_dict_list = []

    for d in dict:
        new_dict = {}
        new_dict["char"] = d
        new_dict["num"] = dict[d]
        sorted_dict_list.append(new_dict)
    
    def sort_on(dict):
        return dict["num"]

    
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list

