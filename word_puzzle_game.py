import random 

#function to generate empty grid according to the size that user
#mentioned
def grid_maker(x):
    col=[]
    grid=[]
    for i in range(x):
        col.append('_')
    for i in range(x):
        grid.append(col)
    return(grid)



#function to generate a list of correct places
def index_gen(grid,word,z):
    index_list=[]
    lists=[]
    l=len(word)
    c=True
    if z==1:
        for i in range(len(grid)):
            for j in range(len(grid)-l+1):
                lists.clear()
                if grid[i][j]=='_':
                    c=True
                    for x in range(l):
                        if grid[i][j+x]!='_':
                            c=False
                            break

                    if c==True:
                        lists=[i,j]
                        index_list.append(lists.copy())                        
                else:
                    continue
    elif z==2:
        for i in range(len(grid)):
            for j in range(len(grid)-l+1):
                lists.clear()
                if grid[j][i]=='_':
                    c=True
                    for x in range(l):
                        if grid[j+x][i]!='_':
                            c=False
                            break

                    if c==True:
                        lists=[j,i]
                        index_list.append(lists.copy())                        
                else:
                    continue
    return (index_list)


#function to print the grid
def display_grid(grid):
    for x in grid:
        print(x)



#function to finally place all the chosen words
#to the correct places
def word_place(grid1, word_list):
    z=0
    w=''
    word=[]    
    index_list=[]
    index=[]
    while word_list!=[]:
        l, i = (0,0)
        for a in word_list:
            if len(a)>=l:
                l=len(a)
                word=list(a)
                w=a
        z=random.randint(1,2)
        index_list.clear()
        index_list=index_gen(grid,word,z)
        while index_list==[]:
            x=random.randint(1,2)
            index_list=index_gen(grid,word,x)
        index.clear()
        index=random.choice(index_list).copy()
        print(grid1)
        if z==1:
            for a in word:
                te = index[0]
                grid1[te][(index[1])+(i)]=a
                i+=1
        elif z==2:
            for a in word:            
                grid1[index[0]+i][index[1]]=a
                print(grid1)
                i+=1
        word_list.remove(w)
    return(grid1)

x=int(input("Enter the size of the grid: "))
grid=grid_maker(x)

f=open("EnglishWords.txt",'r').read()
f1=f.split('\n')
for a in range(len(f1)):
    if len(f1[a])>x:
        f1[a]=''
f1.remove('')
f2=[]
for a in f1:
    if a!='':
        f2.append(a)
display_grid(grid)
print("\n\n\n\n")
word_list=[]
for x in range(2):
    word_list.append(random.choice(f2))
print(word_list)
print("\n\n\n\n")
grid=word_place(grid,word_list)
display_grid(grid)