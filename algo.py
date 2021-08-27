from gen import *
rDict = {
    
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

print(list(rDict.keys())[list(rDict.values()).index(scoreComparison[0])])
