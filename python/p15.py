dim=200
world = [[0 for i in range(dim+1)] for j in range(dim+1)]
for i in range(dim+1):
    world[dim][i]=1
    world[i][dim]=1
for i in range(dim,-1,-1):
    for j in range (dim-1,-1,-1):
        if i!=dim:
            world[j][i]=world[j+1][i]+world[j][i+1]
#print(world)
print(world[0][0])

