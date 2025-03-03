def reverse_list(lst):
    result = []

    # start stop step
    for i in range(len(lst)-1, 0 ,-1):
        result.append(lst[i])

    print(result)

    return result

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)

