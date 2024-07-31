from unittest.mock import MagicMock

from src.classes.word import Word

class TestWord:
    example = Word(" eXAMple   ")

    def test_init(self):
        assert self.example.word == "example"
        assert type(self.example.chars) == list
        assert len(self.example.chars) == 7
        assert len(self.example.char_set) == 6
        assert self.example.char_count["e"] == 2