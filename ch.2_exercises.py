#! /usr/bin/python

my_dna = "ATGCGTA"

print(my_dna)

replacement1 = my_dna.replace('A' , 't')

replacement2 = replacement1.replace('T' , 'a')

replacement3 = replacement2.replace('C' , 'g')

replacement4 = replacement3.replace('G' , 'c')

#uppercase everything

dna_comp = replacement4.upper()

#how to reverse a string

print(dna_comp[::-1])

C_count = my_dna.count('C')

print("C count :" + str(C_count))

G_count = my_dna.count('G')

print("G count :" + str(G_count))

dna_length = len(my_dna)

gc = (G_count + C_count)/dna_length

print(gc)
