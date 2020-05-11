#----------------------------------------------------------------------------------------------------
'''
PROBLEM
    Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

    The trace of a square matrix is the sum of the values on the main diagonal (which runs from the 
    upper left to the lower right).

    An N-by-N square matrix is a Latin square if each cell contains one of N different values, and no 
    value is repeated within a row or a column. In this problem, we will deal only with "natural Latin 
    squares" in which the N values are the integers between 1 and N.

    Given a matrix that contains only integers between 1 and N, we want to compute its trace and check 
    whether it is a natural Latin square. To give some additional information, instead of simply 
    telling us whether the matrix is a natural Latin square or not, please compute the number of 
    rows and the number of columns that contain repeated values.

INPUT
    The first line of the input gives the number of test cases, T. T test cases follow. Each starts 
    with a line containing a single integer N: the size of the matrix to explore. Then, N lines 
    follow. The i-th of these lines contains N integers Mi,1, Mi,2 ..., Mi,N. Mi,j is the integer in 
    the i-th row and j-th column of the matrix.

OUTPUT
    For each test case, output one line containing Case #x: k r c, where x is the test case number 
    (starting from 1), k is the trace of the matrix, r is the number of rows of the matrix that 
    contain repeated elements, and c is the number of columns of the matrix that contain repeated 
    elements.

SAMPLE

Input               Output
3
4
1 2 3 4             Case #1: 4 0 0
2 1 4 3             Case #2: 9 4 4
3 4 1 2             Case #3: 8 0 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3
'''
#---------------------------------------------------------------------------------------------------

def trace(matrix):                                  # Function to find trace of matrix
    tr = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):             # Add elements of main diagonal i.e elements with 
            if i==j:                                # same row and column index
                tr = tr + matrix[i][j]
    return tr

def repRow(matrix):                                 # Function to find the number of rows that have repeated elements
    row = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] in matrix[i][j+1:]:     #  Inc
                row = row + 1
                break
    return row

def makeListOfCol(matrix,j):                        # Function to make a list of the elements present in the curren column
    list = []
    for i in range(len(matrix)):
        list.append(matrix[i][j])
    return list

def repCol(matrix):                                 # Function to find the number of colums that have repeated elements
    col = 0
    for i in range(len(matrix[0])):
        list = makeListOfCol(matrix,i)
        for j in range(len(matrix)):
            if matrix[j][i] in list[j+1:]:
                col = col + 1
                break
    return col

tests = int(input())                                # Input the number of test cases
for i in range(tests):
    n = int(input())                                # Input the number of rows of matrix 
    m = [[] for y in range(n)]                      # Create empty n*n matrix 
    for j in range(n):
        m[j] = [int(x) for x in input().split(' ')] # Input the elements of matrix
    tr = trace(m)
    row = repRow(m)
    col = repCol(m)
    print('Case #%d:'%(i+1),end=' ')
    print(tr,end=' ')
    print(row,end=' ')
    print(col)
    
#----------------------------------------------------------------------------------------------------