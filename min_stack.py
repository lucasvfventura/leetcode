class MinStack(object):

    def __init__(self):
        self.values = []
        self.mins = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.values.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        elif self.mins[-1] >= val:
            self.mins.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        value = self.values.pop()
        if value == self.mins[-1]:
            self.mins.pop()

        return value

    def top(self):
        """
        :rtype: int
        """
        if len(self.values) > 0:
            return self.values[-1]
        
        return 0

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.mins) > 0:
            return self.mins[-1]
        
        return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()