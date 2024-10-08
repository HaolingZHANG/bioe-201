from numpy import zeros, max
from typing import Tuple


PAM250 = {"A": {"A": +2, "C": -2, "D": +0, "E": +0, "F": -3, "G": +1, "H": -1, "I": -1, "K": -1, "L": -2,
                "M": -1, "N": +0, "P": +1, "Q": +0, "R": -2, "S": +1, "T": +1, "V": +0, "W": -6, "Y": -3},
          "C": {"A": -2, "C": 12, "D": -5, "E": -5, "F": -4, "G": -3, "H": -3, "I": -2, "K": -5, "L": -6,
                "M": -5, "N": -4, "P": -3, "Q": -5, "R": -4, "S": +0, "T": -2, "V": -2, "W": -8, "Y": +0},
          "D": {"A": +0, "C": -5, "D": +4, "E": +3, "F": -6, "G": +1, "H": +1, "I": -2, "K": +0, "L": -4,
                "M": -3, "N": +2, "P": -1, "Q": +2, "R": -1, "S": +0, "T": +0, "V": -2, "W": -7, "Y": -4},
          "E": {"A": +0, "C": -5, "D": +3, "E": +4, "F": -5, "G": +0, "H": +1, "I": -2, "K": +0, "L": -3,
                "M": -2, "N": +1, "P": -1, "Q": +2, "R": -1, "S": +0, "T": +0, "V": -2, "W": -7, "Y": -4},
          "F": {"A": -3, "C": -4, "D": -6, "E": -5, "F": +9, "G": -5, "H": -2, "I": +1, "K": -5, "L": +2,
                "M": +0, "N": -3, "P": -5, "Q": -5, "R": -4, "S": -3, "T": -3, "V": -1, "W": +0, "Y": +7},
          "G": {"A": +1, "C": -3, "D": +1, "E": +0, "F": -5, "G": +5, "H": -2, "I": -3, "K": -2, "L": -4,
                "M": -3, "N": +0, "P": +0, "Q": -1, "R": -3, "S": +1, "T": +0, "V": -1, "W": -7, "Y": -5},
          "H": {"A": -1, "C": -3, "D": +1, "E": +1, "F": -2, "G": -2, "H": +6, "I": -2, "K": +0, "L": -2,
                "M": -2, "N": +2, "P": +0, "Q": +3, "R": +2, "S": -1, "T": -1, "V": -2, "W": -3, "Y": +0},
          "I": {"A": -1, "C": -2, "D": -2, "E": -2, "F": +1, "G": -3, "H": -2, "I": +5, "K": -2, "L": +2,
                "M": +2, "N": -2, "P": -2, "Q": -2, "R": -2, "S": -1, "T": +0, "V": +4, "W": -5, "Y": -1},
          "K": {"A": -1, "C": -5, "D": +0, "E": +0, "F": -5, "G": -2, "H": +0, "I": -2, "K": +5, "L": -3,
                "M": +0, "N": +1, "P": -1, "Q": +1, "R": +3, "S": +0, "T": +0, "V": -2, "W": -3, "Y": -4},
          "L": {"A": -2, "C": -6, "D": -4, "E": -3, "F": +2, "G": -4, "H": -2, "I": +2, "K": -3, "L": +6,
                "M": +4, "N": -3, "P": -3, "Q": -2, "R": -3, "S": -3, "T": -2, "V": +2, "W": -2, "Y": -1},
          "M": {"A": -1, "C": -5, "D": -3, "E": -2, "F": +0, "G": -3, "H": -2, "I": +2, "K": +0, "L": +4,
                "M": +6, "N": -2, "P": -2, "Q": -1, "R": +0, "S": -2, "T": -1, "V": +2, "W": -4, "Y": -2},
          "N": {"A": +0, "C": -4, "D": +2, "E": +1, "F": -3, "G": +0, "H": +2, "I": -2, "K": +1, "L": -3,
                "M": -2, "N": +2, "P": +0, "Q": +1, "R": +0, "S": +1, "T": +0, "V": -2, "W": -4, "Y": -2},
          "P": {"A": +1, "C": -3, "D": -1, "E": -1, "F": -5, "G": +0, "H": +0, "I": -2, "K": -1, "L": -3,
                "M": -2, "N": +0, "P": +6, "Q": +0, "R": +0, "S": +1, "T": +0, "V": -1, "W": -6, "Y": -5},
          "Q": {"A": +0, "C": -5, "D": +2, "E": +2, "F": -5, "G": -1, "H": +3, "I": -2, "K": +1, "L": -2,
                "M": -1, "N": +1, "P": +0, "Q": +4, "R": +1, "S": -1, "T": -1, "V": -2, "W": -5, "Y": -4},
          "R": {"A": -2, "C": -4, "D": -1, "E": -1, "F": -4, "G": -3, "H": +2, "I": -2, "K": +3, "L": -3,
                "M": +0, "N": +0, "P": +0, "Q": +1, "R": +6, "S": +0, "T": -1, "V": -2, "W": +2, "Y": -4},
          "S": {"A": +1, "C": +0, "D": +0, "E": +0, "F": -3, "G": +1, "H": -1, "I": -1, "K": +0, "L": -3,
                "M": -2, "N": +1, "P": +1, "Q": -1, "R": +0, "S": +2, "T": +1, "V": -1, "W": -2, "Y": -3},
          "T": {"A": +1, "C": -2, "D": +0, "E": +0, "F": -3, "G": +0, "H": -1, "I": +0, "K": +0, "L": -2,
                "M": -1, "N": +0, "P": +0, "Q": -1, "R": -1, "S": +1, "T": +3, "V": +0, "W": -5, "Y": -3},
          "V": {"A": +0, "C": -2, "D": -2, "E": -2, "F": -1, "G": -1, "H": -2, "I": +4, "K": -2, "L": +2,
                "M": +2, "N": -2, "P": -1, "Q": -2, "R": -2, "S": -1, "T": +0, "V": +4, "W": -6, "Y": -2},
          "W": {"A": -6, "C": -8, "D": -7, "E": -7, "F": +0, "G": -7, "H": -3, "I": -5, "K": -3, "L": -2,
                "M": -4, "N": -4, "P": -6, "Q": -5, "R": +2, "S": -2, "T": -5, "V": -6, "W": 17, "Y": +0},
          "Y": {"A": -3, "C": +0, "D": -4, "E": -4, "F": +7, "G": -5, "H": +0, "I": -1, "K": -4, "L": -1,
                "M": -2, "N": -2, "P": -5, "Q": -4, "R": -4, "S": -3, "T": -3, "V": -2, "W": +0, "Y": 10}}


def function(sequence_1: str,
             sequence_2: str,
             indel_penalty: int) \
        -> Tuple[int, str, str]:
    # Initialize scoring matrix.
    score_matrix = zeros((len(sequence_1) + 1, len(sequence_2) + 1), dtype=int)
    trace_matrix = zeros((len(sequence_1) + 1, len(sequence_2) + 1), dtype=int)

    maximum_score, maximum_position = None, None

    # Fill the scoring matrix.
    for index_1 in range(1, len(sequence_1)):
        for index_2 in range(1, len(sequence_2)):
            score_1 = score_matrix[index_1 - 1, index_2 - 1] + PAM250[sequence_1[index_1 - 1]][sequence_2[index_2 - 1]]
            score_2 = score_matrix[index_1 - 1, index_2] - indel_penalty
            score_3 = score_matrix[index_1, index_2 - 1] - indel_penalty
            score_matrix[index_1, index_2] = max([score_1, score_2, score_3, 0])
            if score_1 == score_matrix[index_1, index_2]:
                trace_matrix[index_1, index_2] = 1
            elif score_2 == score_matrix[index_1, index_2]:
                trace_matrix[index_1, index_2] = 2
            elif score_3 == score_matrix[index_1, index_2]:
                trace_matrix[index_1, index_2] = 3

            if maximum_score is None or score_matrix[index_1, index_2] > maximum_score:
                maximum_score = score_matrix[index_1, index_2]
                maximum_position = (index_1, index_2)

    # Traceback to find the best alignment pair.
    alignment_1, alignment_2, (index_1, index_2) = "", "", maximum_position
    while trace_matrix[index_1, index_2] != 0:
        if trace_matrix[index_1, index_2] == 1:
            alignment_1 += sequence_1[index_1 - 1]
            alignment_2 += sequence_2[index_2 - 1]
            index_1 -= 1
            index_2 -= 1
        elif trace_matrix[index_1, index_2] == 2:
            alignment_1 += sequence_1[index_1 - 1]
            alignment_2 += "-"
            index_1 -= 1
        else:
            alignment_1 += "-"
            alignment_2 += sequence_2[index_2 - 1]
            index_2 -= 1

    # Reverse the alignments.
    alignment_1 = alignment_1[::-1]
    alignment_2 = alignment_2[::-1]

    return maximum_score, alignment_1, alignment_2


if __name__ == "__main__":
    p_1 = ("ATCDCNMEAEICSVLEGPKGPTSQQRWNCINKHAPKTKHKTFFSPHVIGCKMHIGHYWVRPHMSKFSRFDGNSVRWSCSIPMVEILWWIVGMDHVWLRMWSADFEDW"
           "QQHDQLGESIDDNSHDLAQVCMIWPCDDFPSFERRKEILKPRENKIPGMSHPDVLWLAPMPAYRVYNFKWQPIDPAVSWIRVKMHQVKHKYWGYDQAVFNGHKFIGR"
           "FCVKLRVLDFVFPDTNYVKCVDFWEVSKWTVNGDDMVQMWGQCIAQLSRISFVYKDSDKWDDRRAPGFELGCHYPEDIDQWYTEQIRCCMDQRRANFQVYAYKYARL"
           "PTKTSCHQLTHGNGKWATQNQYHSYRHGRESVTARPVTITAGYAKFKHRDEVPQFHADEVRYDHMSCQYCHDIFLCGYTRTHYATWKEGCCWRGKLGTGALSVHYES"
           "KWSQWYTTFWKQKIEPYKFSLVRNNWYQCVYKRTNPNCSMKRNGQCIVGGFCTHICMYIWDGIATANQQRDDPIHPKNTSIMLDRESFPPSSGPGSEDFLVDGWDGH"
           "SDDTDNNMNGNKYLLYNWHPHHELQRTFQLQASHPQERWNQRGDGQNHFQVHNMPKKCVSHLMRIPGPTVGRAIAVTHMSMEPHRSSKHLWAMLLERVATVGLTDWP"
           "RNLQAKADYFLARGSSSPWNMKMNWCERVPESGHCNQNEYDEAMCLFMPVKYIVITFLVMKMEPLIFMEDHDRVHWKLHQIIFLPKMIKMYCQGKEMHLLSEKYAAD"
           "THDKKESYRYHTQTHRPVCSTDPLNCASGTTDRAIRRYCKGVGMPHSMAKNWNWMMGTVHKDCISHSEAFTPRTVHWKQAMQIIKDAHALQYMSFLDKYYRSCQQSF"
           "AVQTHIEPVSKVLHVDDHKVLVMPTYYIFMCYFVDFSETFYMTLGITSLSMCQWTQFNRCYGEWLFVFRLCPVPTTWMGWMIAQIIDKNWQPPCWQHACMQQWFDNK"
           "AETDSIISKCPCNFQFAMWYTSYVGTRHIQNKACHKRDIALDQGHDNVKIPDGLFLALMVGMFCIEMVKTWMQPHRNANYHQREITNNSVRYYTVHDFTWEMWQLDL"
           "MNGQVYNWTAHCYGWNDKVEHLHKIDSQWEEHPSRAGHTMMQELKQFITSHADANSITQNGLGPWCSRGAFGAEMPNSVAGPFLVSKNFTTYVGPTMCWARKMWSHF"
           "IYFIRGVKWYCQCDSKNRMQSLDSRRDISVQVHCPIPQQIGGCHTQQCPKIMKYHATFTLTFDWYCAPMNSFFTMYQYRDELILWKRCHRMNKVLFFVGYVADNRQN"
           "KFVLTQKCFPAEIYPWHPETEDFRNCVFGGNWMPRLWITDDQKFSMRRHNVPPRMPQMHCTWGNNYPNLHRMIWHYKFIFIEIVKEESITFYPPVFSDGVAYDTGFR"
           "DDPQCSNSQIKQFCWLEAIQEHFVTNILTKDCQAFTKYHPELWTWSEYARYEWQFWSIAHNLNYTKFCWQEIGAVHMTMQEPTNFVFCYFVLMERYINCPRNFWMTR"
           "RTVNPKLNWPNSASQWKPTTTVSECQTSPSRVPLTRTCCKRYWKNGSWTMKFQYMRQMTTCVRSKDKSMWPKLTKIPTHHEVRVCDAGNPPTLILMYNSAMCQQLTG"
           "VLMACNIAFNYWTSIYGVMNRMSIEPTQKCQFISPHHKRRPTSSEMGEYCALRCIDHEKEDIPYHAGAYNKYAFDQRNLTLHSDNHTEHAWMEFAGNKGRFPQCFCC"
           "TDMERIRRQGMWERWDPLIRLSNWAENHVCPFIASIKHYLVTIWITSYMHQGTWARRQTCMKLKRDPWYPCMDCGFANWVISCERIVNWNYPYVYNSRQKWWRRRYM"
           "VMDPIVCWQHAHDTERETPLTVTQQCPKIVVTKNQDAGGCWLKSVKDVLSPKFYFCLPVSEFQMGDFLLINMWHVYNWTFIGFCNPAQPHDLYVDYLIMWHMKAFFR"
           "KACNMWWVVSRFDMDIYAPTWKGVHKMMNSDVNEQMPQDQQHRETNWQDSCYQLLYNRNQNIWIKQDHWIFPRALKKMGTEDTELSRACKNCVHVCHRACWSDDVVD"
           "AHPMFNVLCTDQEMSWPLIAFFWTPIFGGMEICKEQRHRTVIMWVFHYSNLGAATQADRMKHGAKNRMCYIQSWWIKWFNFNLELCPAPICRKCHAFESYLFRSHHG"
           "HKAYRDSFDTKYQTQGNCPNEQSGAWEAPCYPGESHEVQHFTTHMMRSTKNEINPLGMQGMVGPHHTMKKDICNLQELFINFKCKRILHTNDNFVGYNLARSTSWVI"
           "DGYDDREQHTCHDTNSSREHTEVFELGKYTEPSFGSQSEAPLKLTTHVYMWVNKAENKGEMMTSPPIREPIRRPSRMDQDANLESDCQNHNRTPSCKTVDIHRSWPH"
           "NNYNAPSMGWTCYDLFLHHASAFVDPTFCWRDIKQQPFWEEMGDLGTIFQPPGMTHSDRYLDQYEPPKGEVYNTRAYCKKYCMEYIVMLVGIIAAGNMNETCIHKSS"
           "TMYVNVDFVALGAWAVCMKEKPAAPKQCCVSDCVFAWMYDYYYLGSRHPNLNACYNMRACMCTRDWWMGIRDVPLCISVISVQSYWSFKGKYIYVYPPYETDRDPLM"
           "NIMPDVTKKFESNYCDGWWLMWWYRVIDGHMRNHPYGVEVVKDRDLEEELWTIRSCWALILGDRAWMNMWQCVKSYIVSHQYVCWKFLFAPIAKWNSETDTYGWEIF"
           "YEEPMDFAGCNLQIPIVPKSFYMAQ")
    p_2 = ("LSWIENVHDKWPKQMSFIMDPRATPNLIFFNFNSHADCRNECLNNYTPFMNRVRQNWQAMEDHTSAHVWCQEGIKKDMGSVVEPRSRAIMNDAFSGTLFQWDNAWYA"
           "THYTAKWPHDSCSAWRKNAIADPCNGGNTQWEDIPICWPILLLVTQQRRKSLQDWHHMWNMAPFGASINNVPTNIHLGSMAHDLTEQHEHMHWINCRYIPNLMKQAK"
           "EFWLFMWIGFEMTTEVFYDVNCHDLFYADDQNICTMKQITKKWMTWVCLDIGYVIGCFYIDLVNMMSESDICKERVAIRHDGFGWYGDNEHHMEFLMYLVDWEFRII"
           "AITQRNMEDWACCVGTTSYQHTDNNSPRQFSTMIKQQLINQLKEREHIVTSYHDNTLCWGFPNNCQPNYYNTGFWVMVLQCGAWLESDFWHYLHAWYNHEDQETVPK"
           "HQPPDAAWEWRFTDSCSHCEWSVHIKMRKFGAPSGCCSQCACSDIICHNWWNFEESCMFDTQGVNMWCGFNHDIIWVRIGNITTLWQSMKGVMQIDEDMRGLCGHLH"
           "WTHCKCIHDFVSHQPTKRCMPFIAFISHCTVGYEEPPLYYSPIFEEDVLKVYGLTIVIPIEGFISKYIHITWSSWPGDMARVFRTNPPDLPFDQCEHPHSSNWAPFD"
           "HRSFHDQSMPWAIRSRWEQQDFYDLADFIRYQWMKNDLIDGTWFTTAIRIRWAIGCKVASSELHRPCVNPYRNCKCMCIIMDQWNERNQMTFMPYAPWWIIDYTRPN"
           "ILQMTMHMGAMPEMFRCMDACDYSLTFVQMYDAAVKTVHKDCISHSEAFTPRTVHWKRAMFGPQIYRAALQYMSFLDKYYRSCQQFAVYTHISPVSKRGCQLHVDDH"
           "KVLKIQDGLDNMAQYYIGSAFHRAQPMCYFVDISETCYMTWNFTSQGITSLSMCQWTQLNRCYGEWLFVFRLCPVPTTISTVWTTIIEQIIDKNHKPSQTQPPCWLH"
           "ACMQQWFYSYINKSIISRFWDAYQTFFAMWYTSYENALVQGHDNVKIYDGWLALMDGMFCIQMVTWMQPHLSTAKASTMPTCASVRYKQVHDFTWEMWHLDLMNGQV"
           "YSWTAHCYGWNDKVEHLHKIDSQMTVPNDREGEHPSRAGWTMMQELLQFIASHLWWQLFLDANSITQNGLRCETQYIHHPWCSKQFWYCGAFGAEKPNSVANPFLVG"
           "KATVVIYFTTYVGPTMCWAPKFIYFIRGWHKWYCICQSKNRMQSLDSRRDISVIEHCPIPCQFHKLGCGKLHTQQDVDISQATRTLAFDTYCAPMYKRCHRMAYVAD"
           "NRQNKFVLTQKCFPAEIYPWHPETEKPKCVMGGNWMPRLWITDDQKFKSKEFYRRHVVPPRMPQMHHIMTSHDTWGNNPPPVPWYPHLHRMIWHYKFIIVKYESPRD"
           "DPQCSNSQIVYTMKSLDMSFPWFCWLEAIQWTKDCQAFTKYEEDNYCEEWSSLAKAFWSQAHYARRIEFQGLNYTKIGRGVHMTMQEPTNFVFCRAYIAVLMERYIC"
           "PRNFEMTRRTVNPNWTSLNWPNAGVDRGASQWKPTTTVSECQYSPSRVPLTRTCCKRYWKNGSWTMKFQYMRQMTTCVRSKDKSMWPKYEFHEDRYQTKIPTHYEVR"
           "VCDASIPPTLILMYNWKCGAMCQQLTHVLMPCNIDHTFYGVMNRMSIEPTETADFVGDRCQFISPHHKRRPTSSMNMRSHDMGEYCADHEKEDIRCWLKDYHAGAYN"
           "KYQSNGASCAFDQRNLTLHSDNHTEHAWSEFAGNKHENVMVRFPQMERRQGMWERWDPLIRLSNWAENHVCPFVASIAHYLVTIWITQVCLHNKPFGFMHQGTWAVN"
           "LIFPRDPWFPCMDCGFANWETVAQPCKMCIEMMNWNSPSPVSEEWPPNSRQKWWRRRYMVMFPEINNSRPLTVTQQCPKIGGCWSFYFCLPVSGFQMHSTWPVFVNC"
           "WYYNSTPIGRKLRNSEVWCNPAQPHQRCSARQNMLGVAHTLPEQKIKPKILNWVFEKWELDPWIPWQHWGQRMVCYKPFHYGNDEWEGYHREKRVFPWFWLRCRNNL"
           "DWMMIPAHKFKGNGYSDTWLTWRASDMWSKANTFFNQTNMMAYTCWVAASHIQVTMTSAGCQWPDQLSMPNSLNRQCKDDWRWCFNFHYCYKHIFMWVQEFNVTTDG"
           "YYDHLAWQNWEHVKIDLKNGRYWAYNMCGYCPNQFNPVELIQHKGYDPWFAVHWQSGPLGRMWVKPMPSFTLWPQTPMMECRILGSEGMIMKGYVWDKWKVGALNSR"
           "TAGMASNLHPWFSDGQKNRVDSTLKMEIMVYRMWVQDSEAFEPFEDGFEGIQSCGHNDFAKYAYVHHCDWTTALGPDGKFGYVFHHCWWCTQGLHGMLLPGYEQIRK"
           "VEPVVFIDSKWNSGEIQKNLKRKFGTSKQKVIISGEPDTTAVYHPRTAYEPYCMSDDPVGAYPFCSLQVKPTFIKRDSMSKVSANTLPDHFPNNEWWDFYQESAFVI"
           "CLMKMCMDSWWNRYGLVPEFSRKISFDGIRRVFYMGWLMNIDICRRVAKGQAQHDVYINMAMMEGMSTCFDRCTSLWRINDLHYGALLRKDAKPVMIIVFQEARVDT"
           "KFAHMQIKKNDPIKPNWQGWTWHYQWMSFVAAWLANMFYTPEVNMELETNWCCTCPLITFTWIIPAFYRFYPRVHEQHMNRDQIGIGAKMFHNRMAIGLCMRSKWHL"
           "GVRWESNITKEYGCNLNIDPTIEMWRRTMPLWHAAGVGNSPQTPINTKKNDICHFPLLSTWSEIPHDPDS")
    p_3 = 5

    r_1, r_2, r_3 = function(sequence_1=p_1, sequence_2=p_2, indel_penalty=p_3)

    print(r_1)
    print(r_2)
    print(r_3)
