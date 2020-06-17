import sys

# Input is read in from a file specified in the command line at run time.
with open(sys.argv[1], 'r') as inFile:
    
    # The file contains the number of wrestlers, n
    n = int(inFile.readline().rstrip())

    graphOfWrestlers = {}
    listOfWrestlers = []
    
    #  followed by their names
    for i in range(n):
        line = inFile.readline().rstrip().split(" ")
        graphOfWrestlers[line[0]] = []
        listOfWrestlers.append(line[0])
        
    #  the number of rivalries r
    r = int(inFile.readline().rstrip())
    
    for i in range(r):
        line = inFile.readline().rstrip().split(" ")

        #  rivalries listed in pairs
        graphOfWrestlers[line[0]].append(line[1]) #these lines build an adjacency matrix
        graphOfWrestlers[line[1]].append(line[0])



babyfaces = []
#  For consistency assign the first wrestler in the list to be a Babyface.
babyfaces.append(listOfWrestlers[0])
heels = []

possible = True

# for every vertex, it's adjacent vertices are examined, if they are compatible,
# add them to the appropriate collection
for i in listOfWrestlers:
    for e in graphOfWrestlers[i]:

                
        if ((i not in babyfaces ) and (i not in heels)):
            if (e in babyfaces):
                heels.append(i)
            elif (e in heels):
                babyfaces.append(i) 
            else:
                babyfaces.append(i)
                heels.append(e)



        elif (i in babyfaces):
            if(e in babyfaces):
                possible = False
            if(e in heels):
                continue
            else:
                heels.append(e)
        
        elif (i in heels):
            if(e in heels):
                possible = False
            if(e in babyfaces):
                continue
            else:
                babyfaces.append(e)
        



if (possible == False):
    print('Impossible')
else:
    print('babyfaces: ')
    print (babyfaces)
    print ('heels: ')
    print (heels)


        
