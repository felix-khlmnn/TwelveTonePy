def scoring(numArray):
    

    consonanceRuleSet = [2, 3, 4, 5, 6, 9, -2, -4, -5, -9]
    
    score = 0
    
    for x in range(len(numArray)):
        d = int(numArray[x]) - int(numArray[x - 1])
        consonance = False
        for c in consonanceRuleSet:
            if (c == d):
                consonance = True
                break
    
        score += int(consonance)
        
    return score

