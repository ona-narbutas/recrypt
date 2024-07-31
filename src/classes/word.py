from collections import Counter

class Word:

    def __init__(self, word: str):
        self.word = word.strip().lower()
        self.chars = list(self.word)
        self.char_set = set(self.chars)
        self.char_count = Counter(self.word)

    def __repr__(self) -> str:
        return f"Word({self.word!r})"
  