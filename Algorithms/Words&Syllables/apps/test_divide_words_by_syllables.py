from divide_words_by_syllables import divideWordsBySyllables


def test_words_equality():
    dividedWords: list[tuple[str, str]] = divideWordsBySyllables()

    for (word, divided) in dividedWords:
        assert word == divided.replace('-', ''), f'{word} != {divided}'
