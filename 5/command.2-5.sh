# Question 2

module load prodigal
input_file="/home/zhanh0m/ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna"
gff_file="${input_file%.fna}.gff"
prodigal -i "$input_file" -o "$gff_file" -q
cds_count=$(grep -c "CDS" "$gff_file")
echo "File: $gff_file, CDS Count: $cds_count"

# Question 3

find /home/zhanh0m/ncbi_dataset/data/ -name "*.fna" -type f | awk '{
    ## generate output. gff file path
    gff_file = substr($0, 1, length($0)-4) ".gff";

    # run the prodigal command to generate a. gff file
    system("prodigal -i \"" $0 "\" -o \"" gff_file "\"");

    # count the number of CDS in the. gff file
    "grep -c CDS \"" gff_file "\""

    # print the result.
    print gff_file, cds_count;
}' | sort -k2 -n | tail -n 1

# Question 4

find /home/zhanh0m/ncbi_dataset/data/ -name "*.fna" -type f | awk '{
    # generate output. gff file path.
    gff_file = substr($0, 1, length($0)-4) ".gff";

    # run the prodigal command to generate a. gff file.
    system("prodigal -i \"" $0 "\" -o \"" gff_file "\" -q");

    # set command line that counting the number of CDS in the. gff file.
    grep_cmd = "grep -c CDS \"" gff_file "\"";

    # obtain number of CDS and save in the grep_result variable.
    grep_result = "";
    grep_cmd | getline grep_result;
    close(grep_cmd);

    # print the result.
    print "File: " gff_file ", CDS Count: " grep_result;
}'

mkdir tmp
module load prokka
find /home/zhanh0m/ncbi_dataset/data/ -name "*.fna" -type f | awk '{
    # generate output. gff file name (keep only the file name and remove the path).
    filename = substr($0, match($0, "[^/]*$"));

    # generate output. gff file path, and set the output path to /home/zhanh0m/tmp/.
    gff_file = "/home/zhanh0m/tmp/" substr(filename, 1, length(filename)-4) ".gff";

    # run the prokka command to generate a. gff file.
    system("prokka --outdir /home/zhanh0m/tmp --force --prefix " substr(filename, 1, length(filename)-4) " \"" $0 "\" > /dev/null 2>&1");

    # set command line that counting the number of CDS in the. gff file.
    grep_cmd = "grep -c CDS \"" gff_file "\"";

    # obtain number of CDS and save in the grep_result variable.
    grep_result = "";
    grep_cmd | getline grep_result;
    close(grep_cmd);

    # print the result.
    print "File: " gff_file ", CDS Count: " grep_result;
}'

# Question 5

grep "gene=" /home/zhanh0m/tmp/*.gff | awk -F 'gene=' '{if ($2) print $2}' | awk -F ';' '{print $1}' | sort | uniq | head -n 5
