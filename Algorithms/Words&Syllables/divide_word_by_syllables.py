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
import re
from typing import Generator, Iterator
from operator import itemgetter

fake = Faker()

# ---

# + active=""
# word = fake.word()
# -

word = 'research'

# + active=""
# syllables = [*wrap(word, 2), *wrap(word, 3)]
# -

syllables = ['in','on','ou','ne','th','ar','ce','es','ng','re','ti','ing','ion','an','ed','en','er','im','io','me','ro','ss','ta']


# + editable=true raw_mimetype="" slideshow={"slide_type": ""} active=""
# print(word, syllables)
# -

# ---

# # Divide word by syllables

# ## Syllables

# ### Sort syllables

def sortByLength(syllables: list[str]) -> list[str]:
    return sorted(sorted(syllables), key=len, reverse=True)


# + active=""
# print(sortByLength(syllables))
# -

# ### Syllables in word

def filterSyllablesByWord(word: str, syllables: list[str]) -> Generator[str, None, None]:
    filteredSyllables = (syllable for syllable in syllables if re.search(syllable, word, re.IGNORECASE))
    
    for syllable in filteredSyllables:
        word = re.sub(syllable, ' ' * len(syllable), word, flags=re.IGNORECASE)
        yield syllable
    else:
        yield from re.findall(r'\w+', word, re.IGNORECASE)


# + active=""
# print([*filterSyllablesByWord(word, sortByLength(syllables))])
# -

# ## Indexes

# ### Start positions of syllables

def findIndexes(word: str, syllable: str) -> list[int]:
    indexes = list()
    syllableRegex = re.compile(syllable, re.IGNORECASE)
        
    while (match := syllableRegex.search(word)) is not None:
        index, _ = match.span()
        indexes.append(index)
        word = syllableRegex.sub(' ' * len(match.group()), word, 1)

    return indexes


# + active=""
# print(findIndexes(word, word[1]))
# -

# ### Index Syllable pair

def findIndexesOfSyllablePair(word: str, syllable: str) -> list[tuple[int, str]]:
    indexes = findIndexes(word, syllable)
    return [(index, syllable) for index in indexes]


# + active=""
# print(findIndexesOfSyllablePair(word, word[1]))
# -

def findIndexesSyllablesPairs(word: str, syllables: Iterator[str]) -> Generator[tuple[int, str], None, None]:
    for syllable in filterSyllablesByWord(word, syllables):
        yield from findIndexesOfSyllablePair(word, syllable)


# + active=""
# print([*findIndexesSyllablesPairs(word, sortByLength(syllables))])
# -

# ## Sort and filter

def sortAndFilterIndexesSyllablesPairs(indexesSyllablesPairs: Iterator[tuple[int, str]]) -> list[tuple[int, str]]:
    sortedIndexesSyllablesByLength = sorted(indexesSyllablesPairs, key=itemgetter(1), reverse=True)
    sortedIndexesSyllablesByIndex = sorted(sortedIndexesSyllablesByLength, key=itemgetter(0))
    stack = list()

    for (index, syllable) in sortedIndexesSyllablesByIndex:
        try:
            (latestIndex, latestSyllable) = stack[-1]
    
            if latestIndex + len(latestSyllable) <= index:
                stack.append((index, syllable))
        except IndexError:
            stack.append((index, syllable))

    return stack


# + active=""
# print(sortAndFilterIndexesSyllablesPairs(findIndexesSyllablesPairs(word, sortByLength(syllables))))
# -

# ## Divide

def divideBy(word: str, syllables: Iterator[str]) -> list[str]:
    filteredSyllables = filterSyllablesByWord(word, syllables)
    indexesSyllablesPairs = findIndexesSyllablesPairs(word, filteredSyllables)
    sortedAndFilteredIndexesSyllablesPairs = sortAndFilterIndexesSyllablesPairs(indexesSyllablesPairs)

    return [syllable for (_, syllable) in sortedAndFilteredIndexesSyllablesPairs]


filteredSyllables = filter(lambda syllable: len(syllable) >= 2, sortByLength(syllables))
dividedBySyllables = divideBy(word, filteredSyllables)

# + active=""
# print(dividedBySyllables)

# + active=""
# print(word, syllables, '-'.join(dividedBySyllables))
