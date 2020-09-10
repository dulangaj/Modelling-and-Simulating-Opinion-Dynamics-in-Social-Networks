#   random modifications to matrices just for fun


#==== making first person strong-minded
def strongfirst(n, weight_matrix, strength):
    for j in range(n):
        weight_matrix[0][j] = (1-strength) / (n - 1)

    weight_matrix[0][0] = strength

    print("\n>> Successfully made the first person strong!\nNew Weight Matrix:\n", weight_matrix)

    return weight_matrix

def strongsecond(n, weight_matrix, strength):
    weight_matrix[1][0] = 1-strength
    weight_matrix[1][1] = strength

    print("\n>> Successfully made the second person strong!\nNew Weight Matrix:\n", weight_matrix)

    return weight_matrix


