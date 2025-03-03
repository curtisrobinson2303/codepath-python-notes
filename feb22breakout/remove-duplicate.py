def remove_dupes(items):
    seen = []

    for ele in items:
        if ele not in seen: 
            seen.append(ele)
            
    print(seen)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)