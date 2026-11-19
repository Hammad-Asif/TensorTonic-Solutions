import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A=np.array(A)
    row,col=A.shape
    output=np.empty((col,row),dtype=int)
    for i in range(row):
        for j in range(col):
            output[j][i]=A[i][j]
    return output
