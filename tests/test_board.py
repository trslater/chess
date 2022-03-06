import pytest

from chess import board


class TestRankAndFileFromIndices:
    def test_raises_value_error(self):
        with pytest.raises(ValueError):
            board.rank_and_file_from_indices(-1, 0)
        
        with pytest.raises(ValueError):
            board.rank_and_file_from_indices(0, 8)

    def test_rank(self):
        actual = board.rank_and_file_from_indices(3, 6)
        expected = 5, "G"

        assert actual == expected
