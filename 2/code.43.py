from copy import deepcopy
from numpy import ndarray, zeros, max
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


def obtain_score_matrix(sequence_1: str,
                        sequence_2: str,
                        indel_penalty: int) \
        -> ndarray:
    # Initialize scoring matrix.
    score_matrix = zeros((2, len(sequence_1) + 1), dtype=int)
    for index in range(1, len(sequence_1) + 1):
        score_matrix[0, index] = score_matrix[0, index - 1] - indel_penalty

    # Calculate the score.
    for location in range(1, len(sequence_2) + 1):
        score_matrix[1, 0] = score_matrix[0, 0] - indel_penalty
        for index in range(1, len(sequence_1) + 1):
            score_matrix[1, index] = max([
                score_matrix[0, index - 1] + BLOSUM62[sequence_1[index - 1]][sequence_2[location - 1]],  # Match
                score_matrix[0, index] - indel_penalty,  # Delete
                score_matrix[1, index - 1] - indel_penalty  # Insert
            ])
        score_matrix[0] = score_matrix[1]

    return deepcopy(score_matrix[0])


def function(sequence_1: str,
             sequence_2: str,
             indel_penalty: int) \
        -> Tuple[Tuple[int, int], Tuple[int, int]]:
    middle = len(sequence_2) // 2

    # Calculate the forward score to the middle column (from the start).
    former_scores = obtain_score_matrix(sequence_1=sequence_1, sequence_2=sequence_2[:middle],
                                        indel_penalty=indel_penalty)
    # Calculate the backward score to the middle column (from the end).
    latter_scores = obtain_score_matrix(sequence_1=sequence_1[::-1], sequence_2=sequence_2[middle:][::-1],
                                        indel_penalty=indel_penalty)[::-1]

    # Find the maximum combination score and determine the middle edge.
    maximum_score, middle_edge = None, None
    for location in range(len(sequence_1) + 1):
        score = former_scores[location] + latter_scores[location]
        if maximum_score is None or score > maximum_score:
            maximum_score = score
            middle_edge = (location, middle, location + 1, middle + 1)

    # Prevent out of bounds if needed.
    if middle_edge[2] > len(sequence_1):
        middle_edge = (middle_edge[0], middle_edge[1], middle_edge[0], middle_edge[3])

    return (middle_edge[0], middle_edge[1]), (middle_edge[2], middle_edge[3])


if __name__ == "__main__":
    p_1 = ("VHFYVAMMKPVQFEGAMPHWIPINSYMCIPFFCMTIYAMPQVDMYEGVTYLSTKCARFDLFKRSCIRWWDINLHSLGMVWNRAIYGAKCVCTTHDHLFWFEDNGGRN"
           "GLDQEGKICNHWWYFTMKEGEGEFSYGKSLEDNVLTNIGCIRRWTHDWSKPNDLECGLDECDIKPAPDLRWYVCWEEFGHVCNAYPTLYHMWNTMFEAIDAIVDCWI"
           "SNFARVYNWTMDYYYANETPKCPQFHNFWNQTGPEKYIQRMMPAKHQFIAFLGECNNDSIFHHFSPNYEAHRKISRCKPQCECWCICTQDHINGFEKWHGYCFQWYM"
           "LIAAFYMYMLISSREILTMHCLIITCWCMQEVWNSCKTSLKETPVNWFDHHTQYQACTYLIMLLWERAGTVMSQSNRHPRVMLWKAPKSYNPMHDCQYVTHMWYVCL"
           "SSMTRSVYKLQQITRPTCTWDPLCMDMEVKDRVDLRRKDQKVVSYYSCNCGQTSGLTTNTEQILSKIATFLGPCFTPFQTGAMCPGSEVDTNHRETEWVYVDLSYLL"
           "QAHSVNGDMNRTIVQPIEWGVPKLMGGGAQYLWRRCEHSYAQEYLDMNTQGCCPICRHRKYANCAMREIKLRYNMCKKNISYLYKPVYERHFPYTKWNRGGDKMSLK"
           "FELRKWFTVCDTLIPGCTGICRVADFWDFFGFFAVTSHMYERFWWSFMNNFTETDDTLNKYWGQKHCPKRTIRLCNKMHFKINITINQFEGNQIMYVTTRDNNQAYW"
           "AMPWFMLVDSYIVFVTKMRPFDDMLQGFCEDIVLMILEMFLQLFSEPEQQNIAGMTAALEPAWANVGWTYWWRMSKTNMDNGWPHVEMRRMFKLGHELFNMDVMPDQ"
           "PKTESERHWELFKYCYKSFNPDVQDSQASYTWCPQYKWERWVMAPHIVAIGKEETLTGMATTMYIWADCSIFNMYQWYFIEMGINFWIPNKSWVVGVLMPTASFWSY"
           "GFDSFCHYMCNSTKNKPTTIQMCFYNMDIYCIDPEGYNKCMCDYFDWQCDVDNCEGGNAQAFTRGGHLWYSE")
    p_2 = ("MTHEKWEDYNQMGQRAYAYMLIDRHGMVIADRFVKLCIGDFKITKTEHFNIRTHHYLSSIPMWETAPKYMWYLFGCCCKWMYIPCIDQHMLGDERNWTICIENGQKC"
           "KVIMESGTTVKDVKGGFTIFMYIIWGPFECYHFAICFAQWFTIYNGTGTRPSKVTIHTRLMCGWQPMNLMDDHRESTASQYATIFFPRIWKDDFEWIQNQDCLVMYW"
           "EAPWWQEVAPNFWTDYVAWIMALHPDREWNQFYLYWGTQWTNRKDKHNTMDASPPVHGNGQSDSLMIYWWDKKEQDRQNGKNELMHYDYPYDLCGCMCGQEECVIFY"
           "QIEAGISERDLDHGIRYEHACVCSTSDECSMGVCKHCFHIMWIIQPHSFVEYCWMFVQICVLATQILTLDFIRCDSFIRLGAYVDGVMIGFTTRDNYTKYIFWAIAF"
           "DQEYEMETIESNKMWYCRRQMCLTDFNLEFEGGYKKQKVVSYYSCNCGQTSKIAYQWTPFQTGAMCPGSEVDTNARMYKVDLSNGDMNRTNPFQPIWVEVPKLFVCR"
           "LQQGGGAQYLWRRCEHSYAQELSFAMLDMNTQLMSLWKMKIPYECLTNRYQHQLKIPEVQPFPEFQVMRPMMQGTHSYGLKACMEHDIFFYECQPGRQPRSHDKIGS"
           "TMPHRDEFAVMHQSFGVCVSVERMGYTLCRDALHFIRYEFGEWHPQTAQAAFMMPLDNKFMGTWIPSPQLMSYGEYPTKGKDFSTWGFCKMKKMCEPLNVIKRMDVQ"
           "AHGPIKQAWMQFYKYECAVMVESVGFSTRMVAMRYVAHNYFDQWLPNDQRTCYHECKPHPMDQQQENITGNHCDSSNLYCYPYEESNEVQKQYPVTLEIWNFDCFIR"
           "NKPMQQWKANYYVHQETLPGQSHWDSKMGKKNPCWWVWCVHESIHRGKDQNEMGAAVKRHLCVLHEVNKRIGDHWDDWWTPNMKKWPGFCDHHVEWLNALQHTLTSP"
           "SKEEYTMCKMIACRNKSQTRMKHCQPRVWYTCLNVRLTMICFMQARKEVGPRSF")
    p_3 = 5

    r_1, r_2 = function(sequence_1=p_1, sequence_2=p_2, indel_penalty=p_3)
    print(r_1, r_2)
