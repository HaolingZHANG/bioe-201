from numpy import zeros, arange, repeat, expand_dims, swapaxes, sum, abs, where
from typing import Tuple


def cmf(sequence: str,
        length: int) \
        -> Tuple[list, int]:
    """
    Find k-mers with maximum frequency in the predetermined DNA sequence.

    :param sequence: predetermined DNA sequence.
    :type sequence: str

    :param length: length of k-mer.
    :type length: int

    :return: determined k-mers and the maximum frequency.
    :rtype: list, int
    """
    patterns = {}
    for location in range(len(sequence) - length + 1):
        pattern = sequence[location: location + length]
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1

    order = sorted(patterns.items(), key=lambda x: x[1], reverse=True)
    maximum_frequency, included = order[0][1], 0

    for index, (pattern, count) in enumerate(order):
        if count == maximum_frequency:
            included = index + 1
        else:
            break

    return [pair[0] for pair in order[:included]], maximum_frequency


if __name__ == '__main__':
    p_1 = "TGGCTGAGTTACCAACCAAATGGCGGTGTAATAATGAGTATGGCTGAGTCAAATGGCAAATGGAATGAGTACGGTGTAATCAAATGGTACCAACTACCAACCAAATGGCAAATGGCGGTGTAATTGGCTGAGTCAAATGGCGGTGTAATCGGTGTAATCGGTGTAATCAAATGGCAAATGGCGGTGTAATTGGCTGAGTCAAATGGTGGCTGAGTCGGTGTAATTGGCTGAGTTGGCTGAGTTGGCTGAGTTACCAACTACCAACCAAATGGCGGTGTAATCAAATGGTGGCTGAGTCAAATGGTGGCTGAGTAATGAGTACAAATGGCGGTGTAATCAAATGGTGGCTGAGTAATGAGTACAAATGGCAAATGGCAAATGGTGGCTGAGTTACCAACAATGAGTACGGTGTAATTGGCTGAGTAATGAGTATGGCTGAGTCGGTGTAATAATGAGTATGGCTGAGTCAAATGGTACCAACCAAATGGTACCAACTACCAACAATGAGTATGGCTGAGTTGGCTGAGTAATGAGTAAATGAGTAAATGAGTACAAATGGCAAATGGCAAATGGAATGAGTATACCAACTACCAACTGGCTGAGTAATGAGTATGGCTGAGTAATGAGTATACCAACTACCAACCAAATGGTGGCTGAGTAATGAGTATGGCTGAGTCGGTGTAATCGGTGTAATCGGTGTAATCAAATGGCGGTGTAATTACCAACTACCAACCGGTGTAATCAAATGGAATGAGTATACCAACCAAATGGTACCAACAATGAGTATGGCTGAGTTACCAACTGGCTGAGTTACCAACAATGAGTACAAATGGCGGTGTAATCAAATGG"
    p_2 = 14
    print(" ".join(cmf(p_1, p_2)[0]))