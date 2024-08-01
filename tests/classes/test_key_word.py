from src.classes.key_word import KeyWord
from src.classes.word import Word

class TestKeyWord:
    example = KeyWord("example", "This is a hint!")

    def test_init(self):
        assert isinstance(self.example, Word)
        assert self.example.hint == "This is a hint!"

    def test_guess(self):
        assert self.example.guess("Wrong guess") == False
        assert self.example.unlocked == False
        assert self.example.guess("EXAMPLE") == True
        assert self.example.unlocked == True

    def test_validate_next(self):
        assert self.example.validate_next(Word("random")) == False
        assert self.example.validate_next(Word("ample")) == True
        
        tape = KeyWord("tape", "Swap 2 letters")
        assert tape.validate_next(Word("pate")) == True