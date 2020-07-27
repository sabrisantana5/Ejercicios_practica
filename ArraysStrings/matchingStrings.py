#Returns the amount of times that the querie appears
#in strings
def matchingStrings(strings, queries):
    returnArray = [0]*len(queries)
    for x in range(len(queries)):
        returnArray[x] = strings.count(queries[x])
    return returnArray
strings = ["aba","d","aba","abaas","s"]
queries = ["aba","b"]
print(matchingStrings(strings,queries))