print("Gathering datas from file...\n")
file = open("n.txt","r")
start = open("starting.txt","r")
ending = open("ending.txt","r")
output = open("output.txt", "a")

raw_list = []
filtered_list = []

for lines in file:
    raw_list.append(lines)

print("Structuring data\n")

for items in raw_list:
    address = ''
    firstAddress = ''
    lastAddress = ''
    for words in items:
        if words == ' ':
            break
        else:
            address = address + words

    firstAddress = address
    address = ''

    line_length = len(items)
    while line_length >= 0:
        if items[line_length-1] == ' ':
            break
        else:
            address = address + items[line_length-1]
            line_length = line_length-1

    for x in reversed(range(len(address))):
        lastAddress = lastAddress + address[x]

    filtered_list.append([firstAddress, lastAddress])

startingLocation = []
endingLocation = []
sequence_array = []

for x in start:
    startingLocation.append(x)

for x in ending:
    endingLocation.append(x)

print("Structuring starting and ending location\n")
for x in range(len(startingLocation)):
    sequence_array.append([startingLocation[x],endingLocation[x]])

#domain sequence_array
#range filtered_list

print("Finding sequence addresses\n")

for item in sequence_array:
    count = 0
    for range in filtered_list:
        print(range[1])
        if int(item[0])<=int(range[0]) and int(range[1])<=int(item[1]):
            count=count+1
    
    item.append(count)
    print(str(int(item[0]))+"-"+str(int(item[1]))+"\t:"+str(count))

print("writting data to the file\n")
for lines in sequence_array:
    output.write(str(int(lines[0]))+"-"+str(int(lines[1]))+":"+str(lines[2])+"\n")

print("Task completed successfully")
output.close()
file.close()
start.close()
ending.close()