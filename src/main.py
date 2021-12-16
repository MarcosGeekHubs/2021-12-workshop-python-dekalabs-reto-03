import re
import os
from typing import Tuple, List


def get_frequent_words(
    filename: str = "src/book.txt", amount: int = 30
) -> List[Tuple[str, int]]:
    counter = {}

    content = ''
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            words = re.findall(r'\w+', line.lower())

            for word in words:
                if (not word) or (not len(word) >= 3): continue

                if word in counter: counter[word] += 1
                else: counter[word] = 1

    by_most_occurrences = sorted(counter.items(), key=lambda item: item[1], reverse=True)

    return by_most_occurrences[:amount]

# print(get_frequent_words('src/book.txt', 3))