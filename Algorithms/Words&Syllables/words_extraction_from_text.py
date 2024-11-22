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
import re
from collections import defaultdict
from typing import Iterator
from remove_non_word_signs import removeNonWordSigns

# ---

fake = Faker()
text = fake.text(max_nb_chars=1000)


# + active=""
# print(text)
# -

# ### Text to Words

def toWords(text: str) -> list[str]:
    return sorted(re.findall(r'\w+', text.lower()))


# + active=""
# print(toWords(text))
# -

# ## Frequencies

# ### Simple

def toFrequencyDictionary(words: list[str]) -> dict[str, int]:
    wordsFrequencies = defaultdict(int)

    for word in words:
        wordsFrequencies[word] += 1
    
    return wordsFrequencies


# + active=""
# print(toFrequencyDictionary(words))
# -

# ### Accumulate

def reduceWordsFrequencies(acc: defaultdict[str, int], wordsFrequencies: dict[str, int]) -> dict[str, int]:
    for word in wordsFrequencies:
        acc[word] += wordsFrequencies[word]
    
    return acc


# + active=""
# print(reduceWordsFrequencies(defaultdict(int, { 'hello': 2 }), { 'hello': 2, 'world': 4 }))
# -

# ### Sorting

def sortWordsFrequenciesByFrequency(wordsFrequencies: dict[str, int]) -> dict[str, int]:
    sortedAlphabetically = dict(sorted(wordsFrequencies.items()))
    sortedByFrequency = sorted(sortedAlphabetically, key=wordsFrequencies.get, reverse=True)
    wordsFrequenciesDict = dict([(word, wordsFrequencies[word]) for word in sortedByFrequency])

    return wordsFrequenciesDict


# + active=""
# print(sortWordsFrequenciesByFrequency(toFrequencyDictionary(words)))
# -

# ## Text to words and frequencies

# ### Text

def getWordsFrequencies(text: str) -> dict[str, int]:
    clearedText = removeNonWordSigns(text)
    words = toWords(clearedText)
    wordsFrequencies = toFrequencyDictionary(words)

    return wordsFrequencies


# + active=""
# print(getWordsFrequencies(text))
# -

def getWordsFrequenciesFromText(text: str) -> dict[str, int]:
    wordsFrequencies = getWordsFrequencies(text)
    sortedWordsFrequencies = sortWordsFrequenciesByFrequency(wordsFrequencies)

    return sortedWordsFrequencies


# + active=""
# print(getWordsFrequenciesFromText(text))
# -

# ### Lines

def getAndReduceWordsFrequencies(lines: Iterator[str]) -> dict[str, int]:
    allWordsFrequencies = defaultdict(int)
    
    for line in lines:
        wordsFrequencies = getWordsFrequencies(line)
        allWordsFrequencies = reduceWordsFrequencies(allWordsFrequencies, wordsFrequencies)

    return allWordsFrequencies


# + active=""
# print(getAndReduceWordsFrequencies(text.split('.')))
# -

def getWordsFrequenciesFromLines(lines: Iterator[str]) -> dict[str, int]:
    allWordsFrequencies = getAndReduceWordsFrequencies(lines)
    sortedAllWordsFrequencies = sortWordsFrequenciesByFrequency(allWordsFrequencies)
    
    return sortedAllWordsFrequencies

# + active=""
# print(getWordsFrequenciesFromLines(text.split('.')))
