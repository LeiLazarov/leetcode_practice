class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ""
        
        for c in s:
            if c.isdigit():
                curNum = curNum*10 + int(c)
            elif c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                preString = stack.pop()
                curString = preString + num*curString
            else:
                curString += c
        return curString