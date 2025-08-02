def dnabox(dbox,gen,hamd):
    dnablen =  len(DNAbox)
    genlen = len(gen)
    DNAbox_index_list = []
    for i in range(0,genlen):
        selnucleo = gen[i:i+dnablen]
        hamdisbound = 0
        if len(selnucleo) == len(DNAbox):
            for counts in range(dnablen):
                if DNAbox[counts] != selnucleo[counts]:
                    hamdisbound = hamdisbound+1
            if hamdisbound <= hamd :
                DNAbox_index_list.append(i)
    LenDNAbos_index_list = len(DNAbox_index_list)
    return LenDNAbos_index_list

DNAbox = input("Enter the pattern of the DNA box : ")
Genome = input("Enter the genome : ")
Hamming_dist = int(input("Enter the pattern of the DNA box : "))

print(dnabox(DNAbox,Genome,Hamming_dist))




