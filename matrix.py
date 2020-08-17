def matrix_init():
    matrix_dimensions = input()

    int_coordinates = [int(x) for x in matrix_dimensions.split(" ")]

    rows = []
    rows_list = []
    for x in range(int_coordinates[0]):
        row_data = input()
        rows_list.append(row_data.split())
        int_coordinates[0] += 1

    for y in rows_list:
        rows_int = [int(x) for x in y]
        rows.append(rows_int)

    return rows


mat1 = matrix_init()
constant = int(input())

for i in mat1:
    result = [a * constant for a in i]
    for i in result:
        print(i, end=" ")
    print()
