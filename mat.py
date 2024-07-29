def print_mat(mat ):
    x=len(mat)
    y=len(mat[0])
    for i in range(x):
        print("\n")
        for j in range(y):
            print(mat[i][j],"  ",end="")

    print("\n")


def element(mat1,mat2,i,j,r):
 
    s=0
    for x in range(r):
        s=s+ mat1[i][x]*mat2[x][j] 
    return s


def produit_mat(mat1,mat2):
    if( len(mat1) == len(mat2[0])):
        mat3=[]

        for i in range(len(mat1)):
            line=[]
            for j in range(len(mat2[0])):
                line.append(element(mat1,mat2,i,j,len(mat1[0])))
            
            mat3.append(line)

        print_mat(mat3)
    else:
        print("nombre des ligne de premier matrice n'egale pas le nombre des columns dans la deuxieme matrice")




mat1 = [[1,2,0],[4,3,-1]]

mat2 = [[5,1],[2,3],[3,4]]



produit_mat(mat1,mat2)

