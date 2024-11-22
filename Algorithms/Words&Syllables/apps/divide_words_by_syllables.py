from divide_word_by_syllables import divideBy
from helpers.file_utilities import readCSVLinesAsPairs, writeCSV


def divideWordsBySyllables() -> list[tuple[str, str]]:
    wordFrequencies = readCSVLinesAsPairs('../data/words')
    syllablesFrequencies = readCSVLinesAsPairs('../data/syllables')

    dividedWords = list()
    syllables = [syllable for (syllable, _) in syllablesFrequencies]

    for (word, _) in wordFrequencies:
        dividedWords.append((word, '-'.join(divideBy(word, syllables))))

    return dividedWords


def main():
    dividedWords = divideWordsBySyllables()

    data = [('word', 'divided')] + dividedWords
    writeCSV('../data/divided_words', data)


if __name__ == '__main__':
    main()
