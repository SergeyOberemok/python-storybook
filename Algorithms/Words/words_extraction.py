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

fake = Faker()

# ---

text = fake.text(max_nb_chars=1000)


# + active=""
# print(text)
# -

# ### Remove non word signs

def removeNonWordSigns(text: str) -> str:
    return re.sub(r'[^\w\s]', '', text).replace('\n', ' ')


clearedText = removeNonWordSigns(text)


# + active=""
# print(clearedText)
# -

# ### Text to Words

def toWords(text: str) -> list[str]:
    return sorted(re.findall(r'\w+', text.lower()))


words = toWords(clearedText)


# + active=""
# print(words)
# -

# ### Frequencies

def toFrequencyDictionary(words: list[str]) -> dict[str, int]:
    wordsFrequencies = defaultdict(int)

    for word in sorted(words):
        wordsFrequencies[word] += 1

    sortedByFrequency = sorted(wordsFrequencies, key=wordsFrequencies.get, reverse=True)
    wordsFrequenciesDict = dict([(word, wordsFrequencies[word]) for word in sortedByFrequency])
    
    return wordsFrequenciesDict


# + active=""
# print(toFrequencyDictionary(words))
# -

def getWordsFrequencies(text: str) -> dict[str, int]:
    clearedText = removeNonWordSigns(text)
    words = toWords(clearedText)
    wordsFrequencies = toFrequencyDictionary(words)

    return wordsFrequencies

# + active=""
# print(getWordsFrequencies(text))
