#!/usr/local/bin/python3

def aa_percent(peptide,residue,fig=2):
	counts=0
	length=len(peptide)
	for i in residue:
		counts += peptide.count(i)
	percent=counts/length
	return round(percent,fig)
	
print(aa_percent("MSRSLLLRFLLFLLLLPPLP",['F','S','L'],4))

def base_counter(dna,threshold):
	count=0
	dna=dna.upper()
	length=len(dna)
	for i in dna:
		if i not in ['A','T','C','G']:
			count+=1
	if round(count/length,2)==round(threshold,2):
		return 'TRUE'
	else:
		return 'FALSE'
print(base_counter(dna='ATCGQ',threshold=0.2))

def kmer_counter(dna,kmersize,minifreq):
	dna=dna.upper()
	length=len(dna)
	number=length-kmersize
	list=[]
	for i in range(number+1):
		kmer=dna[i:i+kmersize]
		count=dna.count(kmer)
		if kmer not in list and count > 2:
			print(kmer)
		list.append(kmer)
kmer_counter("ATGCATCATG",2,2)
