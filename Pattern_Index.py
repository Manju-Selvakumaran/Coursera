def PatternIndex(Pattern,Genome):
    Genlen = len (Genome)
    Patleng = len(Pattern)
    for i in range(0,Genlen-1):
        if Genome[i:i+Patleng] == Pattern :
            print(i,end = " ")
    return

Pat = input("Enter the pattern: ")
Gen = input("Enter the genome: ")
PatternIndex(Pat,Gen)
