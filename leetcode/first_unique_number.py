'''
You have a queue of integers, you need to retrive the first unique integer in the queue
Implement the FirstUnique class:
FirstUnique(int[] nums) initlaizes the object with the numbers in the queue.
int showFirstUnique() return the value of the first unique integer of the queeu and return -1 if there is no such integer
void add(int value) add value to the queue
Input: ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique". "add", "showFirstUnique"]
       [[[2,3,5]], [], [5], [], [2], [], [3]. []]
Output: [null, 2, null, 2, null, 3, null, -1
Explanation:
FirstUnique firstUniuqe = new firstUniuqe([2,3,5])
firstUnique.showFirstUnique();  // return 2
firstUnique.add(5); //the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); //return 2
firstUnique.add(2); //  the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3); // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique() // return -1
'''

class FirstUnique:
    def __init__(self, nums: list):
        self.q = []
        self.dict = {}
        for i in nums:
            self.add(i)

    def add(self, value: int) -> None:
        if value in self.dict:
            self.dict[value] += 1
        else:
            self.dict[value] = 1
            self.q.append(value)

    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.dict[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]
