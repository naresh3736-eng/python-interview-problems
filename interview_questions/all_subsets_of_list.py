def subsets(alist):
    result = []
    for i in range(len(alist)+1):
        for j in range(i+1, len(alist)+1):
            subset = alist[i:j]
            result.append(subset)
    return result

print(subsets([1,2,3]))