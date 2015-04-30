class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        tmp = []
        for item in s:
            if item in ('(', '[', '{'):
                tmp.append(item)
            elif item == ')':
                if len(tmp) > 0 and tmp[-1] == '(':
                    tmp.pop()
                else:
                    return False
            elif item == ']':
                if len(tmp) > 0 and tmp[-1] == '[':
                    tmp.pop()
                else:
                    return False
            else:
                if len(tmp) > 0 and tmp[-1] == '{':
                    tmp.pop()
                else:
                    return False
        return len(tmp) == 0
