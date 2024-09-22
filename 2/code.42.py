from numpy import zeros, max
from typing import Tuple


BLOSUM62 = {
    "A": {"A": +4, "C": +0, "D": -2, "E": -1, "F": -2, "G": +0, "H": -2, "I": -1, "K": -1, "L": -1,
          "M": -1, "N": -2, "P": -1, "Q": -1, "R": -1, "S": +1, "T": +0, "V": +0, "W": -3, "Y": -2},
    "C": {"A": +0, "C": +9, "D": -3, "E": -4, "F": -2, "G": -3, "H": -3, "I": -1, "K": -3, "L": -1,
          "M": -1, "N": -3, "P": -3, "Q": -3, "R": -3, "S": -1, "T": -1, "V": -1, "W": -2, "Y": -2},
    "D": {"A": -2, "C": -3, "D": +6, "E": +2, "F": -3, "G": -1, "H": -1, "I": -3, "K": -1, "L": -4,
          "M": -3, "N": +1, "P": -1, "Q": +0, "R": -2, "S": +0, "T": -1, "V": -3, "W": -4, "Y": -3},
    "E": {"A": -1, "C": -4, "D": +2, "E": +5, "F": -3, "G": -2, "H": +0, "I": -3, "K": +1, "L": -3,
          "M": -2, "N": +0, "P": -1, "Q": +2, "R": +0, "S": +0, "T": -1, "V": -2, "W": -3, "Y": -2},
    "F": {"A": -2, "C": -2, "D": -3, "E": -3, "F": +6, "G": -3, "H": -1, "I": +0, "K": -3, "L": +0,
          "M": +0, "N": -3, "P": -4, "Q": -3, "R": -3, "S": -2, "T": -2, "V": -1, "W": +1, "Y": +3},
    "G": {"A": +0, "C": -3, "D": -1, "E": -2, "F": -3, "G": +6, "H": -2, "I": -4, "K": -2, "L": -4,
          "M": -3, "N": +0, "P": -2, "Q": -2, "R": -2, "S": +0, "T": -2, "V": -3, "W": -2, "Y": -3},
    "H": {"A": -2, "C": -3, "D": -1, "E": +0, "F": -1, "G": -2, "H": +8, "I": -3, "K": -1, "L": -3,
          "M": -2, "N": +1, "P": -2, "Q": +0, "R": +0, "S": -1, "T": -2, "V": -3, "W": -2, "Y": +2},
    "I": {"A": -1, "C": -1, "D": -3, "E": -3, "F": +0, "G": -4, "H": -3, "I": +4, "K": -3, "L": +2,
          "M": +1, "N": -3, "P": -3, "Q": -3, "R": -3, "S": -2, "T": -1, "V": +3, "W": -3, "Y": -1},
    "K": {"A": -1, "C": -3, "D": -1, "E": +1, "F": -3, "G": -2, "H": -1, "I": -3, "K": +5, "L": -2,
          "M": -1, "N": +0, "P": -1, "Q": +1, "R": +2, "S": +0, "T": -1, "V": -2, "W": -3, "Y": -2},
    "L": {"A": -1, "C": -1, "D": -4, "E": -3, "F": +0, "G": -4, "H": -3, "I": +2, "K": -2, "L": +4,
          "M": +2, "N": -3, "P": -3, "Q": -2, "R": -2, "S": -2, "T": -1, "V": +1, "W": -2, "Y": -1},
    "M": {"A": -1, "C": -1, "D": -3, "E": -2, "F": +0, "G": -3, "H": -2, "I": +1, "K": -1, "L": +2,
          "M": +5, "N": -2, "P": -2, "Q": +0, "R": -1, "S": -1, "T": -1, "V": +1, "W": -1, "Y": -1},
    "N": {"A": -2, "C": -3, "D": +1, "E": +0, "F": -3, "G": +0, "H": +1, "I": -3, "K": +0, "L": -3,
          "M": -2, "N": +6, "P": -2, "Q": +0, "R": +0, "S": +1, "T": +0, "V": -3, "W": -4, "Y": -2},
    "P": {"A": -1, "C": -3, "D": -1, "E": -1, "F": -4, "G": -2, "H": -2, "I": -3, "K": -1, "L": -3,
          "M": -2, "N": -2, "P": +7, "Q": -1, "R": -2, "S": -1, "T": -1, "V": -2, "W": -4, "Y": -3},
    "Q": {"A": -1, "C": -3, "D": +0, "E": +2, "F": -3, "G": -2, "H": +0, "I": -3, "K": +1, "L": -2,
          "M": +0, "N": +0, "P": -1, "Q": +5, "R": +1, "S": +0, "T": -1, "V": -2, "W": -2, "Y": -1},
    "R": {"A": -1, "C": -3, "D": -2, "E": +0, "F": -3, "G": -2, "H": +0, "I": -3, "K": +2, "L": -2,
          "M": -1, "N": +0, "P": -2, "Q": +1, "R": +5, "S": -1, "T": -1, "V": -3, "W": -3, "Y": -2},
    "S": {"A": +1, "C": -1, "D": +0, "E": +0, "F": -2, "G": +0, "H": -1, "I": -2, "K": +0, "L": -2,
          "M": -1, "N": +1, "P": -1, "Q": +0, "R": -1, "S": +4, "T": +1, "V": -2, "W": -3, "Y": -2},
    "T": {"A": +0, "C": -1, "D": -1, "E": -1, "F": -2, "G": -2, "H": -2, "I": -1, "K": -1, "L": -1,
          "M": -1, "N": +0, "P": -1, "Q": -1, "R": -1, "S": +1, "T": +5, "V": +0, "W": -2, "Y": -2},
    "V": {"A": +0, "C": -1, "D": -3, "E": -2, "F": -1, "G": -3, "H": -3, "I": +3, "K": -2, "L": +1,
          "M": +1, "N": -3, "P": -2, "Q": -2, "R": -3, "S": -2, "T": +0, "V": +4, "W": -3, "Y": -1},
    "W": {"A": -3, "C": -2, "D": -4, "E": -3, "F": +1, "G": -2, "H": -2, "I": -3, "K": -3, "L": -2,
          "M": -1, "N": -4, "P": -4, "Q": -2, "R": -3, "S": -3, "T": -2, "V": -3, "W": 11, "Y": 2},
    "Y": {"A": -2, "C": -2, "D": -3, "E": -2, "F": +3, "G": -3, "H": +2, "I": -1, "K": -2, "L": -1,
          "M": -1, "N": -2, "P": -3, "Q": -1, "R": -2, "S": -2, "T": -2, "V": -1, "W": +2, "Y": +7}
}


def function(sequence_1: str,
             sequence_2: str,
             gap_open: int,
             gap_extend: int) \
        -> Tuple[int, str, str]:
    # Create a dynamic programming table.
    table = zeros(shape=(3, len(sequence_1) + 1, len(sequence_2) + 1), dtype=int)

    # Fill initial values with affine gap penalties.
    # 0: The highest comparison score that can be achieved after the last match or mismatch.
    # 1: The highest score when the last column contains one or more gaps.
    # 2: The highest score when the last line contains one or more gaps.
    for index in range(1, len(sequence_1) + 1):
        table[0, index, 0] = -gap_open - (index - 1) * gap_extend
        table[1, index, 0] = -gap_open - (index - 1) * gap_extend

    for index in range(1, len(sequence_2) + 1):
        table[0, 0, index] = -gap_open - (index - 1) * gap_extend
        table[2, 0, index] = -gap_open - (index - 1) * gap_extend

    # Fill in the tables.
    for index_1 in range(1, len(sequence_1) + 1):
        for index_2 in range(1, len(sequence_2) + 1):
            blosum62_score = BLOSUM62[sequence_1[index_1 - 1]][sequence_2[index_2 - 1]]
            table[1, index_1, index_2] = max([table[0, index_1 - 1, index_2] - gap_open,
                                              table[1, index_1 - 1, index_2] - gap_extend])
            table[2, index_1, index_2] = max([table[0, index_1, index_2 - 1] - gap_open,
                                              table[2, index_1, index_2 - 1] - gap_extend])
            table[0, index_1, index_2] = max([table[0, index_1 - 1, index_2 - 1] + blosum62_score,
                                              table[1, index_1, index_2],
                                              table[2, index_1, index_2]])

    # Use the maximum score
    maximum_score = table[0, len(sequence_1), len(sequence_2)]

    # Backtrack to find the alignment.
    alignment_1, alignment_2, index_1, index_2 = "", "", len(sequence_1), len(sequence_2)
    while index_1 > 0 or index_2 > 0:
        current_score = table[0, index_1, index_2]
        match = table[0, index_1 - 1, index_2 - 1] + BLOSUM62[sequence_1[index_1 - 1]][sequence_2[index_2 - 1]]
        if index_1 > 0 and index_2 > 0 and current_score == match:
            alignment_1 += sequence_1[index_1 - 1]
            alignment_2 += sequence_2[index_2 - 1]
            index_1 -= 1
            index_2 -= 1
        elif index_1 > 0 and current_score == table[1, index_1, index_2]:
            alignment_1 += sequence_1[index_1 - 1]
            alignment_2 += "-"
            index_1 -= 1
        else:
            alignment_1 += "-"
            alignment_2 += sequence_2[index_2 - 1]
            index_2 -= 1

    # Reverse the alignment.
    alignment_1, alignment_2 = alignment_1[::-1], alignment_2[::-1]

    return int(maximum_score), alignment_1, alignment_2


if __name__ == "__main__":
    p_1 = "EKSDLTEDTPEDTPYKAGENYVPDCRITTYNNPQMYSEPCKFFVPPNKILNNTYRDRTMLQHVHHTHPTSYG"
    p_2 = "EKSDLTEDTPEEVNCWTPYKAGQIYVPDCRITTWFPPQMMSEPCKCYMYSWHFVPPILNNTYRDRHVHFTHPTSQG"
    p_3 = 11
    p_4 = 1

    r_1, r_2, r_3 = function(p_1, p_2, p_3, p_4)

    print(r_1)
    print(r_2)
    print(r_3)
