from chunk_syllables_from_word import getSyllablesFrequencies
from utilities.files import readCSVLinesAsPairs, writeCSV


def main():
    wordsFrequencies = readCSVLinesAsPairs('../data/words')

    syllablesFrequencies = getSyllablesFrequencies([word for word, _ in wordsFrequencies], 50)

    data = [('syllable', 'frequency')] + list(syllablesFrequencies.items())
    writeCSV('../data/syllables', data)


if __name__ == '__main__':
    main()
