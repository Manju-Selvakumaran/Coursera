def maxmap(Text, kmer, times):
    freqtab = dict()
    Txtlen = len(Text)
    for i in range(0, Txtlen - kmer + 1):
        part = Text[i:i + kmer]
        freqtab[part] = freqtab.get(part, 0) + 1

    maxfreqpatterns = set()
    for k, v in freqtab.items():
        if v >= times:
            maxfreqpatterns.add(k)
    return maxfreqpatterns


def FindCLumps(Text, k, L, t):
    kmerinclumps = set()
    lenText = len(Text)
    for i in range(0, lenText - L + 1):
        Window = Text[i:i + L]
        clumps_kmer = maxmap(Window, k, t)
        for evry_kmer in clumps_kmer:
            kmerinclumps.add(evry_kmer)
    return kmerinclumps


# Input from user
istring = input("Enter the complete sequence: ")
kmerlength = int(input("Input the length of the k-mer: "))
windowlen = int(input("Enter the length of the window: "))
notimes = int(input("Enter the times to form a clump: "))

output = FindCLumps(istring, kmerlength, windowlen, notimes)

for otput in output:
    print(otput, end=" ")
print("\nTotal clump k-mers found:", len(output))
