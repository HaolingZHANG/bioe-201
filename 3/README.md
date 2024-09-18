### Install NCBI datasets 

```shell
wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets
```

```text
--2024-09-17 22:54:44--  https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets
Resolving ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)... 130.14.250.31, 130.14.250.11, 130.14.250.7, ...
Connecting to ftp.ncbi.nlm.nih.gov (ftp.ncbi.nlm.nih.gov)|130.14.250.31|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 23121077 (22M)
Saving to: ‘datasets’

datasets                                100%[==============================================================================>]  22.05M  9.52MB/s    in 2.3s

2024-09-17 22:54:48 (9.52 MB/s) - ‘datasets’ saved [23121077/23121077]
```

```shell
chmod +x datasets
export PATH=$PATH:/home/zhanh0m
```

```shell
datasets --help
```

```text
datasets is a command-line tool that is used to query and download biological sequence data
across all domains of life from NCBI databases.

Refer to NCBI's [download and install](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/download-and-install/) documentation for information about getting started with the command-line tools.

Usage
  datasets [command]

Data Retrieval Commands
  summary     Print a data report containing gene, genome, taxonomy or virus metadata
  download    Download a gene, genome or virus dataset as a zip file
  rehydrate   Rehydrate a downloaded, dehydrated dataset

Miscellaneous Commands

  completion  Generate autocompletion scripts

Flags
      --api-key string   Specify an NCBI API key
      --debug            Emit debugging info
      --help             Print detailed help about a datasets command
      --version          Print version of datasets
```

### Download data and further handle

```shell
datasets download genome taxon 2 --released-before 2002-01-01 --released-after 1980-01-01 --assembly-level complete --assembly-source GenBank --include genome
```

```text
Collecting 14 genome records [================================================] 100% 14/14

Downloading: ncbi_dataset.zip    8.39MB valid zip structure -- files not checked

Validating package [================================================] 100% 18/18
```

```shell
unzip ncbi_dataset.zip
rm ncbi_dataset.zip
```

```shell
datasets summary genome taxon 2 --released-before 2002-01-01 --released-after 1980-01-01 --assembly-level complete --assembly-source GenBank > bacteria_genomes_1980_2001.json
```

```shell
jq . bacteria_genomes_1980_2001.json > reformed_data.json
jq -r '.reports[] | [.organism.organism_name, .assembly_stats.gc_percent, .assembly_stats.contig_n50, .assembly_stats.number_of_scaffolds, .assembly_stats.total_sequence_length] | @tsv' reformed_data.json > summary.tsv
rm reformed_data.json
```

### Find the smallest genome

```shell
awk -F'\t' 'NR==1{next} {if(min=="" || $5 < min){min=$5;line=$0}} END{print line}' summary.tsv
```

```text
Chlamydia trachomatis D/UW-3/CX 41.5    1042519 1       1042519
```

### Find the largest genome

```shell
awk -F'\t' 'NR==1{next} {if($5 > max){max=$5;line=$0}} END{print line}' summary.tsv
```

```text
Vibrio cholerae O1 biovar El Tor str. N16961    47.5    2961149 2       4033464
```

### Output the size of smallest genome

```shell
awk -F'\t' 'NR==1{next} {if(min=="" || $5 < min){min=$5;line=$0}} END{print min}' summary.tsv
```

```text
1042519
```

### Output the size of largest genome

```shell
awk -F'\t' 'NR==1{next} {if($5 > max){max=$5;line=$0}} END{print max}' summary.tsv
```

```text
4033464
```

### Find the number of genomes that contain at least two "c" in the species name. 

```shell
awk -F'\t' '{if(gsub(/[Cc]/, "", $1) >= 2) count++} END{print count}' summary.tsv
```

```text
7
```

### Find the number of genomes that contain at least two "c" in the species name. 

```shell
awk -F'\t' '{if(gsub(/[Cc]/, "", $1) >= 2 && $1 !~ /[Cc]occus/) count++} END{print count}' summary.tsv
```

```text
5
```

### Use the find command to find all genome files (FASTA) larger than 3 megabyte.

```shell
find /home/zhanh0m/ncbi_dataset/data/ -name "*.fna" -size +3M
```

```text
/home/zhanh0m/ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.fna
/home/zhanh0m/ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.fna
/home/zhanh0m/ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna
```

### Use the find command to find all genome files (FASTA) larger than 3 megabyte and output the number.

```shell
find /home/zhanh0m/ncbi_dataset/data/ -name "*.fna" -size +3M | wc -l
```

```text
3
```

### Clean

```shell
rm -r ncbi_dataset/
rm README.md
rm md5sum.txt
rm bacteria_genomes_1980_2001.json
rm summary.tsv
```