import copy

initial = [[1,2,3],[-1,4,6],[7,5,8]]
temp = initial.copy()
goal = [[1,2,3],[4,5,6],[7,8,-1]]


def make_copy(matrix):
    f = []
    for i in range(len(matrix)):
        f.append(matrix[i])
    return f

def displaced(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != goal[i][j]:
                count = count + 1
    
    return count

def isValidPos(i, j):
    if (i < 0 or j < 0 or i >2  or j >2):
        return 0
    return 1

def getAdjacent(matrix, i, j):
    v = []

    if (isValidPos(i - 1, j)):
        v.append(matrix[i - 1][j])
    if (isValidPos(i, j-1)):
        v.append(matrix[i][j-1])
    if (isValidPos(i + 1, j)):
        v.append(matrix[i + 1][j])
    if (isValidPos(i, j + 1)):
        v.append(matrix[i][j + 1])
 
    return v


def printmatrix(matrix):
    for i in range(len(matrix)):
        t = []
        for j in range(len(matrix)):
            t.append(matrix[i][j])
        for k in range(len(t)):
            print(t[k],end = " ")
        print()
  

def pos(matrix,element):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==element:
                return i,j
                exit()
    return 0,0

def swap(matrix,a,b):
    ai,aj=pos(matrix,a)
    # print(f"HELLO ==== {ai},{aj}")
    bi,bj=pos(matrix,b)
    
    a1=matrix[ai][aj]
    a2=matrix[bi][bj]
    
    tp = a1
    a1 = a2
    a2 = tp
    
    matrix[ai][aj]=a1
    matrix[bi][bj]=a2
    

tpi,tpj = pos(temp,-1)

gn = -1
fn = 0

print("Initial board")
printmatrix(temp)  
print("  |")
print("  |")
print("  ↓")


def Astar(temp,goal,gn):
    minimum = 10000
    hn = displaced(temp)
    i1,j1= pos(temp,-1)
    gn = gn+1 
    
    vt = getAdjacent(temp, i1, j1)
    # print("debuggg ==========",vt)
    chk_min = []
    
    for element in vt:
        # print("element ===== ",element)
        chk_min_ele = []
        temp_matrix = [row[:] for row in temp]
        swap(temp_matrix,element,-1)
        hn = displaced(temp_matrix)
        # print("HN        =======================  ",hn)
        # printmatrix(temp_matrix)
        fn = gn + hn
        # print(fn)
        chk_min_ele.append(fn)
        chk_min_ele.append(element)
        chk_min.append(chk_min_ele)
        
    # print("DEBUG2  ===========  ",chk_min)
    
    number_to_swap = 0

    for element in chk_min:
        if element[0]<minimum:
            minimum = element[0]
            number_to_swap = element[1]
            
    # print("Number to be swapped ====== ",number_to_swap)
    
    swap(temp, number_to_swap, -1)
    # print()
    printmatrix(temp)
    chki,chkj=pos(temp,-1)
    
    if (chki==2 and chkj==2):
        print("THE GOAL STATE HAS BEEN REACHED")
        exit()
    else:
        print("  |")
        print("  |")
        print("  ↓")
        Astar(temp, goal,gn)
        

Astar(temp,goal,gn)
