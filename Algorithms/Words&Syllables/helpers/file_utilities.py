import json
import csv
from typing import Generator


def readText(fileName: str) -> str:
    with open(f'{fileName}.txt', encoding='utf-8') as file:
        return file.read()


def readLines(fileName: str) -> Generator[str, None, None]:
    with open(f'{fileName}.txt', encoding='utf-8') as file:
        yield from file


def readCSVLines(fileName: str) -> Generator[str, None, None]:
    with open(f'{fileName}.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        yield from reader


def readCSVLinesAsPairs(fileName: str) -> Generator[tuple[str, str], None, None]:
    with open(f'{fileName}.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield tuple(row.values())


def writeText(fileName: str, text: str):
    with open(f'{fileName}.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def writeJSON(fileName: str, data):
    with open(f'{fileName}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def writeCSV(fileName: str, data):
    with open(f'{fileName}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
