from collections import Counter

def get_num_words(book):
    with open(book) as file:
        bcontents = file.read()
        num_words = len(bcontents.split())
        print(f"Found {num_words} total words")

def wordCount(textFromBook):
    with open(textFromBook) as file:
            line = file.read()
            #print("Line: ", line.lower())
            lowerCase_lines = line.lower()
    
    return Counter(lowerCase_lines)            
            #count_line 
        #num_of_words = (lines.lower())
        #print(num_of_words)

def splitDicts(mainDict):
     #getAllDicts = [sorted(mainDict.items(), key=lambda item: item[1], reverse=True)]
    sortByCount = sorted(mainDict.items(), key=lambda item: item[1], reverse=True)
    return sortByCount
    #return [{key: value} for key, value in mainDict.items()]