#!/

#open watermelon.gff
watermelon = open("/Users/Celeste/Desktop/watermelon_files/watermelon.gff")

#open watermelon.fsa
watermelonfsa = open("/Users/Celeste/Desktop/watermelon_files/watermelon.fsa").read()

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
    trimmedDNA_2 = watermelonfsa[start_2:stop_2]
    print(trimmedDNA_2)

