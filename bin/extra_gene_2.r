#!/usr/bin/R

library(biomaRt)

ensembl=useMart("ensembl")
argv <- commandArgs(trailingOnly=T)

titles <- read.csv(argv[2], header = F, sep ="\t")[,1]


mart = useMart("ensembl",dataset=argv[1])

cds_seq = getSequence(id=titles, type="ensembl_transcript_id", seqType="coding", mart = mart)

peptide_seq = getSequence(id=titles, type="ensembl_transcript_id", seqType="peptide", mart = mart)


write.table(cds_seq, "../source/cds_seq.txt", row.names = T, col.names = F, quote = F, sep = "\t")
write.table(peptide_seq, "../source/peptide_seq.txt", row.names = T, col.names = F, quote = F, sep = "\t")
