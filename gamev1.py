f = open("last_game_score_data.txt", "r").read()
f1 = open("last_game_name_data.txt","r").read()
lists1=f.split().copy()
lists2=f1.split().copy()
lists3=[]
print(lists1)
print(lists2)
lists3=lists2.copy()
for j in range(len(lists1)+1):
    for i in range(len(lists1)-1):
        lists2=lists3.copy()
        if float(lists1[i])<float(lists1[i+1]):
            lists1[i]=str(float(lists1[i])+float(lists1[i+1]))
            (lists1[i+1])=str(float(lists1[i])-float(lists1[i+1]))
            (lists1[i])=str(float(lists1[i])-float(lists1[i+1]))
            lists3[i]=lists2[i+1]
            lists3[i+1]=lists2[i]
print(lists1)
print(lists3)
