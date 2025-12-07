
import sys
from stats import getWordCount, getCharacterCounts, makeCharacterDict


def getBookText(filePath):
    with open(filePath, 'r', encoding="utf-8") as f:
        bookText = f.read()
    return bookText


def main():


    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookPath = sys.argv[1]
        bookText = getBookText(bookPath)

    # print(text)

    ## print(getCharacterCounts(text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at", bookPath, "...")
    print("----------- Word Count ----------")
    print("Found", getWordCount(bookText), "total words")
    print("--------- Character Count -------")

    countDict = getCharacterCounts(bookText)
    countList = makeCharacterDict(countDict)
    for eachItem in countList:
        print(f"{eachItem["name"]}: {eachItem["count"]}")

main()