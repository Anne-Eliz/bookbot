def getWordCount(bookText):
    splitText = bookText.split()
    return len(splitText)

def getCharacterCounts(bookText):
    charCountDict = {}
    for eachChar in bookText:
        eachChar = eachChar.lower()
        if eachChar in charCountDict:
            charCountDict[eachChar] += 1
        else:
            charCountDict[eachChar] = 1
    return charCountDict


def sortingKey(item):
    return item['count']

def makeCharacterDict(charCountDict):
    charCountList = []
    for eachChar in charCountDict:
        if eachChar.isalpha():
            currentCharDict = {"name": eachChar, "count": charCountDict[eachChar]}
            charCountList.append(currentCharDict)
    charCountList.sort(key=sortingKey, reverse=True)
    return charCountList





















