file1 = open("n.txt","r")
output = open("output.txt", "a")

arr = []
final_arr = []

for item in file1:
    palindrome = ''
    for char in item:
        if char == ' ':
            break
        else:
            palindrome = palindrome + char
    arr.append(palindrome)


for item in arr:
    gc_count = 0
    if item[0]=='g' or item[0]=='c':
        gc_count = gc_count+1
    
    if item[1]=='g' or item[1]=='c':
        gc_count = gc_count+1

    if item[2]=='g' or item[2]=='c':
        gc_count = gc_count+1
    
    if gc_count == 0:
        final_arr.append([item, '0%'])
    elif gc_count == 1:
        final_arr.append([item, '33.33%'])
    elif gc_count == 2:
        final_arr.append([item, '66.67%'])
    else:
        final_arr.append([item, '100%'])

for item in final_arr:
    output.write(item[0]+" - "+item[1]+"\n")

output.close()
file1.close()