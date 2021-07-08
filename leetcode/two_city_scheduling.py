'''
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.



Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086

Solution:
sort the given cost array in ascending order based on difference between A-B
(i.e. cost of sending person to city A - cost of sending person to city B, cost[i][0] - cost[i][1])
loop throught the given costs array and for first half of the list send the persons to city A and rest to city B
'''

def twoCityScheduling(costs: list):
    sorted_costs = sorted(costs, key=lambda x: x[0]-x[1])
    print(sorted_costs)
    result = 0
    for i in range(len(costs)):
        if i < len(costs)/2:
            result += sorted_costs[i][0]
        else:
            result += sorted_costs[i][1]
    return result

print(twoCityScheduling([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
