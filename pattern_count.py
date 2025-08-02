def PatternCount(Text,Pattern):
    count = 0
    Txtlen = len (Text)
    Patleng = len(Pattern)
    for i in range(0,Txtlen-1):
        if Text[i:i+Patleng] == Pattern :
            count = count + 1
    return count
Txt = input("Enter the sequence: ")
Pat = input("Enter the pattern: ")
print (PatternCount(Txt,Pat))
