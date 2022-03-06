def rank_and_file_from_indices(i: int, j: int) -> tuple[int, str]:
    if i < 0 or i > 7 or j < 0 or j > 7:
        raise ValueError()

    return (8 - i), chr(65 + j)

def indices_from_rank_and_file(rank: int, file: str) -> tuple[int, int]:
    # Do conversions up front, because it is easier to check indices
    i, j = (8 - rank), ord(file) - 65
    
    if i < 0 or i > 7 or j < 0 or j > 7:
        raise ValueError()

    return i, j
