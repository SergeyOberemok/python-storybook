from helpers.icons import mapDigitsToIcons, mapNumberToIcons


class TestIcons:
    def setup_class(self):
        self.length = 10

    def test_mapDigitsToIcons(self, faker):
        names = dict([(i, faker.name()) for i in range(self.length)])
        digits = [i for i in range(self.length)]

        result = mapDigitsToIcons(digits, names)

        for i in names:
            assert names[i] in result

    def test_mapNumberToIcons(self, faker):
        names = dict([(i, faker.name()) for i in range(self.length)])
        randomInt = faker.pyint(1, self.length)

        result = mapNumberToIcons(randomInt, names)

        assert names[randomInt] in result
