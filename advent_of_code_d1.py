file  = open("advent_input.txt", "r")
lines = file.readlines()
first = -1
last = -1
sum = 0
dictNums = {"zero": "zer0o", "one": "on1e", "two": "tw2o", "three": "thre3e", "four": "fou4r", "five": "fiv5e", "six": "si6x", "seven": "seve7n", "eight": "eigh8t", "nine": "nin9e"}
for i in dictNums.keys():
    lines = [line.replace(i, dictNums[i]+i) for line in lines]
for line in lines:
    # for i in dictNums.keys():
    #     line = line.replace(i, dictNums[i])
    for i in line:
        if i.isnumeric():
            if first != -1:
                last = i
            else:
                first = i
    if last == -1:
        last = first
    #print(first, last)
    num = int(first) * 10 + int(last)
    first = -1
    last = -1
    sum += num
print(sum)

file.close()
            