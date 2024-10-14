from words_extraction import getWordsFrequencies
from chunk_by_syllables import getSyllablesFrequencies

from faker import Faker

fake = Faker()

text = fake.text(max_nb_chars=1000)

words = getWordsFrequencies(text)
syllablesFrequencies = getSyllablesFrequencies(list(words.keys()))

print('result', syllablesFrequencies)
