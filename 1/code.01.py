def function_1(text: str, pattern: str) -> int:
    count = 0
    for location in range(len(text) - len(pattern) + 1):
        if text[location: location + len(pattern)] == pattern:
            count += 1
    return count


if __name__ == '__main__':
    p_1 = "GTTCGACGGTCGACGGATCGACGGGTCGACGGTTTCGACGGGCTCGACGGCATCGACGGGTCGACGGCGGCGTTTCGACGGTCGACGGGTCGACGGCAAGTCGACGGGCATCGACGGGTCGACGGAAGTCGACGGGCCTCGACGGTTCGACGGATTCGACGGCGTTTCGACGGGCTCGACGGGTCGACGGAGCTCGACGGAATCGACGGTCGACGGTCGACGGCCGCTCCACCTTCGACGGGTGTAGTGTCGACGGTCGACGGTCGACGGAAGTCGACGGACTTCGACGGCCGCTCGACGGCTCGACGGTCCTGAACTCGACGGTCGACGGGACTCGACGGTCGACGGATATTTCGACGGTGTCGACGGTCGACGGCTTACTCGACGGTCGACGGGGTCGACGGGTTCGACGGATAACCCTCGACGGCATCGACGGTCGACGGCATATTTCGACGGATCGACGGAAAGTCGACGGTCGACGGTCGACGGAATCGACGGGCCTCGACGGACTCGACGGGTCGACGGAGTCGACGGATCTCGACGGGCCCCTCGACGGCTAGTCGACGGCATCGACGGTCGACGGTGGTGGTAGTCGACGGTCGACGGTCTCGACGGTCGACGGTTCATCGACGGATCGACGGTCTCTAAAGCATCGACGGGTCGACGGTCGACGGTCGATCGACGGTCGACGGTCCTAATCGACGGTCGACGGTCGACGGCTAACGGTTCTCGACGGTCGACGGTTCGACGGTTTCGACGGTATCGACGGTCGACGGTCGACGGCTCGACGGCCTAGTCGACGGTCGACGGAGCGTCGACGGTATTCGACGGTCGACGGGATTCGACGGTCGACGGGTCGACGGTTCGACGGGTGTTCGACGGTTCGACGGAGTGTCGACGGTCGTCGACGGACTTCGACGGTCTATCGACGGCCTCGACGGGGTCGTCGACGGTACGATCGACGGTGACCAGTCGGGTCGACGGCTCGACGGTATCTCGACGGTCGACGGAGACAACCTCGACGG"
    p_2 = "TCGACGGTC"
    print(function_1(p_1, p_2))