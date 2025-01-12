
#question 1
def find_matrix_shape(matrix):
    if not matrix:
        return(0,0)
    rows=len(matrix)
    cols=len(matrix[0])  if rows >0  else 0
    return(rows, cols)



