matrix = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8],
          [9, 10, 11]]
for i in matrix:
    for j in i:
        if j != 7:
            print (j)
    print()