from argparse import ArgumentParser
from Bio import SeqIO, Seq


def function_1(file_path: str):
    sequences = {}
    for record in SeqIO.parse(file_path, "fasta"):
        sequences[record.id] = str(record.seq)

    return sequences


def function_2_v1(sequence: str) \
        -> list:
    start_codon, stop_codons, orfs = "ATG", ["TAA", "TAG", "TGA"], []

    # check three different ORFs
    for frame in range(3):
        # check the current ORF.
        start_positions = []
        for location in range(frame, len(sequence), 3):
            codon = str(sequence[location: location + 3])
            if codon == start_codon:
                start_positions.append(location)
            elif codon in stop_codons:
                while start_positions:
                    start_pos = start_positions.pop(0)
                    orf = sequence[start_pos:location + 3]
                    orfs.append((start_pos, location + 3, orf))

    return orfs


def function_2_v2(sequence: str) \
        -> list:
    forward_orfs = function_2_v1(sequence=sequence)
    reverse_orfs = function_2_v1(sequence=sequence.translate(str.maketrans("ACGT", "TGCA"))[::-1])

    return forward_orfs + reverse_orfs


def function_3(orfs: list,
               minimum_length: int) \
        -> list:
    sequences = set()
    for orf in orfs:
        sequence = str(Seq.Seq(orf[2]).translate(to_stop=True))
        if len(sequence) >= minimum_length:
            sequences.add(sequence)
    return list(sequences)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="FASTA file", required=True)
    parser.add_argument("-l", "--length", help="minimum length of ORF", required=True)
    args = parser.parse_args()

    seqs = function_1(file_path=args.file)
    for key, value in seqs.items():
        results = function_3(function_2_v2(sequence=value), minimum_length=int(args.length))
        with open("/home/zhanh0m/outputs-5/" + args.file[48:61] + ".txt", "a+") as file:
            file.write("find " + str(len(results)) + " ORFs:" + "\n")
        for result in results:
            with open("/home/zhanh0m/outputs-5/" + args.file[48:61] + ".txt", "a+") as file:
                file.write(str(result) + "\n")
