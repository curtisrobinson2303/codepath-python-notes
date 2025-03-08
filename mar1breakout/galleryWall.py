from collections import Counter


def organize_exhibition(collection):
    # Count occurrences of each element
    freq = Counter(collection)

    # Number of rows required is determined by the max frequency of any element
    num_rows = max(freq.values())

    # Initialize empty rows
    result = [[] for _ in range(num_rows)]

    # Distribute elements across rows
    for item, count in freq.items():
        for i in range(count):
            result[i].append(item)

    return result


collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))
