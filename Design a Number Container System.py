"""Design a number container system that can do the following:
Insert or Replace a number at the given index in the system.
Return the smallest index for the given number in the system.
Implement the NumberContainers class:
NumberContainers() Initializes the number container system.
void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.

Example 1:

Input
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output
[null, -1, null, null, null, null, 1, null, 2]"""

class NumberContainers(object):
    def __init__(self):
        self.mp={}
        self.idx={}
    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        self.idx[index]=number
        if number not in self.mp:
            self.mp[number]=[]
        heapq.heappush(self.mp[number],index)
    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.mp:
            return -1
        while self.mp[number]:
            min_index=self.mp[number][0]
            if self.idx[min_index]==number:
                return min_index
            heapq.heappop(self.mp[number])
        return -1


        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)