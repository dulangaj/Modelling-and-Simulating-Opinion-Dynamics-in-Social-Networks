#   Code for bounded confidence model; takes in weight matrix and simulates issues -- main class is the last one

import numpy
import visualize
import make_matrix
import math
import random

bound = 1 # opinions more different than this will be rejected!
affectivity = 7 #for self-appraisal -- change in opinion is multiplied for effect on person

#calculate time taken to reach consensus
def timetoconsensus(opinion_matrix):    #calculates time taken to reach consensus
    i=0
    first_val = str(round(opinion_matrix[0], 3))
    for item in opinion_matrix:
        this_val = str(round(item, 3))

        if(this_val!=first_val):       # if this has NOT reached consensus
            return 0
    return 1                            # if this has reached consensus

# calculate opinion after t conversations
def opinion(n, matrix_weight, matrix_opinion, convo_per_issue, self_weights):

    matrix_opinion_new = matrix_opinion
    #consensus = 0

    for x in range(convo_per_issue): #to repeat process

        for i in range(n):  #check change in opinion for each node
            total_change = 0
            for j in range(n):
                if(matrix_weight[i][j]>0):  #increase efficiency
                    if(abs(matrix_opinion[i]-matrix_opinion[j])<bound):
                        total_change = total_change + matrix_weight[i][j]*(matrix_opinion[j]-matrix_opinion[i])

            #print(matrix_opinion[i],total_change)
            matrix_opinion_new[i] = matrix_opinion_new[i] + ( (1-self_weights[i]) * total_change )

        #consensus = timetoconsensus(matrix_opinion_new)

        #print(matrix_opinion)

        #if (consensus == 1):    #ONLY useful if bound==1
            #print("consensus reached after",x)
        #    return matrix_opinion_new, x
        #    break

    return matrix_opinion_new, x


def self_app(n, matrix_network, matrix_weight, n_issues, convo_per_issue):
    self_weights = [0.5] * n
    #self_weights[0] = 1
    #time_to_consensus=[]

    print("\nRunning non-linear self-appraisal on", n_issues, "issues...")

    for issue in range(n_issues): #going through each issue
        print("\nRunning issue number", issue+1)
        matrix_opinion = make_matrix.opinion(n)
        original_opinion = list(matrix_opinion)     # because this tends to get modified
        matrix_opinion_new, this_timetoconsensus = opinion(n, matrix_weight, matrix_opinion, convo_per_issue, self_weights)
        #print(matrix_opinion_new)
        final_opinion = list(matrix_opinion_new)    #because this tends to get modified
        #time_to_consensus.append(this_timetoconsensus) #number of discussions, if bound < 1


        for x in range(n):
            self_weights[x] = math.exp(-affectivity*abs(original_opinion[x]-final_opinion[x]))


    degree_array = [0] * n
    for i in range(n):
        for j in range(n):
            if (matrix_network[i][j] > 0):
                degree_array[i] += 1

    print(degree_array)
    print(self_weights)

    #visualize.scatterplotthis(original_opinion, self_weights)

    #visualize.network_opinion_colors(matrix_network, matrix_opinion_new)    #visualize opinions after discussion

    return self_weights