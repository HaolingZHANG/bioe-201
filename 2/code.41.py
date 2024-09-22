from numpy import zeros, max, inf
from typing import Tuple


def function(sequence_1: str,
             sequence_2: str) \
        -> Tuple[int, str, str]:
    # Create a dynamic programming table.
    table = zeros(shape=(len(sequence_1) + 1, len(sequence_2) + 1))

    # Initialize the table.
    for index in range(1, len(sequence_1) + 1):
        table[index, 0] = 0
    for index in range(1, len(sequence_2) + 1):
        table[0, index] = 0

    # Fill in the table
    for index_1 in range(1, len(sequence_1) + 1):
        for index_2 in range(1, len(sequence_2) + 1):
            table[index_1, index_2] = max([
                table[index_1 - 1][index_2 - 1] + (1 if sequence_1[index_1 - 1] == sequence_2[index_2 - 1] else -2),
                table[index_1 - 1][index_2] - 2,
                table[index_1][index_2 - 1] - 2
            ])

    # Find the maximum score in the last row or last column
    maximum_score, maximum_location = -inf, (0, 0)
    for index in range(1, len(sequence_2) + 1):
        if table[len(sequence_1), index] > maximum_score:
            maximum_score, maximum_location = table[len(sequence_1), index], (len(sequence_1), index)
    for index in range(1, len(sequence_1) + 1):
        if table[index, len(sequence_2)] > maximum_score:
            maximum_score, maximum_location = table[index, len(sequence_2)], (index, len(sequence_2))

    # Backtrack to find the alignment.
    alignment_1, alignment_2 = "", ""
    index_1, index_2 = maximum_location

    while index_1 > 0 and index_2 > 0:
        flag = 1 if sequence_1[index_1 - 1] == sequence_2[index_2 - 1] else -2
        if index_1 > 0 and index_2 > 0 and table[index_1][index_2] == table[index_1 - 1, index_2 - 1] + flag:
            alignment_1 += sequence_1[index_1 - 1]
            alignment_2 += sequence_2[index_2 - 1]
            index_1 -= 1
            index_2 -= 1
        elif index_1 > 0 and table[index_1][index_2] == table[index_1 - 1, index_2] - 2:
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
    p_1 = "AAGCATGCCGGTGTAAACTGGTCACCGCAATGTTAGGATTCTTGGGTCACTTGGTGTTTAAAAGACGTGCGCGTGTACTATTCCTCTTCCGCATAGTTGCATTGGACCAGGCAAGGCCGTATCGTGCCCCCGCTGCGTAACGTCCTGCCGTTACCGTGGATATCCTCTTGACTTTGCGCTGGAGTATCTATAGGCGTACAAGCGCTATTTTTGAACATATTACGTGATGTTTAAAGACCCCATTTGGAGCACAATGTCCGGAGGCGTCCAACCCAAACTGCCTCGCCCTGACGTAGGGTGTTACAAACTGGGTAAAGAGTCCGGCATCTAACAATGTTTCGTGTAGCCTGCAGCAAGGGTCAGTGGGTGTAACGGTAAGGGCCGAGACCCTGGGTGTGGGATAAGCTAACGCGTGTTCCGCTGCATTCCATCTTATTGCCGCCACTTTCGACCGGTACACGGACAAAGTGTCATCCTTAAGTCTTAGCCATGTCACGCGCCCTGTTGACCGTTTTCGAGACATTGCTAAAAACGGCGTGACCAGACTTCTCTGGCGAGGCAGCGCAACAGTGCGTGCGCGCGGTGTTTCACGGCGTAGGGCATTGAATTCGCAGCAAGCTCTCCCACACGAGCGAACAGGTGCACAGCATGTGGTCATGGAATTCTAGCCGATATAGTCTGTCTGCACGCACAGAGCACGTGCTGACCCACGCCGTATGATTTACTCCAAGGCGTAGGACAGTTGGTTACACCGATGAATTCTATGTAGGTCATCGACGGTACCGGATAATCTCCGGATGTTCGCGAGTTTCGCGAGGTTCCGGAGCGGCTATAGGCACTTTCCCACCAGTTTAGTGCAACAGCATGGTGAGTGTCCCTCATCTATACCGTGACAAAGTTTGACTGGCACTTTGCTTATCTTCTAGTGATCG"
    p_2 = "ACACCAGAGCAACGGGGGACCGCTCCATAGAATTACCCCACAGGGTGGAAGATGGAATGACTTACACCGCGGATTCTATATAAACATCGCGTTGCAACGGATAACCACCCTGAGTGTTTGCAAATTACAAGATTCCGGCTCGGCTATAAACACTCGTCCACCAATCACAGAGCAATCTAATGGGGGTTCCCTGTCTATGCCGTGATACAGTTTAACAGCACTGTTGCTTCTCTTTCATGACTAGCAAATCTCCCTAGGACTTCGGGGACGCTTGATTTCTGGTTGCGAATATCTGATTGCCTACCAACGCTAGGAACTATCAGCTCTCTCCTGAGTGTGCAGCGAGTCCAGTAACGTAGTTTGATCCGACGTGGGTATAATTTAACAAATCAGCTACACCTCGTTCTAGCATGAGCCCGATCAGTGCATCCGATCAGTCCGCCCACGGGGTAATGGCCGTGTAGCATTAATGCGAAAATAAAGAAGATAACCGGTCGCTTCTTGGACATGCTGGCCGTAGAGATCCTGAAGAGGGGTCATAAACTCACGTAGATATGAGGGGGTACATCGTAGTCGTAGATAGAAGCTTCACGTGTAGATAATGTGTGGGGGCTGCCTCACCCCCGGCGTCGGGACGTGCAATAACTCACACCGCAACGTACTCCGCTTTAAAGTGTCTATTATAGTGCGGCTTTGCTCTATTAGATTATGAGTCAATAGAACAGCCGCGTGCATCACAATTTGCGCTAAACACTACGTTGTATGAGTACTTCTAGAACCGACGCGAAGGATAATTCTCTGGCCTTCAGATTGGATCCCAAGCAAAAAGCTACTAGTCAGATTGGCACATGAAACTGGAACATCGAGACGGTTATGTCTAGACAGACCTTGTCGTTACGAGGACGCACT"

    r_1, r_2, r_3 = function(p_1, p_2)

    print(r_1)
    print(r_2)
    print(r_3)
