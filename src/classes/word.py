from collections import Counter

import requests

from src.settings import (
    DICTIONARY_API_KEY,
    DICTIONARY_URL
)

class Word:

    def __init__(self, word: str):
        self.word = word.strip().lower()
        self.chars = list(self.word)
        self.char_set = set(self.chars)
        self.char_count = Counter(self.word)

        self.dictionary = self.lookup()
        if not self.dictionary:
            raise ValueError("Word not recognized.")

    def __repr__(self) -> str:
        return f"Word({self.word!r})"

    def lookup(self) -> dict:
        url = f"{DICTIONARY_URL}/{self.word}"
        r = requests.get(url=url, params={"key": DICTIONARY_API_KEY})
        return r.json()