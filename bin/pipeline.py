#!/usr/bin/env python

import os
import sys
import re
import os
import subprocess

species = sys.argv[1]
snps_file = sys.argv[2]
chr_num = sys.argv[3]
start = sys.argv[4]
end = sys.argv[5]
#r_path = sys.argv[6]

######################################################################

def convert_chr (key):
	dict = {
	
		'1':'I',
		'2':'II',
		'3':'III',
		'4':'IV',
		'5':'V',
		'6':'VI',
		'7':'VII',
		'8':'IIX',
		'9':'IX',
		'10':'X',
		'11':'XI',
		'12':'XII',
		'13':'XIII',
		'14':'XIV',
		'15':'XV',
		'16':'XVI',
		'17':'XVII',
		'18':'XVIII',
		'19':'XIX',
		'20':'XX',
		'21':'XXI',
		'22':'XXII',
		'23':'XXIII',
		'24':'XXIV',










		'25':'XXV',
		'26':'XXVI',
		'27':'XXVII',
		'28':'XXVIII',
		'29':'XXIX',
		'30':'XXX',
		'31':'XXXI',
		'32':'XXXII',
		'33':'XXXIII',
		'34':'XXXIV',
		'35':'XXXV',
		'36':'XXXVI',
		'37':'XXXVII',
		'38':'XXXVIII',
		'39':'XXXIX'
			
		}

	return dict[key]

######################################################################

def translate (key):	
	dict = {
		
"thorhynchus_anatinus":"oanatinus_gene_ensembl",
"Taeniopygia_guttata":"tguttata_gene_ensembl",
"Cavia_porcellus":"cporcellus_gene_ensembl",
"Gasterosteus_aculeatus":"gaculeatus_gene_ensembl",
"Loxodonta_africana":"lafricana_gene_ensembl",
"Ictidomys_tridecemlineatus":"itridecemlineatus_gene_ensembl",
"Myotis_lucifugus":"mlucifugus_gene_ensembl",
"Homo_sapiens":"hsapiens_gene_ensembl",
"Choloepus_hoffmanni":"choffmanni_gene_ensembl",
"Ciona_savignyi":"csavignyi_gene_ensembl",
"Felis_catus":"fcatus_gene_ensembl",
"Rattus_norvegicus":"rnorvegicus_gene_ensembl",
"Gallus_gallus":"ggallus_gene_ensembl",
"Tupaia_belangeri":"tbelangeri_gene_ensembl",
"Pelodiscus_sinensis":"psinensis_gene_ensembl",
"Xenopus_tropicalis":"mfuro_gene_ensembl",
"Equus_caballus":"xtropicalis_gene_ensembl",
"Callithrix_jacchus":"ecaballus_gene_ensembl",
"Pongo_abelii":"cjacchus_gene_ensembl",
"Danio_rerio":"pabelii_gene_ensembl",
"Xiphophorus_maculatus":"drerio_gene_ensembl",
"Tetraodon_nigroviridis":"xmaculatus_gene_ensembl",
"Tursiops_truncatus":"tnigroviridis_gene_ensembl",
"Latimeria_chalumnae":"ttruncatus_gene_ensembl",
"Saccharomyces_cerevisiae":"lchalumnae_gene_ensembl",
"Ailuropoda_melanoleuca":"scerevisiae_gene_ensembl",
"Caenorhabditis_elegans":"amelanoleuca_gene_ensembl",
"Macaca_mulatta":"celegans_gene_ensembl",
"Pteropus_vampyrus":"mmulatta_gene_ensembl",
"Monodelphis_domestica":"pvampyrus_gene_ensembl",
"Vicugna_pacos":"mdomestica_gene_ensembl",
"Anolis_carolinensis":"vpacos_gene_ensembl",
"Oreochromis_niloticus":"acarolinensis_gene_ensembl",
"Tarsius_syrichta":"oniloticus_gene_ensembl",

"Otolemur_garnettii":"tsyrichta_gene_ensembl",
"Takifugu_rubripes":"trubripes_gene_ensembl",
"Drosophila_melanogaster":"dmelanogaster_gene_ensembl",
"Petromyzon_marinus":"pmarinus_gene_ensembl",
"Erinaceus_europaeus":"eeuropaeus_gene_ensembl",
"Microcebus_murinus":"mmurinus_gene_ensembl",
"Oryzias_latipes":"olatipes_gene_ensembl",
"Pan_troglodytes":"ptroglodytes_gene_ensembl",
"Echinops_telfairi":"etelfairi_gene_ensembl",
"Ciona_intestinalis":"cintestinalis_gene_ensembl",
"Ochotona_princeps":"oprinceps_gene_ensembl",
"Gorilla_gorilla":"ggorilla_gene_ensembl",
"Dipodomys_ordii":"dordii_gene_ensembl",
"Nomascus_leucogenys":"nleucogenys_gene_ensembl",
"Sus_scrofa":"sscrofa_gene_ensembl",
"Mus_musculus":"mmusculus_gene_ensembl",
"Oryctolagus_cuniculus":"ocuniculus_gene_ensembl",
"Meleagris_gallopavo":"mgallopavo_gene_ensembl",
"Gadus_morhua":"gmorhua_gene_ensembl",
"Sorex_araneus":"saraneus_gene_ensembl",
"Dasypus_novemcinctus":"dnovemcinctus_gene_ensembl",
"Procavia_capensis":"pcapensis_gene_ensembl",
"Bos_taurus":"btaurus_gene_ensembl",
"Macropus_eugenii":"meugenii_gene_ensembl",
"Sarcophilus_harrisii":"sharrisii_gene_ensembl",
"Canis_familia":"cfamiliaris_gene_ensembl"
	}

	return dict[key]











########################################################################################

def R_path_name(path):
	

	os.system("whoami > ../source/getwd.log")

	x = open("../source/getwd.log",'r')

	for line in x:
        	if not re.search("^$",line):
	                print line
	                sub = re.search("^.*\\\(.*)\n",line)
	                user = sub.group(1)

	path_version = path[2:]
	path_version = path_version[:-2]

	#print path_version

	path_lib = "C:/Users/"+user+"/Documents/R/win-library/"+path_version+"/"

	return path_lib

########################################################################################

if __name__ == "__main__":

#	cmd = "\"c:/Program Files/R/"+r_path+"/bin/Rscript.exe\""

	#print cmd

#	r_lib = R_path_name(r_path)

	os.system("rm ../result/*")

	roman_names = ["Saccharomyces_cerevisiae","blabla"]

	for spe_name in roman_names:
		if re.search(species,spe_name):
			os.system("R --vanilla --no-save --args %s %s %s %s < extra_gene.r >../source/temp.log" %(translate(species),convert_chr(chr_num),start,end))	
			
			break
		else:
			continue	
	else:
		os.system("R --vanilla --no-save --args %s %s %s %s < extra_gene.r >../source/temp.log" %(translate(species),chr_num,start,end))
	
        os.system("sed -n '/#CHROM/,$p' %s | tail -n +2 | awk -F \"\t\" '{print $1\"\t\"$2\"\t\"$2\"\t\"$4\"\t\"$5}' > ../source/input_vcf.bed" %(snps_file))
        os.system("bedtools intersect -wa -wb -a ../source/input_vcf.bed -b ../source/utr5.bed | awk -F \"\t\" '{print $10\"\t\"$1\"\t\"$2\"\t[ \"$4\" / \"$5\" ]\tUTR5\"}'> ../source/snps_in_utr5.bed")
        os.system("bedtools intersect -wa -wb -a ../source/input_vcf.bed -b ../source/utr3.bed | awk -F \"\t\" '{print $10\"\t\"$1\"\t\"$2\"\t[ \"$4\" / \"$5\" ]\tUTR3\"}'> ../source/snps_in_utr3.bed")

	os.system("less ../source/exon.bed | awk -F \"\t\" '{print $1\"\t\"$2-5\"\t\"$2+5\"\t\"$4\"\t\"$5\"\t\"$6\"\t\"$7}' > ../source/exon_start_flanking.bed")
	os.system("less ../source/exon.bed | awk -F \"\t\" '{print $1\"\t\"$3-5\"\t\"$3+5\"\t\"$4\"\t\"$5\"\t\"$6\"\t\"$7}' > ../source/exon_end_flanking.bed")
        os.system("bedtools intersect -wa -wb -a ../source/input_vcf.bed -b ../source/exon_start_flanking.bed | awk -F \"\t\" '{print $12\"\t\"$1\"\t\"$2\"\t[ \"$4\" / \"$5\" ]\tSPLICING SITE\"}'> ../source/snps_in_exon_start_flanking.bed")
        os.system("bedtools intersect -wa -wb -a ../source/input_vcf.bed -b ../source/exon_end_flanking.bed | awk -F \"\t\" '{print $12\"\t\"$1\"\t\"$2\"\t[ \"$4\" / \"$5\" ]\tSPLICING SITE\"}'> ../source/snps_in_exon_end_flanking.bed")

	os.system("less ../source/exon.bed | grep \"\-1\" > ../source/exon_negative_strand.bed")
	os.system("less ../source/exon.bed | grep \"\-1\" -v > ../source/exon_positive_strand.bed")

        os.system("bedtools intersect -wa -wb -a ../source/input_vcf.bed -b ../source/exon_positive_strand.bed | awk -F \"\t\" '{print $12\"\t\"$1\"\t\"$2\"\t\"$4\"\t\"$5\"\tCODING REGION\t\"$2-$7+$9\"\t\"$11}' > ../source/pre_snps_in_cds_positive.txt")
        os.system("bedtools intersect -wa -wb -a ../source/input_vcf.bed -b ../source/exon_negative_strand.bed | awk -F \"\t\" '{print $12\"\t\"$1\"\t\"$2\"\t\"$4\"\t\"$5\"\tCODING REGION\t\"$8-$2+$9\"\t\"$11}' > ../source/pre_snps_in_cds_negative.txt")
	os.system("cat ../source/pre_snps_in_cds_positive.txt ../source/pre_snps_in_cds_negative.txt > ../source/pre_snps_in_cds.txt")
	os.system("less ../source/pre_snps_in_cds.txt | cut -f1 | sort -u > ../source/trans_titles.txt")
	
	os.system("R --vanilla --no-save --args %s ../source/trans_titles.txt < extra_gene_2.r >../source/temp_2.log" %(translate(species)))
	os.system("python detect_snps_in_coding_regions.py > ../source/snps_in_coding_regions.txt")
	os.system("cat ../source/snps_in_utr5.bed ../source/snps_in_utr3.bed ../source/snps_in_exon_start_flanking.bed ../source/snps_in_exon_end_flanking.bed ../source/snps_in_coding_regions.txt > ../source/total_snps.txt")	
	os.system("R --vanilla --no-save --args %s < convert_gene_ids.r >../source/temp_3.log" %(translate(species)))	










