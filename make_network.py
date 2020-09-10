#   Takes the number of required nodes, and outputs a graph of 1 of 5 types

import random
import sys
import numpy
import visualize


# =================  MAIN ----- asking for number of nodes for control_main.py   =================
def ask_graph_type(n):
    n = int(n)
    #=======creating network
    while(1>0):
        graphtype = input("\n>>What kind of graph? \n"
                          "1= line 2= ring  3= star 4= random 5= stochastic block model     ")

        if graphtype == "1":
            print("\n>>Creating a line graph with ",n," people...\n")
            matrix = make_linegraph(n)
            break

        elif graphtype == "2":
            print("\n>>Creating a ring graph with ",n," people...\n")
            matrix = make_ringgraph(n)
            break

        elif graphtype == "3":
            print("\n>>Creating star graph with ",n," people...\n")
            matrix = make_stargraph(n)
            break

        elif graphtype == "4":
            print("\n>>Creating a random graph with ",n," people...\n")
            matrix = make_randomgraph(n)
            break

        elif graphtype == "5":
            print("\n>>Creating a stochastic block model graph with ",n," people...")
            matrix = make_stochasticgraph(n)
            break

        else:
            print("\nInvalid input!\nPlease enter a number between 1 and 5.")


    print(">> Successfully created Network Adjacency Matrix:\n",matrix)

    return matrix

#========= create graph for control.py
def create(n, graphtype):
    n = int(n)
    #graphtype = int(graphtype)


    if graphtype == 1:
        print("\n>>Creating a line graph with ", n, " people...\n")
        matrix = make_linegraph(n)

    elif graphtype == 2:
        print("\n>>Creating a ring graph with ", n, " people...\n")
        matrix = make_ringgraph(n)

    elif graphtype == 3:
        print("\n>>Creating star graph with ", n, " people...\n")
        matrix = make_stargraph(n)

    elif graphtype == 4:
        print("\n>>Creating a random graph with ", n, " people...\n")
        matrix = make_randomgraph(n)

    elif graphtype == 5:
        print("\n>>Creating a stochastic block model graph with ", n, " people...\n")
        matrix = make_stochasticgraph(n)

    elif graphtype == 6:
        print("\n>>Creating a doubly stochastic graph with ", n, " people...\n")
        matrix = make_doublystochastic(n)

    else:
        print("\nInvalid input for network type! Terminating program.")
        sys.exit()


    print(">> Successfully created Network Adjacency Matrix:\n",matrix)

    return matrix

#============== Checks if graph is disconnected
def disconnection_checker(matrix):

    #power matrix to 5. rows that add upto 0 have no friends
    matrix_pow = numpy.linalg.matrix_power(matrix,5)
    matrix_tot = matrix_pow.sum(axis=1)

    #print(matrix_tot)

    counter = 0
    for sumno in matrix_tot:
        if(sumno<10):
            return 1

    return 0

#================   Creating MATRICES     ========================

#----------      LINE graph (Binary)
def make_linegraph(n):

    #------NETWORK
    #draw matrix with 1 along 1st diagonal
    # -> this creates a directed graph
    matrix = numpy.eye(int(n), k=1)

    #reflect along diagonal to make graph undirected
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i] = matrix[i][j]

    return matrix


#----------      RING graph (Boolean/BINARY??) - like line, but connected at ends
def make_ringgraph(n):

    #create line graph
    matrix = numpy.eye(int(n), k=1)

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i] = matrix[i][j]


    #join ends by conecting first and last nodes
    matrix[int(n)-1,0] = 1
    matrix[0,int(n)-1] = 1

    return matrix

#----------      STAR graph (Binary) ---- one node in the center connected to n-1 nodes
def make_stargraph(n):
    #create zero matrix
    matrix = numpy.zeros((int(n), int(n)))

    #add ones
    matrix[0, ] = 1
    matrix[0, 0] = 0

    #mirror
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i] = matrix[i][j]

    return matrix


#----------      RAND graph (Binary) --- n nodes connected with each other with 1.1 log(n)/n
def make_randomgraph(n):

    # assign edges with probability 1.1 log(n)/n
    p = (1.1 * (numpy.log(n))) / n

    matrix_is_connected = False

    while(matrix_is_connected==False):  #remake graph until connected
        # create zero matrix
        matrix = numpy.zeros((int(n), int(n)))

        # add values to top triangle, avoiding diagonal
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                ram = random.random()
                if (ram < p):
                    matrix[j][i] = 1

        # reflect, avoiding diagonal
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j] = matrix[j][i]

        connected_vertices = 0

        if(disconnection_checker(matrix)==0):
            return matrix
            break
        else:
            print(".. Generated graph is not connected. Trying again...")

    return matrix


#----------      STOCHASTIC Block graph (Binary) --- n nodes connected with each other with 1.1 log(n)/n
def make_stochasticgraph(n):
    graph_is_disconnected = 1
    while(graph_is_disconnected==1):
        # connection probabilities
        p_inblock = (4 * (numpy.log(n))) / n #within block
        p_exblock = p_inblock/12 #outside block


        n = int(n)

        # create empty FULL matrix
        matrix = numpy.zeros((int(n), int(n)))

        #calculating number of blocks according to number of people
        if n<10:
            blocks = 1
        elif n<20:
            blocks=2
        elif n<100:
            blocks=3
        elif n<500:
            blocks = 6
        elif n<1000:
            blocks = 20
        else:
            blocks = n/50
        #print("Number of blocks:",blocks)

        #calculating block size
        blocksize = int(n/blocks)
        leftover_nodes = n%blocks
        #print ("Number of nodes in a block:",blocksize,"  (with",leftover_nodes,"extra nodes in first block)")

        print("...graph will have",blocks,"block(s), with approximately",blocksize,"people in each.\n")

        blocklengtharray = [0]*blocks #array containing number of people by block
        for x in range(blocks):
            blocklengtharray[x]= blocksize
        blocklengtharray[0] = blocksize + leftover_nodes

        #creating network
        triangle=blocklengtharray[0]
        blocklengtharray.pop(0)

        for i in range (n):
            #connections within block
            for j in range (i+1, i+triangle):
                ram = random.random()
                if (ram < p_inblock):
                    matrix[i][j]=1
            triangle-=1

            #connections outside block
            for j in range (i+1+triangle,n):
                ram = random.random()
                if (ram < p_exblock):
                    matrix[i][j] = 1

            #to move onto next block
            if (triangle==0):
                if(blocklengtharray==[]):
                    continue
                triangle=blocklengtharray[0]
                blocklengtharray.pop(0)


        # reflect, avoiding diagonal
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[j][i] = matrix[i][j]

        graph_is_disconnected = disconnection_checker(matrix)

    return matrix

def make_doublystochastic(n):
    #create zero matrix
    matrix = numpy.ones((int(n), int(n)))

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if(i==j):
                matrix[i][j] = 0

    return matrix



#==========================     NOTES       ===================

#to add opinions: make each node a dictionary
#to add trust weightings: change values from binary to probability
