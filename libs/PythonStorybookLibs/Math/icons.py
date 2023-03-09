
import numpy as np;

from ..helpers.numbers import getDigits

icons = {
    0: '🎲',
    1: '🚗',
    2: '✍',
    3: '🍻',
    4: '🛫',
    5: '🏫',
    6: '😈',
    7: '⛪',
    8: '🎱',
    9: '💍',
}

def getIcon(digit: int) -> str:
    return icons[digit]

def getIcons(digits: int) -> list:
    return [getIcon(digit) for digit in digits]

def mapNumberToIcons(number: int, separator: str = '') -> str:
    digits = getDigits(number)
    icons = separator.join(getIcons(digits))
    
    return icons

def mapMatrixToIcons(M):
    size = M.shape
    rowSize = size[0]
    columnSize = size[1]
    R = np.ndarray(size, dtype = object)

    for row in range(0, rowSize):
        for column in range(0, columnSize):                
            if M[row, column] == None:
                R[row, column] = ''
                continue
            
            R[row, column] = mapNumberToIcons(M[row, column])

    return R

def mapDictionaryWithNumberTermsToIcons(d, separator = ''):
    keysWithIcons = [(number, mapNumberToIcons(number)) for number in d.keys()]
    R = { icon: [] for key, icon in keysWithIcons }
    
    for key, icon in keysWithIcons:
        numberTerms = d[key]
        
        for terms in numberTerms:
            termsStr = separator.join([mapNumberToIcons(terms[0]), mapNumberToIcons(terms[1])])
            R[icon].append(termsStr)
    
    return R