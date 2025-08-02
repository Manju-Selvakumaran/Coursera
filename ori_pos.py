def skew_fn(genome):
    skew = 0
    result = [0,]
    for nucleo in genome:
        if nucleo == "A" :
            skew = skew
        elif nucleo == "T" :
            skew = skew
        elif nucleo == "G" :
            skew = skew +1
        else :
            skew = skew -1
        result.append(skew)
    print(result)
    ori = min(result)
    indices = []
    for index , value  in enumerate(result) :
        if value == ori :
            indices.append(index)
    return indices

genomeee = input("Enter the genome string:")
print(skew_fn(genomeee))
