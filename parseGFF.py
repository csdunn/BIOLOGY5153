#!/

import argparse
from Bio import SeqIO

## add argparse to allow input of the files from the command line 

parser=argparse.ArgumentParser(description="Read in Two files gff and fasta")
parser.add_argument("-fa",help="fasta input file" ,dest="fasta_file", type=str, required=True)
parser.add_argument("-gf",help="gff input filename" ,dest="gff_file", type=str, required=True)
args=parser.parse_args()

#this assings the inputs from command line -fa  as file_fasta 
# -gf input as file_GFF    
file_fasta = args.fasta_file # these match the "dest": dest="input"
file_GFF = args.gff_file # from dest="output"

#open the watermelon file for use in loop 
watermelon = open(file_GFF)

#BioPython to strip the header from fsa file 
for record in SeqIO.parse(file_fasta, "fasta"):
            genome = record.seq

#read gff in line by line using a for loop
#split line into list,grab 4th and 5th on list, print it out to the screen, and continue to the next line, print 
for line in watermelon:
    positions = line.split("\t")   
    start = (positions[3])
    stop = (positions[4])
    print("start codon is " + start + " and stop codon is " + stop)

#change positions to integers, pull sequence from watermelon.fsa, print    
    start_2 = int(positions[3])
    stop_2 = int(positions[4])
    trimmedDNA = genome[start_2:stop_2]
    print(trimmedDNA)

