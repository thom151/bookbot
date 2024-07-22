
def main():
    book_path = "book/frankenstein.txt"
    file_contents = getContents(book_path)
    char_dict = getCharLength(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(getLength(file_contents),  "words found in the document")
    print()
    for item in sortDict(char_dict):
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']}")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def sortDict(char_dict):
    sorted = []
    for char  in char_dict:
        sorted.append({"char": char, "num":char_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted



def getContents(book):
    with open(book) as f:
        return f.read();


def getLength(contents):
    return len(contents.split());


def getCharLength(contents):
    char_dict = {}
    lowered_contents = contents.lower()
    for c in lowered_contents:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict


main()
