from itertools import product


def function(sequence: str,
             length: int) -> list:
    patterns = {}
    for location in range(len(sequence) - length + 1):
        pattern = sequence[location: location + length]
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1

    results = []
    for order in product("ACGT", repeat=length):
        pattern = ''.join(order)
        if pattern in patterns:
            results.append(patterns[pattern])
        else:
            results.append(0)

    return results


if __name__ == '__main__':
    p_1 = "GCGGGATGCCACTGAGACCGGGCCGTGGTTGGGAATTTAATGAGGATGCTCGCGAGCTTCGATTTCTGAAAGCTCGTATCATCAGACGGTCGATAGCGCAATGGCAATACGACCGGACATCCCTCTTTTGCGCCTTAAACAACAGCCGGGTGGAATACTGATACAATAACCAATCCACCCTAAGTACTTTTGACATTGGTATCACTTGTTATGTCAAAATGCCACCTCGGCGTGACAGTCACCTATGACTACCCCACCCCGAGGGTATGCAATAGCGCCCATGATACCCTCGATCAGATCGGTCTAACCCATCCCTATGGATTCAACGGCCCCGAGCTGAGGGTACCCGCATGTGGCGCCCAATCAGTCGCCCTTCTAGATATCATCTCGCGCCCACTTTCCAGTGCGAGGTCTAGCCGCGCTCGTAAGTAAGCTCATATTCGATTGCGACTCCACAGATGATGGCGACGGACGATACCTGCTAACCCTTATATTCGGTCTTTTCGCAGACAATCATATTCGCCACAGTTAGTGGCCGTATATATTATGTTGGTATTGACCGGTGCGAAGAGACCCAGTCTCCGAGCATCGTGCTTAGCCTTGGTGGACTCACCCCTTCCAGACTATCTACTCAGT"
    p_2 = 6
    print(" ".join(list(map(str, function(p_1, p_2)))))
