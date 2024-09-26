## Question 1

If given the amino acid sequence KVRMFTSELDIMLSVNGPADQIKYFCRHWT*,
what is the number of amino acids in the encoded peptide (not including the stop codon)? 
Additionally, how many bases are contained in the open reading frame of the DNA sequence 
encoding the amino acids (including the stop codon)?

```python
print(len("KVRMFTSELDIMLSVNGPADQIKYFCRHWT"))
print(len("KVRMFTSELDIMLSVNGPADQIKYFCRHWT") * 3 + 3)
```

Answers
```text
30
93
```

## Question 2

Run prodigal on one of the genomes you have previously downloaded.
Using command line tools, count how many genes were annotated
(you can use any of the output formats for this but some are easier than others).

```shell
module load prodigal
prodigal --help
input_file="/home/zhanh0m/ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna"
gff_file="${input_file%.fna}.gff"
prodigal -i "$input_file" -o "$gff_file" -q
cds_count=$(grep -c "CDS" "$gff_file")
echo "File: $gff_file, CDS Count: $cds_count"
```

Answer:
```text
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.gff, CDS Count: 897
```

## Question 3 
Run prodigal on all the genomes you have previously downloaded.
Using command line tools, find which genome has the highest number of genes. 
Put all your code into a shell script, and put your code on the repository on Github 
where you keep your README with the solutions to this assignment.

```shell
module load prodigal
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
```

Answer:
```text
/home/zhanh0m/ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.gff 3594
```

## Question 4
Annotate all genomes you have previously downloaded using prokka instead of prodigal. 
Using shell commands, count the number of coding sequences (CDS) annotated by Prokka. 
Are the total number of genes the same as they were with prodigal? What are the differences?

```shell
module load prodigal
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
```

```text
File: /home/zhanh0m/ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.gff, CDS Count: 3594
File: /home/zhanh0m/ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.gff, CDS Count: 2032
File: /home/zhanh0m/ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.gff, CDS Count: 2383
File: /home/zhanh0m/ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.gff, CDS Count: 3152
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.gff, CDS Count: 1579
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.gff, CDS Count: 1866
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.gff, CDS Count: 3248
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.gff, CDS Count: 1009
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.gff, CDS Count: 1776
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.gff, CDS Count: 897
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.gff, CDS Count: 1063
File: /home/zhanh0m/ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.gff, CDS Count: 1505
File: /home/zhanh0m/ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.gff, CDS Count: 1748
File: /home/zhanh0m/ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.gff, CDS Count: 1063
```

```shell
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
```

```text
File: /home/zhanh0m/tmp/GCA_000006745.1_ASM674v1_genomic.gff, CDS Count: 3589
File: /home/zhanh0m/tmp/GCA_000006825.1_ASM682v1_genomic.gff, CDS Count: 2028
File: /home/zhanh0m/tmp/GCA_000006865.1_ASM686v1_genomic.gff, CDS Count: 2383
File: /home/zhanh0m/tmp/GCA_000007125.1_ASM712v1_genomic.gff, CDS Count: 3150
File: /home/zhanh0m/tmp/GCA_000008525.1_ASM852v1_genomic.gff, CDS Count: 1577
File: /home/zhanh0m/tmp/GCA_000008545.1_ASM854v1_genomic.gff, CDS Count: 1861
File: /home/zhanh0m/tmp/GCA_000008565.1_ASM856v1_genomic.gff, CDS Count: 3245
File: /home/zhanh0m/tmp/GCA_000008605.1_ASM860v1_genomic.gff, CDS Count: 1001
File: /home/zhanh0m/tmp/GCA_000008625.1_ASM862v1_genomic.gff, CDS Count: 1771
File: /home/zhanh0m/tmp/GCA_000008725.1_ASM872v1_genomic.gff, CDS Count: 892
File: /home/zhanh0m/tmp/GCA_000008745.1_ASM874v1_genomic.gff, CDS Count: 1058
File: /home/zhanh0m/tmp/GCA_000008785.1_ASM878v1_genomic.gff, CDS Count: 1504
File: /home/zhanh0m/tmp/GCA_000027305.1_ASM2730v1_genomic.gff, CDS Count: 1748
File: /home/zhanh0m/tmp/GCA_000091085.2_ASM9108v2_genomic.gff, CDS Count: 1056
```


Answer:
```text
The count result of Prokka is less than or equal to Proligal.
```

## Question 5

Extract and list all unique gene names annotated by Prokka using shell commands. 
Provide the command you used and the first five gene names from the list.

```shell
grep "gene=" /home/zhanh0m/tmp/*.gff | awk -F 'gene=' '{if ($2) print $2}' | awk -F ';' '{print $1}' | sort | uniq | head -n 5
```

Answer:
```text
aaaT
aaeA
aaeA_1
aaeA_2
aaeB
```
