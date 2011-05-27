import io

# Problem 18/67
dim=100
file = io.open("triangle.txt","r")
# Load file to array
world = [[0 for i in range(dim)] for j in range(dim)]
for i in range(dim):
    #print(i)
    l = (file.readline()).split()
    for j in range(i+1):
        #print(j)
        world[i][j]=l[j]
        
# Next 3 lines solve the actual problem..
for i in range(dim-2,-1,-1):
    for j in range(i+1):
        world[i][j]=int(world[i][j])+max(int(world[i+1][j]),int(world[i+1][j+1]))

# Print answer
print(world[0][0])
