from utilities.files import readLines, writeCSV
from words_extraction_from_text import getWordsFrequenciesFromLines


def main():
    lines = readLines('../data/text')

    wordsFrequencies = getWordsFrequenciesFromLines(lines)

    data = [('word', 'frequency')] + list(wordsFrequencies.items())
    writeCSV('../data/words', data)


if __name__ == '__main__':
    main()
