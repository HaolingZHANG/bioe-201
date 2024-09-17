def function(pattern: str,
             text: str,
             mismatch: int) \
        -> list:
    records = []
    for location in range(len(text) - len(pattern) + 1):
        difference = sum(base_1 != base_2 for base_1, base_2 in zip(text[location: location + len(pattern)], pattern))
        if difference <= mismatch:
            records.append(location)
    return records


if __name__ == '__main__':
    p_1 = "AGACTGCCATG"
    p_2 = "GGGCCACGATAGCAACCTTAAACTTGCGATTAGTTAATGGTACCAAAAGGTACCTGCGTAAACGTTGAACTACAGGTCCTGCGACGAGGGGTATATTCGATACTTTACCGCCTGGAGGGGCATTGTGGGGCCGCGTTAGAGCGTTGGGATATACTAGGGAATAAGATATTGTCTGTCATTAAGAGCCCTCGTCGTAGAACCTAAGCATAAATAACACGGTCGGCCTAACGCGACCCAGCAGTTGCGCCTCCATCCCCCAATGTTTGCCCTAACCAACTACTCCCGCTTGTACAGGCGGACACAGGGGAGGACCGTCAGCTCAATGCCACGACCATTAAGGGGCTTGTAAGATTAGTTTCCAGCTACGCATACCAGAACCCCGTGTCGTTGAATATTTTGGCATACGAATCGGCCGAGCCTGCTATTATATATCTCCACCAGCGACCCAGCTGCAGCATACCGAGATCCCGCGCGTACGGTTAGGGGAAAACATCATAGGTTTTTGCGGCGCTGCATATGAGCAAGGTATGTCTCTAATTATTTGCTCAGTCCTGTTGAGTAGAAGGTCTCCACAGTAGGCCAAACCCCTAGATCAGGCCCTCCAAACAGGAACGAGCCAGAACATGTGCGGCAGAAACAACACATACCCGATATCTGCATTCATCTTGCGAAGCCTTGACTGCTGGTCGGGAACAGGGCAACAAGAGAAGCGCTCATAGTTAGCAATGCGGGCAATTTCCAATGGCTAGATTTCAAATCTATTTACGCGTTGTCTGTCGCTGCACTGCATAAACAGTATTTCTGCCTACACGGCCAGTGAATCGGAACATCTCCCCGGACGGAGTGCTTAGCAGTCGAGTCCAATGGTACGAACATCGGGGTATGGCTTGGATAGAAATAGTTGCTGACCGTTAGCGATGGAAAGCTGCAAGAAAAACCGCATGCCCATGTCATAGCATTGCGGTACATCCGATGCAGTCACAAGGAAACAGCGTGCGGGACATTTACCCAAGGAAATAATGCGGTATGATGACGGGGATACACCATTTACTCTTGGCCACTGTGCCTCCATACTGCTCCGTCTGGGTACGATAGCGCGCCCGGCCTGCCGCGATGAGATCCGTATATGCTCTTGGGCTGGTCGATGAGTTCTTGTATGGCAAGGTACCCTTTGGAATGCTAAATCAATTACGCATTGTATTCGCCGAAGAGGCGGACTCGTACGATGTAACGATTTTGAAGCGTCCATATGGCGAATTTGCCGTAAGCTCTGCCAGGTAAATAGTGAGCGTATAACTCACTAGATCCAGGGGCCTTAACTTGTCTGAGTCGGAAACCTGCATTCTCGAGTTCTATTGGACAGGGCTGATAAGTCCCTAGCCTAGCAGGCTAGTAATAGGTAGACCGATCGTTCACCTGTGGTGGTGAGCCTCTTTTTCTACGCTCAGGCGAGGCTATCGGGGGCAAGCCAGGGGTAGAATTCATATAGCCGTTTGGGGAAGTACGTGATGAGAGTATAATGGCGTAGGAGGGCAGGGACGGATGGTCGGTTACCCACCCTTGAATTCGTAGCCAGCACTATGCCGCGGCCTCCTCGTGTAGCTGATTCAAGTCTCCGTACAGTCTCGTAAGCGTACGTACATGCTACCGCAAGGAATTACCTAGCCGAGATCAGAGCCCTACCGTAGGGTTACTATACTGGTATTGGACCTTTCGGTTCTAGCGGAATCACAACATTCTACGCACAGCATAGGGTCAATTATCCAGAGTCTCGGGACTAAAGGTGTAGTGCGCACAGGGATGCTGTATACGTTCCCGGTGCTACGTCGGGGAGTTGCGCGATGATGTCATACGCATACTTCAGGCACTGTACGGTAAGACGAATGAATGCGTAGAATCATAACAGAAATCCACCACATTGAGGGCTGGCCGCGTCGGTTTCCTAGACAATTCCCATCTACTTTTGCACTCCGTAGGCCAGTTCACTGTAAGGCTCCATATTCCCGTCTCGGGTCACTTCCGTGCAGTTAAGTCCCAATGAGTCGAAGGGCTAAAGTGGGCAGGCGACAAGAGTATTCCATCGTACGGGTAGTTGGCATAGTGAGGTTATTGCGAGTTTTCACTAGTGTGCTAATGCATTAAGAGATAGCTTTGGTAGTAGTTATCGGCGCTCGGTAGGAACAGGGACACAGCGCGATACATAGTTCACCTTGATTCCAGGAAATCAAGATCAAGGCCACTTTATTCTCCGGCGGTGGTAACTTCTAGGGTGGGAGGATTCCACCCTGAGCCTACACCGGATACGATGAGATGGAAAGGATAGCTGAATGAGTATAACCCTCAGAACAGGCCGCGCTGACCCAGGGGTGCTTCGGGGGGACCAGGTGGCAGAGAAGTCTGTCAAGGACTATTTACAACAGATCATTCGAGGCTTTTCTTTGAACTCAATATGTGAACTGGAGACGGCGTTATTGTTGTGGCAGGAACAATGCCGTAGATCTCTGATCTTCACGATCGCACTAGACGGGACGTCCGCGGCATTGCTGGGCAAAGTACGACGCGAGGTGATTAGAGGCACCAACTAAATACCTCCGTAAGAACTTACCTTCGATACGGTCTCTAGAACTTCGGGTCGCTCTTCGTACCTGTGTCCATACGAACAAGCGCGGCGACATACGAGCTCCCGCTGACATAGGCGCAGCCAGGGGCCACGGGACGTGACTAAGGCTCCGCCCCGTGTCGTCATGAGCTACAGCGTCCCCGAAACGTACCATCTTTAACACCAGGGCCTGACTCGGCACGTTCACGAGCAAGCTCGTGTGCTTCACATTCGTGGATGCACTAGACCGTGAACAGGTCTTTCTATGTCCAATGAGGGCCAGCGTCCTTAAAGGGAGAGAGCTTAGATTATACCAGCGAGACCAAACTCCATTTGAGTTTGCGGCCGAATGACGGTGAGACCTCTTAGGAACTAAGATGTTGTGTACCTGTTCCAGTCCACTCAACTAAGGGATTACCATGCTGCTTGAGCAAGCCACTGATATCTAAGGCATCGAAATCCCAAGCGGGGATGACAAGGAGAGCGCTGCAGCCAGTCATACGCTTAAGTCCTTTAGCTTTACCCGTTATCCCCTGTTGGACTTTGTAAATCCCGAACACTTCTTAGACCACCCCAACATTTTAGAGAATAGACCCGTGGTATGCGCCCCCGCGGCAGGACCCGGTGCGGCGGTTCGAGGATGACTTAAAGGACTGGAAGTTTGTGAGTCATTCATGCCGCTTGCGATTAATAATACTTTTCAATTACGGCCTCCGTAGAATTTATTATTTATAAGATGCTGAAAATGGTTCGGACACGTGACTTTATCGTTCTCAAAAGCAACTCCTGAGAATGAGATAAAAGCCAGATTCGTGTAGGTCCAGAACGTTGCTATTTTTAAGCGGTTCGTCCCTTTCTCAATCAGCACGCTGAGATTCACTCGGTGTCTCGCAAAGAGATGGCCTCGCATCTCTGTTATCGCATCCCACGCAGTCGTCGCCGTACCTAACCCTGCTATATGGATTGCTTTACCCACCGCTCACAACCGAGAGTAAGGGGCTTAGAAATCCAAAGGTAGGCACCGTTTCACATAACTGTGTACTATTAGTCTTTAGTGAGTCTAGAATGGAGAATGGGCTCAATCAGGGCGAGTGTATGGCACGTCCCATCGTTCAGTAACCTCGATCTTAGTCCGTGAAAGTGATACAGGAGCGTAATTGGTTCTGGGCTGCATGGCCGCCATCATATTGATAACTTTTGCGTGATGCTTGCGTCTGGCAAGGCCGACGCTTCGATTGCTTATCTTGCCGTGCACTCATACAAAGCGACGCTCCAAGTGGACTATGAGATAGCCGTATATGTATCTTGTGACTTCTAGTGGAGACTAAGCCAGGCTAAGTCAACTAAGCAATCGCGACCAAACCCCGGGCGTGATAGTCGTAGTGAACGAACTGTTACGTGTTTAGTTGCCAAGTGCCAACGCCAGAGTGAATACGTCTCGAGCCACAAGCCATCTATACGCAGGATGAGGGGATCGTTAATCGGTTTTAGGGCACTTAGCACGGATCAATATATGATCACACGTTACCGTCTGCGTGTCTTGACTGTCGATCGTCAGGGTGCGGGTTAGTACTAGCGCCAAACTCGCTGGCATCTGGGTATCGTCGTCGACTGGTGAGTCCATCACGGGAACTAAGGTACACTTGACAGACGTTATTTCATTGCTATGGACGCTCCTTGCTTTAAACGCTGTAAACTGGACCAAGCCGCGCGCCAAGGGTAAACCCGGAAATGGTACCGGGACACTTGCCATTGGCTAATGAGGTGGCACGCTCTATACTCTTCGACCACTATTGAGGGTCGCACTACAGACTACCTCCAAACATCCATCAACCACGCACAACGTACACAAAACCCGCACTTGCCTAGAAAGAAAAAGCCAGGCAGCGCTCATTGTCAGCTTACCTAGCATTTGCGGCCAGTGAAGCACGGCAGATCGGCCTCTAACGTTACCACTCGCACAGGTGGTGAACTGTCGTTATTGATCGGCACTATCACAGGAAAGTGAGAATAAAGCACTAGATATTACCTCTCACTACTCGGGTTTTACCCGGGATGTATCGTCGCTGCACGATAACGTGAGGACACGAAATGCGTGTAGTTCAGTGTCGTACTGTCCAGTAAAACCCTACGCTCCACGCGTCACTCTGGAGCAGTAGTTTCGATCTCGTAGTCGCGGATACAGACAGTCGCATCGGCGTAGCTTCCGGTGTAACGAAGACAGTCTTGGAATACAAGGAGCTTGCTGTTGTTCGTACCCCAACGTGCCCTGTAATGGACCTCGTAACGATGCTGAGAGCCATACCGCAGGCATTATTCTACCACTGTTAAATGCCGGGTATCCTCTAGACAGCCGTAATAACACTGCGGTCTGTCAATAGCATATGGATGGCAGGAGGATGATCTGGGTTAACTTAAGGAGACACTTCCGTCGGAGCGATATATCCACTCACCCGGCTACCCTCGTGCTGCTCAAGGTATAATGGTGTTGGCGACAGAAGCACCGACGTACCGACTGACTTTTCGCAGTAACGTTGGTAGTCGCAACATCAAAGGCTGTTTTGCTTATGTGTGACTGAGTACCTGTGCCGAAATAATCATGAGAACGAGATAGGAGCTTTCTATCGGCATAGCAGTGAACGAACCGGCCAAACCTGAAAGGATTTAAGAACTGGTGGAGTTAACGCATGTAGACTCACATTTGTTGGTTGCGTCGGTCTAAGTCACTTATATCGAGTGGGACCGTACAACGCGATGCCATCCCATGGCCCACGGACAGCAGATGTTACCCAACCAACGTTAGCACTAAATCGACATTGTGCGGGCCACAGACGAACAATCAAATATTACCCTAAGAGAGAATTCCATGTGAATATCTACACGCATAATACCGACACTACAAACGAGTGGATCCCACGATCAGCTGACTCTTGCCAAGGTATATCTGTCTCACGCGATGCCCGCGTGTAAGCATGAGGTGCGACTTACATAATAGTGGGCAAGAGCAGAACCAGGCCATACGACAGCTAAACTAATTACCTGTAAACGTGTCCCTGCGATTGTCCAGTCGGTCGAGTAGCCTTTTGCAAACATAGGGAGCGCATGCGTACGCGAATCATTTCCAAGCTTAGGGACTCAATTTGCGTAGCTGCGGAAGTGATTTACGACACTTGTCAAACAACTTTTCGGGAGGTGCCTTACGCGCAATTCAAAATAGGGGTTGGCTTGCAAGAAGTCTTGGTGACCTGGCACCGCCAACGGGTCATTGCAGATCTTTGCTGATGAGAGCGATGAGGACGGTAACGACGCTTAATTGCCCAGGAACTTCACCCCAAGTACACCTAGAATCTGTTTGGTAGAACGACATACAGCTCCATAGTCTGAAGTCGTGAAGGTGGGTATGCCTATCACTCAGTAATACTCCCACACCTCTGAGGACGTGATTAATACTGCACTGCAGGAACGACGGATCTGAAAGCCTAACACAAGTTCCTCACGCGCGGGCGAACGAAGCGATTGCCTCTATACCGCGCCCTCTATTAAAGGCCTGAGGACGCCTCGGCGGGGGGGTGGATTTCCTGCTGCTCTCTGTGGCGCTTACTGTCGCGTTGTGTTAGTATGGGCTTGTTTCGCCAATGGTAACCGTATCCTCCTTGCATCCTGTGACCCCTAAAAGGTGTCTCTTATGTAGCGGCATTTTTCGGAAGGGAAGCGCAGGGCGATAGGTTTGATGATGACGTGTAGTAAAAAAACTTGGATATGTATCGGCCACCACTGCCCAGCAAGATTCACCTAGGGGACCAGTAAACTCTGAAGCGGCCTAAATGGGAGCTATTTTTTGAGGATGCGTAATCGTGCCGAGTAACATCCCTGCCTCTTCTGGGAGATAATGACAGGTACGATTATCAGCTCACTTGCGGTTATGGTCATGCACCTTGGCAGCGAGGTTCAGCCATTCACCAAGTCGGGGATCACCACCGGCTCACTTCCTTTAGCACCTCGTCGCTCTGGTATTCTGCTTGAGGTTTTGACCCCTTGGTACATGCTTGCTCAACAGCGGGAGGTCAAGCTTGCCGTAGTCGACCTAGTACCCAAATTCCCCAGGTACTGAGTAAAAGTGGATAACGGATCGTTATTTTCAGAGCTGCTGTAGGGTCTTTGGATACTGGCTCTACCATCCGTCCGCTAGTACTAATAGGTAGTTAACGCAGTGTACACGCGGAGACGCATGCGATATACCTAGCAGTGGGAGCTTTGTTCTATCAAGACCGAGAAGCTAACAGTACCGAGGGTGAATTCGTTTACTGGCATGCGATGATTATATACGTGTTTTTTACCGTTTTGCGATCCACACAATACGGTCATTCGGTCCCCTTGACGGAACTGTCATTACTCATTTACAGGATAGCTAACCAAACGCGGGTGAGGACCTATAAGGCAATGCCTTTTTCGCTCCTAACCTGCACTGCGTCCACCAAGCTACACGAACGGGAATGCAAGCAAGTGCCGAAAGTCCTTACGGGGCACTCGATCAGACAGCTATTTACTCTACAGGATCTTGCAGGGGATTTTATCGAGACGGATTCTAGTCCGGGTTGACGAACGCGCATTGCCTGAGGGTCTTACGGGGGAACTAGTACCCGCAGATCCAATTAACGAAGCATTGGACGTAATCCCCCGCGGGATGAACTGAGCAAGCCTGATGGGGTCTACAGGCTTAGACCCGTTAAGCATTACTGTAATGATGCTACGAGAGTCTAACTCCCCGATTTGGAACCTAGAATGCGGTCTCAAGCCCTCATTTAGTCTGCTGAGTATTGCGTCCGTAATCGAGCAATCCCATATGCACAGCATTCTTAACCGAGAAGAGCGAATAGAAGTCTTACTAAGTCATCATCACTTGCTTCACTACTGTGAATTGGGCTCTATTAAAAATCCGATTCTGAGAGGGTATATGACCCTGGGTCAGAGGTAATAACTTCCTTACGAAACATAAGACGTTTCATAAATAACACATTGTCAGAACCCAGCTAGGTTTTCCCTGTTACTCACGGTTTAAGTGACATCCCATACAACGGTAGGGTGCAGCGCTTAATTACCAATTGGCGGCACCTACGAACATGAACACATTGCCTCAGATTCATAGATCAGTCTCCCCGTGGACCACACCCTTTATAGGGGGGTACTTGCTACACGCTAGATTGTGTAATGTAATCCTATACTGGTGGTGCACTCGACCTAAGTCCCTACGGTCATGGATGTCGGTTTAGTCAGATCTTCACCTGCGGCCACTAAGGGAAGTCATCTCTAGTGTTAGAATTCGAATATGAGGCCGTTTGTCGATCTGTGACGTATATTGGCTACATTTATTCAAATTCACATGAGACAAGCTCGTTTATTGTGGAGGGGTTTAATTTCGTTCAAGATAACTGATCGTGCATTAAAGATGTAGGGGTCTTCATCAGCCTGTCTTTCACCTCGTACCCTCTGGACCGCTCAGAGCTCTAGCACCTGGTCACACCAAGTTTTCCGACCCGTCTTCCGCTCTTTATTGAAGACATCTATCGCGTATAACATACATGGACTTTCGCATAGACACGTGTCGCTTTGTAGTGATTGCAACGTTCTGATGGTGTAACGTTTATGAATCAATTTTCGGACTGAATAGCTGTTGGCCCCGTCCGGGCTATTATCACAACCTCTCCGGATATTCCCGGCGGCCCGCATGAGGTGAATATCGCCACAACGTAGATGTTGCGTATAAGGTTTTGCCATGGAGGGGATTCTGGAATGCCTAGTATGTTTCCCTTGACCCTTGCGGTTAGATTTTACCTGTGATGCCACGTCCAAACTCGGTCGCCTGGGGATGGTTGCCGGTTAAATTGTACCTCACAATGCTGATGGAAAATTCTACTTGAAGGCTTGCGACCCCCTGCCCGGGGGAGGGAAGAGTATAAGACACGCAACTCCCCAAAGTAATACATCCGGCCCAACGTCTGCAGACCATTTCAGCGCATTCAAGGGACTAAGAGTTCTCTTTATCCGATCCGAGCCAGCATAGATTGATGTTAGCTATCCTGATGCTAGGGCGCACAACGAAGGCCGGGTACTCGACGCGTATACACTTATCCGTGAAACGCATCGATCGTCATTGATCCCCCGCAAATCCTTCTGCCCCCACAAAGCGAGGACGCTTCCCTAGAAATGGTTAACGCTTAAAGTAAATACATCGGGCCCACCCGGGATGGAAAGGTGCAGGGTGTGAAACGCTCCGATACCTCTTCTCTACCGGGGTGATGATTCGAACACTGCATTAAGATCGCCTCAATCCTCCTTCTGTATGAGTTCTTTAGAAAATATGTAACACGGTCCGGGTCCTGGGTCAACCTAGTGGTACGCGTTAAAGAAATCAATGTGGTCCTATGCATATAGCAGAGCTTTGTGAACGACCACTTTCATAAGAGCGGTCGGTGGCCTTCTGAAAAATGTCTATCTAGAATCGTAACTCAAGCTACGCGTAGTTCGGTTATTGGGCCATTCTTAGGAGACCTTCTCACGTGTCGGGTGAACAGGCTTGGTGCGGTGGTGCGTGGCCTGGACTGTGACATCGTTGCTCATATGGGATAATGGGGAGGAGGACGACGAATTGTGCAGTTGACCGTGACTACGGAGTTGGCGTATCGATAGCTTATGGGTGATCCCCCGATCGACTGTTAGGCCTTGTGCCTTGTCAACCATCCCAAGGTCGCAGCTTAAGATGACTTGGGGGAGAAATCTGTTAGTCCAAACAACGACCCAAATTCTTGCCTCGATTCGGATTCCAGCCAGCGGTCCGGTCGTTACTCCCGTACGACAGGCACGATCGGCTTGTAAGACGAGCTCAGAATACCCTTCGTGACGTCGGCTATGGTGGAGTTTCACCAAGAAGAGTTATGCGGGGATGATAAAGGTCAATGTAAAAATAGAGCCACGTAGAAGAATTAGTCCGGCACGTTAAGTGTTAACTGTCAGGACGGTGACATGGACTAACCATTTAGTTTCCACGTCTGGTTTTAAGGTTAGTCTTTTTGCTAATGCAAATATGGGTTGCAAGTGGTCTAGTACAGTGCACGTGCTACGAACTGCTACCGTTCGAGGCCTTCCGTGACTGCGCGGTGGCACCCGACGGCAGGCTCCCAACCGCCTGTCTAAGACTCGACGCAGATCCACCTGATCGACCAGCAATACGGGGCTTGTTTAAAAGTACCTAAGACGCTTGGTTCCTCAATGGGGGACGTCCGGGACGAGTGGACAATCCGGCGGTAGCTTAGCACCTAGGGATTTGGACGTCGATCCCCAAAATACCTTTCGGGTGCTGAGCTAAATCTCCTAAAGCACCGAGATCATACATTTCTTACACGGAACAGCGCCGGAGCCGTACTTTATGGGACCTTGGCGACATGACTTCAATTCGTAGATGTCTTGCTGTATAAACACGAGCCACCAGCCCTGTTAATAGACAATACCGAGCAGCAGGCTCTTCATGTCGTCCCGCGAAGCCACAGCAGGCTCTCTCTTCAATGCAGGTTTCTCTAGCTTGAATGCGTCATGTAATAGGCGGCGCCTGTACCCCCATCCTCGCTCTGGCTGTTAGTTAGTCAAAAACCAGAAATTGAAGGAATCGTTTCCCTGAGAGCGGTCTCAGAACACGTAGCGCTTTAACGCTATGGGCAGTCCGTTACGATGACAGTGATCACTGACTTTCAGTATTGAGCTTGTGATAGGAGAGGGGTAACAGCATGTAAAGTACGCGCATGAATGACATCACGGCGATCGCGGGTCTTGACGTTATCTGAGAGCCGTGTTAATCGTCGGTCAGATCCCTCAGGTGAAACTTTCCTTGAAAATATCCCACAAGTCGCCCTAGAGACAAAGAAAGCAGGTACTTTAGGTACCCGTTTAAGGGTAAATGGACGCATACATATACGGAGCAAGTGTGCGGCACGCCGGGCTCTACATTTCTGAGAACTTGTACCAGCGCCCGCGACCGTAGCTAGCAATTGGTAACGGGATAGAGAGATTCTTCAAGGTGGACCCACTAAATAACGCGGATTGGTGGTTTCTCCGTCCCTCACACTTTAGCACGCGTCTTAGAGGCTAGATAGCACCGATAAGTCCAGGGTGTGTCGAGTATCCTTTGGGGCTCAAGAGCACCATGTGCTATAGGCACTAGCCAGGCAGACAAACAGCAGGGCAGTAACAATATTGCCGTCGAGAAGATTGATTTTATCTCGGCCACCTCGGAGATAGATGGGCCGCCAATCGGCCGTTGGTCAGGTACAGTTTTCCTATAGTCCGGCCACTCGGTAATTGCTCGATGCAGTAAAGTCCAGATTCCGTACCGAGCCCGTCAAGGTCTGATGCATAAGACTCGCACGGACTGCCTACTGAGTGTATGGCTTAAAGCTGCCAGGGCGTAATCACTCTTAAGAGCTGCACTTGCGTAGTCAACCGCACGTGCCAACGAAGTTTACCAGCTCTTCCGGTCTTAGTAGAATTGAATAGCCCCATAGCAGGCTGTGGAACACTGTGTATTAGAGCAATTTGTGATGAGTTCATGGAAAGATGCCGCAGGGGCCCTATCGAAGATCACGTTTATGAATCTCTCCATATCCCGGCTAGTTGACCTGACGTGTGCCTACTGGAGTCGGGTCCTACATTAACGCTAATTAGTCCTAATCAGCCATCTCGGCGGCCCTCATGACTAACAAGGGTCCAATGAGTTATTATGATGACAACGCTGGAGCGAGCGGGGTCTCCATGGACGAATCAGTATTTTCATAAGATAGGATTCAGCTCCTTGTGTCATCCCGCACGATATCTGGGTCGTCGCGGATTATCAAAATATCGCCTACTGTGAGAAGTTACCACATGAATGGTAGACATATGCTGCGAAGTTAAACAGAACATCCAACCATGTGAGGTGCATCAGGACGTCATAGTGAGGCCTTACGCATAAGGCGTCATGGTACAACCACCCCGAACGCAACAATGCCTAGCTAAACATTGACTCCAGACTGTCTCATCCTAGACCTGAGAGCTGAGTGCATGCATCGGCAGATTAGTGGAGACGCGCCGTACGAACGTCAAATACGCCTCCCACGACTTAACACAATTCGGGTCCCCTTAATGATTGGACCCTGGTATATTGACTGGGGGTGTCCTTGTATTTATGTGCGGACCACCCTTCTGTCGCGACGATTAACTCGAGAGTCCCGTCCACAATTATTCAATGGGTCGAATTTGACGAGGAACCCCTGTCAAGCTTACCCACGCTTATCGCTCGATCCGATGCCGCAATGGTCAGGACGCTCGGTAAGCATCAGGGCTTACCTCCCGAAATCTGACGCTTATGCGATCTGATTTTTGCCAAACAACAATGCGTCTCCGGCGTGTCGGCATAAAACACTCAGAACTGACGGTCCCGGGGGCACTCCATGACTGGTCCTTCCGGTGAATTAGATGGTGCAGAAATGATTTTTACGGAGTGACAACCTATTGTCCCCAGGGACGAACGGATGTTAAGGTTAAACGACATCCTCCTAGATGATACTTAATACCACGTAATTGGCTCGAGTCGACATCGATAATTATAAAATTCGAATCGTCCTTCACCGCCGCTAGCAGCTCGTAGTACGACGCTCCCGGGAGGGTCATTCGAGTAACTGGCTGAGACCCGCAGACAGCTCCCAAAGGAGTAGGGAGGAGGCTAAGCCACAATTTCGTCTCGGATTAGGATAGACTCCTGCGTTTAATACAGACCGGGGTCACGGCGCACGATCCTCAAACAGCCGGTAGTTGTTGATGGACAACAGTGGTTACAGCGCACGGGATGCAGCCACAAAGCACCCAGGCGCTCAGGCTTATGGAGATTTTTCGCCTGCTAACATAAAAGTCTACCCGATCGAACGAGTTACGCCACGAGCATCACGTCGTACCTGTACGTCTTCCGAAAGGATAAACTGGCGGGCTTTCCATGCAGACTTTCGGCTTATGTCTCATGCAAGACGCTAACCGTTGGATGCGAGTCCCCAGGGTCATAGACTGCGTAACACGCTCTGTGACTCCGCTTTTGCATGTATTGAGAGTCTCTAACCGAAAATAGTCGCGCGTAACTAAACGCAGGATTTGCCATAGGGGGCTGGCCAAAAGTATAAAAACGGACGCGGCCGCAAATCTAGGCGTGATATTCGGCAGAGCAGCAAAATTAATGTCCGTTATAATTTCCTCCCGTAACTGCTTGTTACCCGCACAATTTGTCACACGTTTAGGACATGTAGGCTTTGCTAACCGCTCCTCGTAACTCTCTCTAGGCAATCTCAGGCCTCGTAATGCTCCGCCTGAGACGGGTAGGCGCCTGTACCAGTAGGTGCACTGAATCCAGGGGGACTGGGCATAGAGCAAGTACGAGAGCTTTGCCAGGCAAGTCCTATGCGGGAAAACAAGCGACGCCGCTTAGTGACATAAGCAAGAAAGCAGGGGTCCTCTAGATGCCAATAACCTCGGCACCAATGCTGGTCCCCCCACCGTATTGAAAAGAATTTATCCCTTGAATTCCGTCAAGCGGGCGTGATAGTTAACTGGTTACTCACTTCGGGACTGCTTGAGCAGGAGCGCAAGAAGCAACGCTCGGTAATAGTGTTACCGCTGTATTAGCCTATGTACAGGGCAGTCCAGATACTGCTGCTCAGAGCGTTACTCCCCCGTTGGAGTCATTTCATACAACTTTTTGTCTTACAGGCGCAGAAACTTTGCTGATTGGTCACAGTGTTGCCCAGGGCTTGCCCTGTGATACTGACTACTTTCACTGGGGCAACATGTGCCCACCTTATAGAGAAGACATTGAAAGCAGGAACTGGGATATGCTCTGGGAGATCCTAGATGCGGCGCGGAAGTCCGCCACGCTTAGAAGCGAGGGTATCAGTAACGTTCCGCCTCGTGGAGGAATTCTCGCACGTGTCTTCTCGGTTTAGTTCGTGGCGGGTCGAGGACGGCTTACTCCCTCTAAGGATAGTGAGCTTGTACTACATAGTTCCGATCCCCCACATCGGCAACGTAGTGTCTCGAAATCCCGTAAAGCGTGTATAAGGAACATCACATGAAGACAGGAGTAGGGACCACACGATCCTGGCCGACAGGCTTGTCCCGTGCCCGATTCAGCAAATTTTCTGACGCTACATGTGAGCCTCTATACCCTTTACTATGGGAACTTATACTACTAGAGCCCGGCTAACGCTTCACACCAGCGATTTTTCTGATCTGATGAGGGCATTACATTTTATAAATTGGAGCCTCCAGCACGCGTACCGATGTGGTCGCGGCAAAAGCATAGCTTTCTTGCTTACCCCTACGGATTAAATCCTTTCGAATTTGGTACGCCTGTCTGTTCATAGTATAGCGCCATTCCTAAGCAGTCCGCAAAGACGTCACATGGCTCCTTTAGTGGGGACTTCGTGTACCTTTGGTCTGCAAACATCGCTGACTGGGTCGTACAAGCCGAGAGATGGGACCTGCGCATCGGGAGCTTGATATTTCACGTCGCTAAGCTGTCACCGTTTGGATCTAAAATAATGACTATTCGGTGCTTATCCACAAGGGCAAACTCTGCAGCTACTCCTCCGTATCAAGTGTCTCGACGGTTCGCCCCCCAGTCTCGCTTGCCCTGCGCCCTGCGAGTTTCAGTTCGTTCATTCGGCAGGAAGAGAGCCACCGTTTAAGAGGGTACTTTAGGCCATCTGTTCAAGCGATTCGGCCGGACTTAAGGAACACGGAGATCCGACGGTCCCTCTCAGAATGCACTCTTAGCACTGCTCTATTGAGCCAGCCCGTATTGGTGTAAATGTATAATGACGGGACCGAGACCGAAGTTCTGTAACCAGTTTTAGTACCATGTCGACGCTGGACTACCCCCGACAAAGTGCGTCGAAAAACGCCGCTTCTAATAGCTGAGGCTGAGCTGAGTAAACGACGTAATGCGGCAATAAGGCCTATTCGATTATGAAAACTAGAAAAATTCTTTTTGCACGATGAATGGCTTTCCTCGGAAAAAGCCTCCCTCCCCTACTCTCTTTGGCGACCGCGCTACAGGAGGCTGCTACTAATGGCGCGGCTAATAAGGCTCGTAGGTGATAAAGCCCGAAGTACGTCGCGATAGGATACACTTTTCGCCGTGTAAAACGAGGATGGCATTACGCAGGCCAATTGAAGTCGTCGTCTTACCAATTGAGTTCTGCTGAATAATATCATTACATCAGGTGCATACTTGGCGGCCCGATAACGTAACAATAGAGACGCTCGATTACTACCGGTGGAGGATACTCATGAACGGGACCAAGGCATAAAAAAGGCAGCCATCCGTCAGCCTCCAGTCTTCTTGTACCCGAAAGTAGAGGCCCGTACGAATAATATTCTCTGTGGAGAAGAAATCTGTGAGTCGAGCACACACATCCTTCGACCCAGGCGGGCCTAGTGGCACCACACCCGTACACAGCAGAGGGGCGCACGAATGCCCGTATACGTAATCTTGAGCCTCTGAGCACAGGTCAGAGTAGTGGAGTCATCAGCGGTTCTTCTTTACAGAATCGCGGACCCTGCTCAGGATAAATAGCTATGACGTCGATGTCCTCTGTCACTTAAGTTGAACCGCCCTCAAGTTGGTCCACTTGCGCTAATGCCGCGCCACATAACCATGAGACAATGCTTGTTGAGTATAACCTCAAACACGTCATTTCCTGGCCGCAACATTTATCCGTCCCGTTTTACTAGACCGCCCTGGATACCAAAGAAATCCGTATTCCGCTCGGCTCGTAGGGATCCCATTATGATCTTTTCGATCTTGCTTGGTGTGACTACGAAGGAAAGCGTATCTAGCAGCCCGCGAGATCGGTGGAGCGTTAAGTCACCTCCTCTGGAGTGACCTGATGTCAGGGTACAGTTGGCACCTAGCTCAGCTAGCGTTAAGCAAGGAGCAGGTCACAGAGAAAATTTCAGGTTACCGATTATCGTTTCACCGCACCACAGTCATGGCTATTCTGCACATCTCTGCACTTCCACGGGTAGCGGGTCACGTAGTGTCCCATGTGTTTGACAAGAACAGACTTGGACAGACCAAGATTCTGATAATATTTAGGATAATTTCGCCGTCAAAAGAGTAATACCGGTGACCATGGCGAACTTTGAAAGCTCGTAGTACCAACCCATAAGGTTTCCAGCTCATGTTCCGCTTGTGCCCCTGACCTTCAGATGACGTACCATCGCCTATTAAGCAACCCTAAATAGGCTAGACTGGTTTTAAGCACGGGTGCTAAGCCGCGTGTGTCAGGCTAAGATCACTAGACTGGCCGATAGTGGCTTCTGTTTAGTAAGCTGAGACAGCACATGATGACGAAAGACAAAGTCAGCGAGTGAGACATTGTTAACATAGATTTTCAAAACACTCAATCTGATTCACCCGTACCGCGTCACTTCTGTCGCTTAGGGATCTTCAGGAATCCAACGCCTCGGAACCATGGTACGTCTAATCGTATGACCCTCGTGTGCCCCTACCCGTGAACTGAGTAAGCAAGCAACTTTTAGAGTATTCCAGCCATCCAGTCTTGAGGCTCTTTCCAACAAGCCATCTCACTATCGGCCACCACTTATAATTGGTGCAGCGTGGTATCCGAAGCGCATGGCCGGCCGTTACTGCCATCGAGTGCTAGCATTGAAAGAACTGGGTTAGCATGGGTTCCCTTATCGCAGATCCTATATTCCAATGGAGGTGAGCCTTGAGAGTGTGAACGCAGTGAGTCGGTCATCTAGCTCTGGTGCCCGAGCACGTCGTCAGGGTTCTCAATCGATTTGGAAGCTGAGAAACGATGGCTTAGAAACCCATAGTATCCACCATCCGTGCGGGTGCTCTGTTCACGATGATGCGTAGATAACGGCTACTCATCCAAATACCGTTCGCAGAA"
    p_3 = 6
    print(" ".join(list(map(str, function(p_1, p_2, p_3)))))
