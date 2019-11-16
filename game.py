import Cell

def get_data_user():
    game_row_column = int(input("input row-column number: "))
    game_data = []
    print("Enter column and row data in the end of data enter '0'")

    for j in range(2):
        game_data.append([])
        for i in range(game_row_column):
            game_data[j].append([])
            if j == 0:
                print("Enter rows: ")
                while True:
                    x = int(input("Enter for row " + str(i) + ":"))
                    if x == 0:
                        break
                    game_data[j][i].append(x)
            else:
                print("Enter columns: ")
                while True:
                    x = int(input("Enter for column " + str(i) + ":"))
                    if x == 0:
                        break
                    game_data[j][i].append(x)
    return game_data


def set_true(data):
    final_data = []
    for k in range(2):
        final_data.append([])
        for i in len(data):
            final_data[k].append([])
            for j in len(data[i]):
                final_data[k][i].append({})
                x = 0
                for ij in data[k][i][j]:
                    x += ij
                if x + len(data[k, i, j])-1 > len(data[i]):
                    return False
                elif x + len(data[k, i, j])-1 == len(data[i]):
                    final_data[k][i][j] = {data[k,i,j] : True}

    return final_data
'''
def set_new_data(data: str):
    data = data.split("|")
    for i in range (len(data)):
        for k in data[i].split(','):
            data[i].append(k)
        for j in range(len(data[i])):
            data[i, j] = int(data[i, j])
            if(data[i,j][0] == 0 ):
                data[i,j] = []
    return data

main_data = ["0|9|2,2|3,1,2|1,2,1,2|3,11|1,1,1,2,1|1,1,1,1,1,1|3,1,3,1,1|1,1,1,1,1,1|1,1,1,3,1,1|3,1,1,1,1|1,1,2,1|11,0",
             "9|1,1,1,1|10|2,1,1|1,1,1,1|1,10|1,1,1|1,1,1,1,1|1,9|1,2,1,1,2|2,1,1,1,1|2,1,3,1|3,1|10"]
for i in range(len(main_data)):
    main_data[i] = set_new_data(main_data)
'''

def possible_cells(data):



    return data