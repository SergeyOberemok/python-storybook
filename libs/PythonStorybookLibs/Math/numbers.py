def getTerms(number, maxBase = 10):
    terms = []
    
    for index, term in enumerate(range(number, 0, -1)):
        if index == 0:
            continue
        
        if number == index + term and index <= term and term < maxBase:
            terms.append((index, term))
    
    return terms