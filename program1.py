class Solution(object):
    def__init__(self):
        self.stack = []
        self.mapping = { ')' : '(' , '}': '{', ']':'['}
        def isValid(self, s):
            " " "
            :type s: str
            :rtype:bool
            " " "
            self.stack = []
            for char in s:
                if char in self.mapping:
                top_element = self.stack.pop()
                 if self.stack  else '#' if self.mapping[char] != top_element:
                    return False
                    else:
                        self.stack.append(char)
                        return not self.stack
   
    



  

