'''
Input:  Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}
             start = TOON
             target = PLEA
Output: 7
Explanation: TOON - POON - POIN - POIE - PLIE - PLEE - PLEA
'''

'''
The idea is to use BFS. We start from the given start word, traverse all words that adjacent (differ by one character) to it and keep doing so until we find the target word or we have traversed all words.
'''

class QItem():
    def __init__(self, word, len):
        self.word = word
        self.len = len


def isAdjacent(a, b):
    count = 0
    n = len(a)

    for i in range(n):
        if a[i] != b[i]:
            count += 1

        if count > 1:
            break

    return True if count == 1 else False

def shortestChainLen(start, target, L):
    queue = []
    item = QItem(start, 1)
    queue.append(item)

    while len(queue) > 0:
        curr = queue.pop()

        for word in L:
            temp = word

            if isAdjacent(curr.word, temp):
                item.word = temp
                item.len = curr.len + 1
                queue.append(item)

                L.remove(temp)

                if temp == target:
                    return item.len


D = []
D.append("poon")
D.append("plee")
D.append("same")
D.append("poie")
D.append("plie")
D.append("poin")
D.append("plea")
start = "toon"
target = "plea"
print "Length of shortest chain is: %d"% shortestChainLen(start, target, D)



