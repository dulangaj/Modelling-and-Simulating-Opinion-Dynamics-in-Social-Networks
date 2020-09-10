#   takes in number of nodes and outputs opinion and weigh matrices

import numpy
import random

#====   create a column matrix x with OPINIONS for each person
def opinion(n):
    matrix = numpy.zeros((int(n)))

    for i in range(len(matrix)):
        matrix[i] = random.random()

    matrix = matrix.transpose()

    #print("\nInitial Opinions for this issue:\n",matrix)

    return matrix


#====   creating WEIGHT matrix - count degree, equal weight for all
def weight(n, network_matrix):
    n = int(n)
    weight_matrix = numpy.zeros((int(n),int(n)))

    #---COUNTING DEGREE per row ---the degree counted includes self!
    degree_array = [1]*n

    for i in range(n):
        for j in range(n):
            if(network_matrix[i][j]>0):
                degree_array[i]+=1

    #print("Array with degrees of each node: ", degree_array)

    #---calculating equal weight
    weight_array = [0]*n

    for i in range(n):
        weight_array[i]=1/degree_array[i]


    #=======adding weight to matrix
    for i in range(n):
        for j in range(n):
            if(network_matrix[i][j]>0):
                weight_matrix[i][j]=weight_array[i]
        weight_matrix[i][i] = weight_array[i]


    print("\n>> Successfully created Weight Matrix:\n",weight_matrix)


    return weight_matrix


def weightfor_star(n):      #this enables special attributes to be added to the weight matrix for a star
    weight_matrix = numpy.zeros((int(n),int(n)))

    for i in range(n):
        for j in range(n):
            if(j==0 or j==i):
                weight_matrix[i][j]=1/2

    for j in range(n):
        weight_matrix[0][j] = 1/n

    print("\n>> Successfully created Weight Matrix:\n",weight_matrix)

    return weight_matrix