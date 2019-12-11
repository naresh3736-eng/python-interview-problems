def subsets(alist):
    result = [[]]
    for i in xrange(len(alist)+1):
        for j in xrange(i+1, len(alist)+1):
            subset = alist[i:j]
            result.append(subset)
    return result

print subsets([1,2,3])