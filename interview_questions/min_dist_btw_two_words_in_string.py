# function to calculate the minimum
# distance between w1 and w2 in s

def minDistance(s, w1, w2):
    if w1 == w2:
        return

    words = s.split(" ")
    minDist = len(words) + 1

    for index in range(len(words)):
        if words[index] == w1:
            for search in range(len(words)):
                if words[search] == w2:

                    curr = abs(index - search) -1

                    if curr < minDist:
                        minDist = curr

    return minDist


string = "geeks for geeks now practice"
w1 = "geeks"
w2 = "practice"

# print minDistance(string, w1, w2)


def minDistance_efficient(s, w1, w2):
    if w1 == w2:
        return 0

    words = s.split(" ")
    min_dist = len(words) + 1

    for i in range(len(words)):
        if words[i] == w1 or words[i] == w2:
            prev = i
            break

    i = 0

    while i < len(words):
        if words[i] == w1 or words[i] == w2:
            if words[prev] != words[i] and (i - prev) < min_dist:
                min_dist = i - prev - 1
                prev = i
            else:
                prev = i

        i += 1

    return min_dist

print minDistance_efficient(string, w1, w2)

