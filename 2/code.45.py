from numpy import zeros, max
from typing import Tuple


def function(sequence_1: str,
             sequence_2: str,
             sequence_3: str) \
        -> Tuple[int, str, str, str]:
    # Create a dynamic programming table with 3 dimensions.
    table = zeros(shape=(len(sequence_1) + 1, len(sequence_2) + 1, len(sequence_3) + 1), dtype=int)

    # Fill the table.
    for idx1 in range(1, len(sequence_1) + 1):
        for idx2 in range(1, len(sequence_2) + 1):
            for idx3 in range(1, len(sequence_3) + 1):
                # Calculate the maximum score for dp[i, j, k]
                match = int(sequence_1[idx1 - 1] == sequence_2[idx2 - 1] == sequence_3[idx3 - 1])
                table[idx1, idx2, idx3] = max([
                    table[idx1 - 1, idx2, idx3],  # Deletion from sequence 1.
                    table[idx1, idx2 - 1, idx3],  # Deletion from sequence 2.
                    table[idx1, idx2, idx3 - 1],  # Deletion from sequence 3.
                    table[idx1 - 1, idx2 - 1, idx3],  # Deletion from both sequence 1 and sequence 2.
                    table[idx1 - 1, idx2, idx3 - 1],  # Deletion from both sequence 1 and sequence 3.
                    table[idx1, idx2 - 1, idx3 - 1],  # Deletion from both sequence 2 and sequence 3.
                    table[idx1 - 1, idx2 - 1, idx3 - 1] + match  # Match or mismatch.
                ])

    # Use the maximum score is at the last cell of the table.
    maximum_score = table[len(sequence_1), len(sequence_2), len(sequence_3)]
    
    # Backtrack to find the alignment.
    alignment_1, alignment_2, alignment_3 = "", "", ""
    idx1, idx2, idx3 = len(sequence_1), len(sequence_2), len(sequence_3)

    while idx1 > 0 or idx2 > 0 or idx3 > 0:
        if idx1 > 0 and idx2 > 0 and idx3 > 0 and sequence_1[idx1 - 1] == sequence_2[idx2 - 1] == sequence_3[idx3 - 1]:
            alignment_1 += sequence_1[idx1 - 1]
            alignment_2 += sequence_2[idx2 - 1]
            alignment_3 += sequence_3[idx3 - 1]
            idx1 -= 1
            idx2 -= 1
            idx3 -= 1
        elif idx1 > 0 and table[idx1, idx2, idx3] == table[idx1 - 1, idx2, idx3]:
            alignment_1 += sequence_1[idx1 - 1]
            alignment_2 += "-"
            alignment_3 += "-"
            idx1 -= 1
        elif idx2 > 0 and table[idx1, idx2, idx3] == table[idx1, idx2 - 1, idx3]:
            alignment_1 += "-"
            alignment_2 += sequence_2[idx2 - 1]
            alignment_3 += "-"
            idx2 -= 1
        elif idx3 > 0 and table[idx1, idx2, idx3] == table[idx1, idx2, idx3 - 1]:
            alignment_1 += "-"
            alignment_2 += "-"
            alignment_3 += sequence_3[idx3 - 1]
            idx3 -= 1
        elif idx1 > 0 and idx2 > 0 and table[idx1, idx2, idx3] == table[idx1 - 1, idx2 - 1, idx3]:
            alignment_1 += sequence_1[idx1 - 1]
            alignment_2 += sequence_2[idx2 - 1]
            alignment_3 += "-"
            idx1 -= 1
            idx2 -= 1
        elif idx1 > 0 and idx3 > 0 and table[idx1, idx2, idx3] == table[idx1 - 1, idx2, idx3 - 1]:
            alignment_1 += sequence_1[idx1 - 1]
            alignment_2 += "-"
            alignment_3 += sequence_3[idx3 - 1]
            idx1 -= 1
            idx3 -= 1
        elif idx2 > 0 and idx3 > 0 and table[idx1, idx2, idx3] == table[idx1, idx2 - 1, idx3 - 1]:
            alignment_1 += "-"
            alignment_2 += sequence_2[idx2 - 1]
            alignment_3 += sequence_3[idx3 - 1]
            idx2 -= 1
            idx3 -= 1

    # Reverse the alignment.
    alignment_1, alignment_2, alignment_3 = alignment_1[::-1], alignment_2[::-1], alignment_3[::-1]

    return maximum_score, alignment_1, alignment_2, alignment_3


if __name__ == "__main__":
    p_1 = "ACATTTCACCACCAGCACGCTTCGGAT"
    p_2 = "CCATGTCCACTTCTCATGGAGTCACACCA"
    p_3 = "CCAGCAATCGTGCTTGCCAAACAT"

    r_1, r_2, r_3, r_4 = function(p_1, p_2, p_3)

    print(r_1)
    print(r_2)
    print(r_3)
    print(r_4)
