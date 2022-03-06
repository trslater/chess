from chess.pieces import Pawn, Knight, Bishop, Rook, Queen, King


class TestPiece:
    def test_sum(self):
        groups = ((Pawn(), Knight(), Bishop()),
                  (Knight(), Bishop(), Queen()),
                  (Pawn(), Pawn(), Pawn(), Pawn()))

        actual_sums = tuple(map(sum, groups))
        expected_sums = (7, 15, 4)
        
        for actual_sum, expected_sum in zip(actual_sums, expected_sums):
            assert actual_sum == expected_sum
    
    def test_compare(self):
        assert Knight() == Knight()
        assert Bishop() == Knight()
        assert King() <= King()
        assert Bishop() <= Rook()
        assert King() > Queen()
        assert Pawn() < Knight()
        assert Queen() != Rook()
