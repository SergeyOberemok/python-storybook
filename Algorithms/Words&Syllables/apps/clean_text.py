from helpers.file_utilities import readText, writeText
from remove_non_word_signs import removeNonWordSigns


def main():
    text = readText('../data/text')

    text = removeNonWordSigns(text)

    writeText('../data/unicode', text)


if __name__ == '__main__':
    main()
