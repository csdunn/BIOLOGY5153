#! /usr/bin/python

#declare sequence
my_dna = "ATGCGTA"

#print sequence
print(my_dna)

#count each nucletide
#NOTE:we are assuming that our sequence is just A,C,G and T
C_count = my_dna.count('C')

print("C count: " + str(C_count))

G_count = my_dna.count('G')

print("G count: " + str(G_count))

#calculate DNA length
dna_length = len(my_dna)

#calculate GC fraction
gc = (G_count + C_count)/dna_length

#print gc fraction out to two decimal places
print(gc)

############start calculating the reverse complement #################

replacement1 = my_dna.replace('A' , 't')

replacement2 = replacement1.replace('T' , 'a')

replacement3 = replacement2.replace('C' , 'g')

replacement4 = replacement3.replace('G' , 'c')

#uppercase everything
dna_comp = replacement4.upper()

#how to reverse a string
print(dna_comp[::-1])

################ trying it with biopython ##############

print ("Trying it with Biopython")

for record in SeqIO.parse("test.fa","fasta"):
	print(record.id)
	print('sequence is ', record.seq)
	print('record complement is ', record.seq.reverse_complement() 

#create a sequence object
#my_seq = (/user/Celeste/Desktop/BIOL5153/test.fa)

#print out some details about it
#print 'seq %s is %i bases long' % (my_seq, len(my_seq))
#print 'reverse complement is %s' % my_seq.reverse_complement()
#print 'protein translation is %s' % my_seq.translate()
