import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)
    

from stats import num_of_words, count_characters, sort_dictionaries

def main():

    print("\n============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_of_words()} total words\n")
    print("--------- Character Count -------\n")

    for i in sort_dictionaries():
        char = i["char"]
        if char.isalpha():
            print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")
        

main()