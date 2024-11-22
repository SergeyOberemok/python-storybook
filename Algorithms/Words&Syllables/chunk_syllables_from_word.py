# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from faker import Faker
from textwrap import wrap
from itertools import chain
from functools import reduce
from collections import defaultdict

# ---

fake = Faker()

word = fake.word()


# + active=""
# print(word)
# -

# ---

# # Divide word into syllables for search

# ## Spin

# ### Spin word

# #### One spin

def spinWord(word: str) -> str:
    firstLetter = word[0]
    rest = word[1:]
    return ''.join([rest, firstLetter])


# + active=""
# print(word, spinWord(word), spinWord(spinWord(spinWord(spinWord(spinWord(spinWord(word)))))))
# -

# #### Spin around

def spinWordAround(word: str) -> list[str]:
    originalWord = word
    spunList = [originalWord]
    spun = spinWord(word)

    while originalWord != spun:
        spunList.append(spun)
        spun = spinWord(spun)

    return spunList


# + active=""
# print(spinWordAround(word))
# -

# ## Chunk

# ### syllables

# +
def getSyllables(word: str, length: int) -> list[str]:
    syllables = wrap(word, length)
    return list(filter(lambda syllable: len(syllable) == length, syllables))


def getDiphthongs(word: str) -> list[str]:
    return getSyllables(word, 2)


def getTriphthongs(word: str) -> list[str]:
    return getSyllables(word, 3)


# + active=""
# print(getSyllables(word, 2), getDiphthongs(word), getTriphthongs(word))
# -

# ## Flatten

# ### Chunk of syllables

def flattenSyllables(syllables: list[list[str]]) -> list[str]:
    return list(chain.from_iterable(syllables))


# + active=""
# print(flattenSyllables([getDiphthongs(word), getTriphthongs(word)]))
# -

def divideIntoSyllables(word: str) -> list[str]:
    spins = spinWordAround(word)
    diphthongs = [getDiphthongs(spun) for spun in spins]
    triphthongs = [getTriphthongs(spun) for spun in spins]
    syllables = flattenSyllables([*sorted(triphthongs), *sorted(diphthongs)])
    existed = list(filter(lambda syllable: syllable in word, syllables))
    unique = reduce(lambda acc, i: acc + [i] if i not in acc else acc, existed, [])
    return unique


# + active=""
# print(divideIntoSyllables(word))
# -

# ## Frequencies

# ### Count syllables

def countSyllables(words: list[str]) -> dict[str, int]:
    syllablesFrequencies = defaultdict(int)
    
    for word in words:
        for syllable in divideIntoSyllables(word):
                syllablesFrequencies[syllable] += 1

    return syllablesFrequencies


# + active=""
# print(countSyllables(fake.words()))
# -

def percentageToNumber(total: int, percent: int) -> int:
    return round(total * percent / 100)


# + active=""
# print(percentageToNumber(4, 25))
# -

# ### Merge and sort

def getSyllablesFrequencies(words: list[str], minFrequencyPercentage: int = 0) -> dict[str, int]:
    syllablesFrequencies = countSyllables(words)
    sortedAlphabetically = sorted(syllablesFrequencies)
    sortedByLength = sorted(sortedAlphabetically, key=len, reverse=True)
    sortedByFrequency = sorted(sortedByLength, key=syllablesFrequencies.get, reverse=True)
    minFrequency = percentageToNumber(max(syllablesFrequencies.values()), minFrequencyPercentage)
    syllablesFrequenciesDict = dict([(syllable, syllablesFrequencies[syllable]) for syllable in sortedByFrequency if syllablesFrequencies[syllable] >= minFrequency])
    
    return syllablesFrequenciesDict

# + active=""
# print(getSyllablesFrequencies(fake.words()))
