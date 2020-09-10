#   Code for DeGroot model  -- takes weight and opinion matrices, and outputs conversation results and self-appraisal
#            -- main class is the last one, self_app

import numpy
import visualize
import make_matrix
import scipy.linalg as la
import tweaks



visualization = 0
visualize_rate = 10 #draw graph every x conversations; go to mod_degroot.py to turn on/off

#====calculates time taken to reach consensus ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def timetoconsensus(opinion_matrix):
    i=0
    first_val = str(round(opinion_matrix[0], 3))
    for item in opinion_matrix:
        this_val = str(round(item, 3))

        if(this_val!=first_val):       # if this has NOT reached consensus
            return 0
    return 1                            # if this has reached consensus

#====calculate opinion after t conversations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def opinion(n, matrix_network, matrix_weight, matrix_opinion_original, convo_per_issue):
    consensus = 0

    matrix_opinion_new = matrix_opinion_original

    visualize.network_opinion_colors(matrix_network, matrix_opinion_new)

    #visualize.network_opinion_colors(n, matrix_network, matrix_opinion_new)

    i = 1
    while (convo_per_issue>0):
        matrix_opinion_new = numpy.dot(matrix_weight, matrix_opinion_new)
        #print("\n>> Opinion Matrix number ",i,":\n",matrix_opinion_new)
        convo_per_issue-=1

        consensus = timetoconsensus(matrix_opinion_new)

        if(consensus==1):
            visualize.network_opinion_colors(matrix_network, matrix_opinion_new)
            return matrix_opinion_new, i
            break

        if(visualization==1):
            if(i==1 or i%visualize_rate==0):
                print("Visualization after",i,'conversations')
                visualize.network_opinion_colors(matrix_network, matrix_opinion_new)
        i += 1
    #print("New opinion:\n",matrix_opinion_new)
    print("\nDid NOT reach consensus")
    return matrix_opinion_new, i


#=== calculate OPINIONS and SELF-Appraisal ====
def self_app(n, matrix_network, mat_weight, n_issues, convo_per_issue):
    time_to_consensus = []

    print("\nRunning DeGroot self-appraisal on", n_issues, "issues...")

    for i in range(n_issues):
        print("Running issue number ", i+1)

        # 1 get opinion on issue i+1 after convo_per_issue
        mat_opinion_ori = make_matrix.opinion(n)
        mat_opinion_final, this_time_to_consensus = opinion(n, matrix_network, mat_weight, mat_opinion_ori, convo_per_issue)

        if(this_time_to_consensus-1!=convo_per_issue):
            print("\nConsensus after", this_time_to_consensus,"discussions for issue",i+1)

        time_to_consensus.append(this_time_to_consensus)
        #print("\nFinal Opinions for this issue: \n",mat_opinion_final)

        # ===== 2 Self appraisal
        #get eigen vals and vector matrix
        transpose = numpy.transpose(mat_weight)
        e_vals, e_vecs = la.eig(transpose)

        #finding top eigen value
        list_e_vals = []
        for values in e_vals:
            list_e_vals.append(values)

        position_of_top_right = list_e_vals.index(max(list_e_vals))

        eigen_vector = []


        for row in e_vecs:
            eigen_vector.append(row[position_of_top_right])

        #print("\nAll eigen vals",e_vals)
        #print("\n","Top eigen_value",e_vals[position_of_top_right],"\nTop right eigen vector",eigen_vector)

        #get self-weight

        diag_ys = numpy.diag(eigen_vector)
        xxx = numpy.dot((numpy.identity(n) - diag_ys) , (mat_weight))
        mat_weight_new = diag_ys + xxx
        #mat_weight = mat_weight_new

        print("Weightings at end of issue",i+1,":\n", mat_weight)


    print("\nFinal weight matrix:\n", mat_weight)

    #print("\nAverage DeGroot time to consensus",sum(time_to_consensus)/n_issues)
    #print("Degroot",time_to_consensus)




    return mat_weight


