from src.classes.word import Word

class KeyWord(Word):
    def __init__(self, word: str, hint: str = ""):
        super().__init__(word=word)
        self.hint: str = hint
        self.unlocked: bool = False

    def __repr__(self) -> str:
        return f"KeyWord({self.word!r})"
    
    def guess(self, attempt: str) -> bool:
        guess_word = Word(attempt)
        if guess_word.word == self.word:
            self.unlocked = True
        return self.unlocked
    
    def _is_anagram(self, candidate: Word) -> bool:
        return self.char_count == candidate.char_count

    def _contains_or_contained(self, candidate: Word) -> bool:
        return self.word in candidate.word or candidate.word in self.word

    def validate_next(self, candidate: str) -> bool:
        """Options for next word:
        1. Words are anagrams
        2. New word exists in old word, or vice versa (example -> ample)
        3. New Word must exist

        Regardless, new word must be valid English word
        """
        if not candidate.lookup():
            return False
        return (self._is_anagram(candidate) or self._contains_or_contained(candidate))
