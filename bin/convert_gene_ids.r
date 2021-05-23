#!/bin/R




argv <- commandArgs(trailingOnly=T)

require("biomaRt")

mart <- useMart(biomart="ENSEMBL_MART_ENSEMBL", dataset=argv[1])

x <- read.csv("../source/total_snps.txt", header = F, sep = "\t")


keys <- x[,1]

annotations <- getBM(
mart=mart,
attributes=c("ensembl_gene_id", "ensembl_transcript_id","external_gene_name","description"),
filter="ensembl_transcript_id",
values=keys,
uniqueRows=TRUE)


match_index <- match(annotations[,2], keys)
x <- x[match_index,]

y <- data.frame(x[,1], annotations,x[,2:ncol(x)])
colnames(y)[1] <- "Transcript Id"
colnames(y)[6] <- "Chromosome"
colnames(y)[7] <- "SNV position"
colnames(y)[8] <- "SNV"
colnames(y)[9] <- "Gene Regions"

write.table(y,"../result/total_snps_annotated.txt", row.names = FALSE, col.names = T, quote=F, sep = "\t")


