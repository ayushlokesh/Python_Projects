"""
This is a stub for the comp16321 midterm.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here".

Each method is documented to explain what work is to be placed within it.
"""


def read_mazes():#(s)
    """
        Read in the text file and save the mazes into a python list

        :return: A list of strings denoting each maze
    """

    # Your code here
    maze_strings=open('mazes.txt','r').read().split('\n\n')
    return (maze_strings)#(s)

def validate_mazes(maze_strings):#(s)
    """
        Validate if the input from the text file is correct based on the rules defined

        :param: list maze_strings: The list of strings denoting each maze
        :return: A list of string values in order denoting if the input
            is invalid as defined in the specification
    """

    # Your code here
    counter=0; invalid_count=0; maze_validation=[]
    for a in maze_strings:
        m=0; n=len(a); status=True
        for b in a:
            if b==',':
                m+=1
        o=(n-m)/(m+1)
        count=0; scount=0; ecount=0
        for c in a:
            count+=1
            if c!=',':
                if c=='S':
                    scount+=1
                    if scount==2:
                        status=False
                        break
                elif c=='E':
                    ecount+=1
                    if ecount==2:
                        status=False
                        break
                if c!='1' and c!='0' and c!='E' and c!='S':
                    status=False
                    break
            elif c==',':
                if (count)%(o+1)!=0:
                    status=False
                    break
        if ecount==0 or scount==0:
            status=False
        if status==False:
            maze_strings[counter]='invalid'
            invalid_count+=1
            status=True
        counter+=1
    maze_validation=maze_strings.copy()

    return (maze_validation)#(s)


def transform_input(maze_strings, maze_validation):#(s)
    """
        Transform the valid mazes into a 2d array and combine the list with the maze validation
        list as defined in the specification

        :param: list maze_strings: The list of strings denoting each maze
        :param: list maze_strings: The list of string values in order denoting if the input
            is incorrect based on the described rules
        :return: A list of 2d arrays and string values in order denoting mazes and invalid inputs as
            defined in the specification
    """

    # Your code here
    for x in range(len(maze_validation)):
        if maze_validation[x]!='invalid':
            maze_validation[x]=maze_validation[x].split(',').copy()
            for y in range(len(maze_validation[x])):
                maze_validation[x][y]=list(maze_validation[x][y]).copy()
                for z in range(len(maze_validation[x][y])):
                    if maze_validation[x][y][z]!='E' and maze_validation[x][y][z]!='S':
                        maze_validation[x][y][z]=int(maze_validation[x][y][z])
    transformed_maze_validation=maze_validation.copy()
    return (transformed_maze_validation)#(s)


def solve_mazes(transformed_maze_validation):#(s)
    """
        Determine if each valid maze is solvable and then solve them by providing the coordinates
        in the order required to traverse the maze from start to end

        :param: The list of 2d arrays and string values in order denoting mazes and invalid inputs
        :return: A list of coordinate lists and string values in order denoting solutions, invalid inputs
            and unsolvable mazes as defined in the specification

    """

    # Your code here
    solved_transformed_maze_validation=[]; sol=[]
    for a in transformed_maze_validation:
        sol=[]
        if a!='invalid':
            E=[]; S=[]; size_x=len(a[0]); size_y=len(a);steps=[]
            for b in range(len(a)):
                for c in range(len(a[b])):
                    if a[b][c]=='S':
                        S.append(b)
                        S.append(c)
                    elif a[b][c]=='E':
                        E.append(b)
                        E.append(c)
            steps.append(S)
            already=[]
            while E not in steps:
                if S[0]+1!=size_y and S[0]-1!=-1 and S[1]+1!=size_x and S[1]-1!=-1:
                    solved_transformed_maze_validation.append('unsolvable')
                    break
                if E[0]+1!=size_y and E[0]-1!=-1 and E[1]+1!=size_x and E[1]-1!=-1:
                    solved_transformed_maze_validation.append('unsolvable')
                    break
                z=len(steps); 
                step=steps[z-1]
                if step[1]+1!=size_x and (a[step[0]][step[1]+1]==0 or a[step[0]][step[1]+1]=='E') and ([step[0],step[1]+1] not in steps) and ([step[0],step[1]+1] not in already):
                    steps.append([step[0],step[1]+1])
                elif step[0]-1!=-1 and (a[step[0]-1][step[1]]==0 or a[step[0]-1][step[1]]=='E') and ([step[0]-1,step[1]] not in steps) and ([step[0]-1,step[1]] not in already):
                    steps.append([step[0]-1,step[1]])
                elif step[1]-1!=-1 and (a[step[0]][step[1]-1]==0 or a[step[0]][step[1]-1]=='E') and ([step[0],step[1]-1] not in steps) and ([step[0],step[1]-1] not in already):
                    steps.append([step[0],step[1]-1])
                elif step[0]+1!=size_y and (a[step[0]+1][step[1]]==0 or a[step[0]+1][step[1]]=='E') and ([step[0]+1,step[1]] not in steps) and ([step[0]+1,step[1]] not in already):
                    steps.append([step[0]+1,step[1]])
                
                if len(steps)==z:
                    already.append(steps[z-1])
                    steps.remove(steps[z-1])
                    if z==1:
                        solved_transformed_maze_validation.append('unsolvable')
                        break
                    
                if E in steps:
                    # sol.append(steps)
                    solved_transformed_maze_validation.append(steps)
        else:
            solved_transformed_maze_validation.append('invalid')
    return (solved_transformed_maze_validation)#(s)


if __name__ == '__main__':
    # You can place any ad-hoc testing here
    # i.e mazes = read_mazes()
    # i.e print(mazes)
    pass
