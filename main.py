from stats import get_num_words
from stats import wordCount
from stats import splitDicts
import sys
def get_book_text(relative_path):
    with open(relative_path) as file:
        contents = file.read()
        print("File contents:")
        print(contents)

def main():
    #file_pathArg = sys.argv[1]
    
    if len(sys.argv) != 2:
        #len(sys.argv) > 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    #else:
        #print("No arguments provided.")
    newDict = {}
    myrelative_path = sys.argv[1]#"books/frankenstein.txt"
    getcounts = wordCount(myrelative_path)
    #get_book_text(myrelative_path)
    #return(wordCount)
    
    newDict = [{key: value} for key, value in sorted(getcounts.items(), key=lambda item: item[1], reverse=True)]   
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    #print(f"Found {totalWords} total words")
    get_num_words(myrelative_path)
    print("--------- Character Count -------")
    for dict in newDict:
        if any(char.isalpha() for char in dict):
            for char, count in dict.items():
                print(f"{char}: {count}")
        else:
            continue

main()
