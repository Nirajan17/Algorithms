# calculating space and time complexity of multiplication of two matrices

def mat_mul(mat1, mat2):
    row1 = len(mat1)
    col1 = len(mat1[0])
    row2 = len(mat2)
    col2 = len(mat2[0])

    if col2 != row1:
        raise ValueError("Incorect Dimensions!!!")

    product = [[0 for _ in range(row1)] for _ in range(col2)]
    partial_sum=0

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                partial_sum += mat1[i][k]*mat2[k][j]
            product[i][j] = partial_sum
            partial_sum = 0

    return product

mat1 = [[1,2,3] , [4,5,6], [7,8,9]]
mat2 = [[9,8,7] , [6,5,4], [3,2,1]]

result = mat_mul(mat1, mat2)

for i in range(len(mat1)):
    for j in range(len(mat2)):
        print(result[i][j], end=" ")
    print(end="\n")



