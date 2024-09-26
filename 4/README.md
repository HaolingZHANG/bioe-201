## Question 1 evaluation using the case sample in rosalind.

```shell
 python gene_finder1.py --file rosalind-sample.fasta
```

## Question 2 evaluation using the case sample in rosalind.

```shell
 python gene_finder2.py --file rosalind-sample.fasta
```

## Question 3 evaluation using the practical sample in rosalind.

```shell
 python gene_finder3.py --file rosalind_orf.txt
```

## Question 4 evaluation using 14 complete bacterial genomes.

```shell
wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets
chmod +x datasets
export PATH=$PATH:/home/zhanh0m
datasets download genome taxon 2 --released-before 2002-01-01 --released-after 1980-01-01 --assembly-level complete --assembly-source GenBank --include genome
unzip ncbi_dataset.zip
rm ncbi_dataset.zip
mkdir outputs-4
source /ibex/user/zhanh0m/venv/bio/bin/activate  # Haoling's bio-relevant virtual environment
find /home/zhanh0m/ncbi_dataset/data/ -name "*.fna" -type f | awk '{ system("python gene_finder4.py --file " $0) }'
zip -r outputs-4.zip outputs-4/
rm -r outputs-4
```

## Question 5 evaluation using 14 complete bacterial genomes (minimum ORF length = 100).

```shell
mkdir outputs-5
find /home/zhanh0m/ncbi_dataset/data/ -name "*.fna" -type f | awk '{ system("python gene_finder5.py --length 100 --file " $0) }'
zip -r outputs-5.zip outputs-5/
rm -r outputs-5
```