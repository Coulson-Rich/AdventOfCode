RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

def get_input():
    file  = open("advent_input_d2.txt", "r")
    lines = file.readlines()
    file.close()
    return lines
input = get_input()
game_id_sum = 0
for line in input:
    is_counted = True
    ind_colon = line.index(":")
    line_end = line[ind_colon+2:]
    line_end = line_end.replace(" ", "")
    sets = line_end.split(";")
    for i in sets:
        indv_set = i.split(",") 
        for j in indv_set:
            num = 0
            k = 1
            for k in range(1, len(j)):
                if j[k].isdigit():
                    num = num + int(j[k]) * (10*k)
                else:
                    break
            if j[k] == "r":
                if num > RED_LIMIT:
                    is_counted = False
                    break
            elif j[k] == "g":
                if num < GREEN_LIMIT or num > BLUE_LIMIT:
                    is_counted = False
                    break
            elif j[k] == "b":
                if num < BLUE_LIMIT:
                    is_counted = False
                    break
        if is_counted:
            game_id_sum = game_id_sum + int(line[6:ind_colon])
print (game_id_sum)
                    

    
