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
                while (True):
                    x = int(input("Enter for row " + i + ":"))
                    if (x == 0):
                        break;
                    game_data[j][i].append(x)
    return game_data


def set_true(data):
    final_data = []

    for i in len(data):
        final_data.append([])
        for j in len(data[i]):
            final_data[i].append({})
            x = 0
            for ij in data[i][j]:
                x += ij
            if x + len(data[i, j])-1 > len(data[i]):
                return False
            elif x + len(data[i, j])-1 == len(data[i]):
                final_data[i, j, data[i, j]] = True
    return final_data



