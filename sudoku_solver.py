import math

sudoku_grid=[[8,0,0,0,0,5,0,3,9], [0,0,0,3,4,2,8,0,0], [0,6,0,9,1,0,0,7,0],
[7,5,2,0,0,9,0,1,0], [0,0,0,0,0,0,0,0,0], [0,4,0,1,0,0,3,2,5], [0,8,0,0,2,3,0,9,0],
[0,0,6,8,7,4,0,0,0], [5,2,0,6,0,0,0,0,3]]
sizeof_sudoku_grid=len(sudoku_grid)
theset=[]
if sizeof_sudoku_grid==4:
    theset=[1,2,3,4]
elif sizeof_sudoku_grid==9:
    theset=[1,2,3,4,5,6,7,8,9]

zero_set=[]
column_list=[]

c=True
mark=0
area=int(math.sqrt(sizeof_sudoku_grid))
places=0
thecopy=theset.copy()
while c==True:
    c=False
    for i in range(sizeof_sudoku_grid):
        thecopy=theset.copy()
        zero_set=[]
        for j in range(sizeof_sudoku_grid):
            if sudoku_grid[i][j]!=0:
                thecopy.remove(sudoku_grid[i][j])
            else:
                zero_set.append(j)
        for z in thecopy:
            places=0
            for y in zero_set:
                column_list.clear()
                if z not in sudoku_grid[i]:
                    in_row=0
                else:
                    in_row=1
                for r in range(sizeof_sudoku_grid):
                    column_list.append(sudoku_grid[r][y])
                if z not in column_list:
                    in_column=0
                else:
                    in_column=1
                in_block=0
                a=(i//area)*area
                b=(y//area)*area
                for row in range(a,a+area):
                    for col in range(b,b+area):
                        if sudoku_grid[row][col]==z:
                            in_block+=1
                if in_block==0 and in_row==0 and in_column==0:
                    places+=1
                    mark=y
                
            if places==1:
                sudoku_grid[i][mark]=z
                zero_set.remove(mark)
                
            else:
                continue
    for rows in range(sizeof_sudoku_grid):
        for cols in range(sizeof_sudoku_grid):
            if sudoku_grid[rows][cols]==0:
                c=True
    
print(sudoku_grid)
