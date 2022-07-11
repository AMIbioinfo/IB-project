filename = input("Enter the EMBOSS palindrome filename: ")

sample = open(filename+".txt", 'r')
arr = []
complete_array = []

for lines in sample:
    arr.append(lines)

for words in arr:
    if words[0] == 'P' and len(words)!=13:
        complete_array.append(words)
    elif words[0]>'0' and words[0]<='9':
        complete_array.append(words)

sample.close()

density = open(filename+"density.txt",'a')
palindromes = []
single_sequences = []

for item in complete_array:
    if item[0]!='P':
        palindromes.append(item[9]+item[10]+item[11])

for x in palindromes:
    if single_sequences.count(x) ==0:
        single_sequences.append(x)

for palindrome in single_sequences:
    density.write(palindrome+"  -  "+str(palindromes.count(palindrome)-1)+"\n")

density.close()

print("Density ready at "+filename+"density.txt")