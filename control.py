import numpy as np

desired_width = 320     # change this value to get python to fit code to your display
np.set_printoptions(linewidth=desired_width)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)}) #to stop NumPy displaying large digits

import make_network     #importing other python files from within this project
import make_matrix
import mod_degroot
import tweaks
import mod_bounded_conf
import visualize
import csv_processor


# ~~~~~ CONTROL VARIABLES ~~~~~~~
convo_per_issue= 2000
n_issues=7

#============  !!! 1. create NETWORK
type_of_network= 3  # 1-line    2-ring  3-star  4-random    5-stochastic blocks    6-doubly stoch
n_people = 50
matrix_network = make_network.create(n_people, type_of_network)
#n_people, matrix_network = csv_processor.create_matrix()   #use IMPORTED network

#============ drawing network [VISUALIZE]
#visualize.network(matrix_network)

#============  !!! 2. making WEIGHT Matrix
matrix_weight = make_matrix.weight(n_people, matrix_network)
#matrix_weight = make_matrix.weightfor_star(n_people) #for special star

#   3.2 TWEAKS
#strength_of_peep = 0.9
#matrix_weight = tweaks.strongfirst(n_people, matrix_weight, strength_of_peep)    #to make first person strong
#matrix_weight = tweaks.strongsecond(n_people, matrix_weight, strength_of_peep)    #to make first person strong
#matrix_opinion_original[0] = 0.9   #to make first person's opinion a certain value

#=========== 3 BOUNDED CONFIDENCE
#matrix_opinion_new = mod_bounded_conf.self_app(n_people, matrix_weight, n_issues, convo_per_issue)
#self_weights = mod_bounded_conf.self_app(n_people, matrix_network, matrix_weight,n_issues,convo_per_issue)

#=========== 4 DEGROOT
#============  !!! 3.X. Running several issues and SELF-Appraisal (SKIP 3)
matrix_opinion_new = mod_degroot.self_app(n_people, matrix_network, matrix_weight, n_issues, convo_per_issue)

#   3.1 OPTIONAL to run one ONE issue (unnecessary)
#matrix_opinion_original = make_matrix.opinion(n_people)


#   3.3 OPTIONAL to calculate ratios of values. Disable 3 [VISUALIZE]
visualize.network(matrix_network)




