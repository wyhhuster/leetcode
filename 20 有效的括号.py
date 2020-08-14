class Solution(object):
    #太太太长
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            if s[i]==')':
                if stack:
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if s[i]==']':
                if stack:
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if s[i]=='}':
                if stack:
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not stack
    #简化一楼
    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        d={'(':')','{':'}','[':']'}
        for char in s:
            if char in d:
                stack.append(char)
            else:
                if not stack or d[stack.pop()]!=char:
                    return False
        return not stack
    #评论区大佬
    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i=='(':
                stack.append(')')
            elif i=='[':
                stack.append(']')
            elif i=='{':
                stack.append('}')
            elif not stack or i!=stack.pop():
                return False
        return not stack
    def isValid3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
A=Solution()
print(A.isValid('([)]'))