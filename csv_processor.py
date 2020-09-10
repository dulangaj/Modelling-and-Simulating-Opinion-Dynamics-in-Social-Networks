# -- reads edge data from file in FROM TO form

import numpy
import visualize

# == Getting data from file

input_file = "input_stanford.csv"
output_file = "output"

try:
    f_input_matrix = open(input_file)
    print('Opened file')
except IOError as e:
    print ('unable to open the file')

#checks for disconnected edges
def disconnection_checker(matrix):

    #power matrix to 5. rows that add upto 0 have no friends
    matrix_pow = numpy.linalg.matrix_power(matrix,5)
    matrix_tot = matrix_pow.sum(axis=1)

    counter = 0
    for sumno in matrix_tot:
        if(sumno==0):
            numpy.delete(matrix,counter)
            print("deleted row ",counter+1)
        counter = counter+1

    return matrix

#main function to process matrix
def create_matrix():
    print('Processing matrix')
    listofedges = []

    for line in f_input_matrix:
        edge_data = line.split()

        this_edge = int(edge_data[0]),int(edge_data[1])
        listofedges.append(this_edge)

    second_person_list = []

    for edge in listofedges:
        rubbish, this = edge
        second_person_list.append(this)

    no_of_nodes = max(second_person_list)

    print("The matrix in the chosen file contains ",no_of_nodes," nodes.")

    # == Making matrix
    matrix = numpy.zeros((int(no_of_nodes), int(no_of_nodes))) # create empty matrix

    #add edges from list
    for edge in listofedges:
        edgefrom, edgeto = edge
        matrix[edgefrom-1][edgeto-1]=1

    #mirror
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i] = matrix[i][j]

    matrix = disconnection_checker(matrix)

    print("\nProcessed Network Matrix with \n",matrix)

    return (matrix)