def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        print("--- Begin report of books/frankenstein.txt ---")
        splitwords = thesplitter(file_contents)
        print(f"{len(splitwords)} words found in the document")
        print()#prints blank line
        chardict = dict_maker(file_contents)
        sorted_list = reportsort(chardict)
        for item in sorted_list:
            print(f"The '{item['char']}' character was found {item['num']} times")
        print("--- End report ---")

        
        
def thesplitter(text):
# This function splits the text into a list of words, this is used for word count
    splittext = text.split()
    return splittext


def dict_maker(text):
# This function populates the chardict dictionary and returns that dictionary
    chardict = {}  
    for char in text:
        if char.isalpha():
            if char in chardict:
                chardict[char] += 1
            else: 
                chardict[char] = 1
    return chardict

def sort_on(dict):
    return dict["num"]

def reportsort(dictionary):
# This function sorts dict chardict into a list of dict, then reverse sorts them    
    sortlist = []
    for char,count in dictionary.items():
        sortlist.append({"char": char, "num": count})
    sortlist.sort(reverse=True, key=sort_on)
    return sortlist

        


main()