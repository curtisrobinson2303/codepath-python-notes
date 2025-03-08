# I
# O
# C
# E -


def is_authentic_collection(art_pieces):
    sortedList = sorted(art_pieces)
    print(sortedList)

    if sortedList[0] == 1 and sortedList[1] == 1 and len(sortedList) == 2:
        return True

    if (
        sortedList[len(sortedList) - 1] == len(sortedList) - 1
        and sortedList[len(sortedList) - 2] == len(sortedList) - 1
    ):
        for i in range(0, len(sortedList) - 2):
            if sortedList[i] != i + 1:
                return False
        return True
    return False


collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
