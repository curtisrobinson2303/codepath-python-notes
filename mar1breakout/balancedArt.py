# I - art_pieces this is a array/list
# O - longest balanced subsequence thats int
# C - storing the frequency of each element
# E - length is 1


# A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.


def find_balanced_subsequence(art_pieces):

    dict = {}

    for ele in art_pieces:
        if ele in dict:
            dict[ele] += 1
        else:
            dict[ele] = 1

    print(dict)

    bestlen = 0

    for element1, val1 in dict.items():
        for element2, val2 in dict.items():
            if element1 - element2 == 1 or element1 - element2 == -1:
                if val1 + val2 > bestlen:
                    bestlen = val1 + val2

    return bestlen


# solve for the differneces = to 1

# count the number of each int with a dictionary

# then use the


art_pieces1 = [1, 3, 2, 2, 5, 2, 3, 7]
art_pieces2 = [1, 2, 3, 4]
art_pieces3 = [1, 1, 1, 1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))
