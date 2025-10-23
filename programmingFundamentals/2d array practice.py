days = ['monday','tuesday','wednesday','thursday', 'friday']
name = [
    'barry smith',
    'florian wirtz',
    'jon smeth',
    'michael smoth',
    'josh smath',
    'tony smuth',
    'jason smuoth',
    'leo gallagher',
    'lenard richards',
    'garry neville']


scores = [
    [60,70,65,87,64],
    [99,99,99,99,99],
    [1,1,1,1,1],
    [12,21,60,21,12],
    [11,12,13,13,12],
    [0,0,0,0,0],
    [76,67,41,38,2],
    [78,90,89,77,0],
    [12,34,65,78,98],
    [45,42,23,65,87]
]

for i in range(len(scores)):
    print(name[i])
    for j in range(len(scores[0])):
        if j <4:
            print(str(scores[i][j]), end= " | ") 
        else:
            print(str(scores[i][j]))
    print('------------------------------------------')            
