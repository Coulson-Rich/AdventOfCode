RED_LIMIT = 0
GREEN_LIMIT = 0
BLUE_LIMIT = 0

def get_input():
    file  = open("advent_input_d2.txt", "r")
    lines = file.readlines()
    file.close()
    return lines
input = get_input()
all_prod = []
game_id_sum = 0
for line in input:
    ind_colon = line.index(":")
    line_end = line[ind_colon+2:]
    line_end = line_end.replace(" ", "")
    sets = line_end.split(";")
    for i in sets:
        indv_set = i.split(",") 
        for j in indv_set:
            num = 0
            k = 1
            for k in range(0, len(j)):
                if j[k].isdigit():
                    num = int(str(num) + j[k])
                else:
                    break
            if j[k] == "r":
                if num > RED_LIMIT:
                    RED_LIMIT = num
                    
            elif j[k] == "g":
                if num > GREEN_LIMIT:
                    GREEN_LIMIT = num
                    
            elif j[k] == "b":
                if num > BLUE_LIMIT:
                    BLUE_LIMIT = num
    limit_product = RED_LIMIT * GREEN_LIMIT * BLUE_LIMIT
    RED_LIMIT = 0
    GREEN_LIMIT = 0
    BLUE_LIMIT = 0
    all_prod.append(limit_product)

    
print (sum(all_prod))