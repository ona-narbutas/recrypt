from unittest.mock import MagicMock, patch

import pytest


from src.classes.word import Word

class TestWord:
    example = Word(" eXAMple   ")

    def test_init(self):
        assert self.example.word == "example"
        assert type(self.example.chars) == list
        assert len(self.example.chars) == 7
        assert len(self.example.char_set) == 6
        assert self.example.char_count["e"] == 2

        with patch.object(Word, "lookup", return_value=[]) as mock_lookup:
            with pytest.raises(ValueError):
                fake_word = Word("fiwefwefhu")
        mock_lookup.assert_called_once()
