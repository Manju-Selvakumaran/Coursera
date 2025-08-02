def maxmap(Text,kmer):
    freqtab = dict()
    Txtlen = len(Text)
    for i in range(0,Txtlen-1):
        part = Text[i:i + kmer]
        if part in freqtab:
            freqtab[part] +=1
        else:
            freqtab[Text[i:i+kmer]] = 1
    maxfreqpatterns = list()
    maxfreq = max(freqtab.values())
    for k,v in freqtab.items():
        if v == maxfreq :
            maxfreqpatterns.append(k)
    return maxfreqpatterns

istring = input("Enter the string of nucleotides: ")
kmersize = int(input ("Enter the k-mer size: "))
maxlist = maxmap(istring,kmersize)
for pat in maxlist:
    print(pat,end=' ')
