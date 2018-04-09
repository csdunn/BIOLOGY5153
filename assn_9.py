#!/

#read in the genome(FASTA format) and store it in a variable-use SeqIO for this

#open watermelon.gff
watermelongff = open("/Users/Celeste/Desktop/watermelon_files/watermelon.gff")

#read gff in line by line using a for loop
#split line into list,grab 4th and 5th on list, print it out to the screen, and continue to the next line, print 
for line in watermelongff:
	positions = line.split("\t")   
	start = positions[3]
	stop = positions[4]
	print("start codon is " + start + " and stop codon is " + stop)
	print("start codon is " + start + " and stop codon is " + stop)
	trimmedDNA = [start + ":"  +  stop]
	print(trimmedDNA)

#close gff file
watermelongff.close()

#open watermelon.fsa
watermelonfsa = open("/Users/Celeste/Desktop/watermelon_files/watermelon.fsa")

#use start and stop codon to pull sequence from watermelon.fsa

#print sequence with start and stop codon

