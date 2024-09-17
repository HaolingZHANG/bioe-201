from itertools import product


def function(sequence: str,
             length: int,
             mismatch: int) \
        -> list:
    patterns = {}
    for location in range(len(sequence) - length + 1):
        pattern = sequence[location: location + length]
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1

    keys, records = ["".join(order) for order in product("ACGT", repeat=length)], {}
    for key in keys:
        records[key] = 0
        for pattern, count in patterns.items():

            difference = 0
            for base_1, base_2 in zip(key, pattern):
                if base_1 != base_2:
                    difference += 1
            if difference <= mismatch:
                records[key] += count

            difference = 0
            for base_1, base_2 in zip(key, pattern[::-1].translate(str.maketrans("ACGT", "TGCA"))):
                if base_1 != base_2:
                    difference += 1
            if difference <= mismatch:
                records[key] += count

    order = sorted(records.items(), key=lambda x: x[1], reverse=True)
    maximum_frequency, included = order[0][1], 0

    for index, (pattern, count) in enumerate(order):
        if count == maximum_frequency:
            included = index + 1
        else:
            break

    return [pair[0] for pair in order[:included]]


if __name__ == '__main__':
    p_1 = "CCGGGCTTACATAGTAAATAGGCAATTAGGCAATCATAGTAAATAGGCAATCTCAGGTCGCCGGGCTTACATAGTAAATAGGCAATCCGGGCTTACCGGGCTTAACTGGTAGCACATAGTAAACTCAGGTCGCTCAGGTCGCATAGTAAATAGGCAATCTCAGGTCGCTCAGGTCGACTGGTAGCACTCAGGTCGTAGGCAATCCGGGCTTACCGGGCTTAACTGGTAGCACATAGTAAACTCAGGTCGTAGGCAATCTCAGGTCGCTCAGGTCGCCGGGCTTACCGGGCTTAACTGGTAGCACATAGTAAACATAGTAAACTCAGGTCGCATAGTAAACCGGGCTTACATAGTAAAACTGGTAGCACATAGTAAAACTGGTAGCACCGGGCTTAACTGGTAGCACATAGTAAACCGGGCTTACCGGGCTTACATAGTAAACCGGGCTTACTCAGGTCGCATAGTAAACCGGGCTTAACTGGTAGCACATAGTAAATAGGCAATACTGGTAGCATAGGCAATCCGGGCTTACTCAGGTCGTAGGCAATCTCAGGTCGACTGGTAGCACCGGGCTTATAGGCAATCCGGGCTTATAGGCAATTAGGCAATACTGGTAGCACATAGTAAACATAGTAAATAGGCAATCTCAGGTCGCATAGTAAACATAGTAAACCGGGCTTACTCAGGTCGCATAGTAAACCGGGCTTACTCAGGTCGTAGGCAATCTCAGGTCGCATAGTAAACATAGTAAACTCAGGTCGTAGGCAATTAGGCAATCTCAGGTCGTAGGCAATTAGGCAATCCGGGCTTACTCAGGTCGCATAGTAAACCGGGCTTATAGGCAATTAGGCAATCATAGTAAACCGGGCTTACTCAGGTCGCTCAGGTCGTAGGCAATACTGGTAGCA"
    p_2 = 7
    p_3 = 2
    print(" ".join(function(p_1, p_2, p_3)))
