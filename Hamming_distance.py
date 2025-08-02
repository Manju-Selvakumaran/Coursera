def hammingd(str1,str2):
    hammingdis = 0
    if len(str1) == len(str2):
        for i in range(0,len(str1)):
            if str1[i] != str2[i]:
                hammingdis = hammingdis+1
    return hammingdis

nucleostring1 = input("Enter the first string: ")
nucleostring2 = input("Enter the second string: ")
print(hammingd(nucleostring1,nucleostring2))
