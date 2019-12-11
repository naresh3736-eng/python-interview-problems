# O(n^2) apporach

def largest_area_n2(histograms):
    max_area = 0

    for i in range(len(histograms)):
        min_height = histograms[i]

        for j in range(i, len(histograms)):
            min_height = min(min_height, histograms[j])
            max_area = max(max_area, min_height * ((j-i) + 1))

    return max_area


def largest_area_efficient(histograms):
    max_area = 0
    index = 0
    stack = list()

    while index < len(histograms):
        if not stack or histograms[index] >= histograms[stack[-1]]:
            stack.append(index)
            index += 1

        else:
            top_of_stack = stack.pop()
            area = (histograms[top_of_stack] * (index - stack[-1] -1) if stack else index)
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (histograms[top_of_stack] * (index - stack[-1] -1) if stack else index)
        max_area = max(max_area, area)

    return max_area


hist = [6, 2, 5, 4, 5, 1, 6]
print("n2 solution ", largest_area_n2(hist))
print("Maximum area is ",  largest_area_efficient(hist))