from gen import *
rDict = {
    
}

noteDict = {
    "c": 1,
    "c#": 2,
    "d": 3,
    "d#": 4,
    "e": 5,
    "f": 6,
    "f#": 7,
    "g": 8,
    "g#": 9,
    "a": 10,
    "a#": 11,
    "h": 12
}

def createReadAndRank():
    i = str.splitlines(gen())
    
    c = i[0]
    s = i[1]
    rDict[str(c)] = s


for r in range(500):
    createReadAndRank()
    
scoreComparison = list(rDict.values())
scoreComparison.sort()

#print(list(rDict.keys())[list(rDict.values()).index(scoreComparison[0])])
#Notes as numerical values
rawList = list(rDict.keys())[list(rDict.values()).index(scoreComparison[0])].split(" ")
formattedString = ""
for i in rawList:
    for note, value in noteDict.items():
        if str(value) == i:
            formattedString += (note + " ") 
print(formattedString)