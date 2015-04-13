class Solution:
    # @return a string
    def convert(self, s, nRows):
        if s == '':
            return ''
        sr = ''
        length = len(s)
        if nRows == 1 or length <= nRows:
            return s
        for i in range(nRows):
            idx = i
            sr += s[idx]
            while True:
                if i != nRows-1:
                    idx += 2*(nRows-i-1)
                    if idx >= length:
                        break
                    sr += s[idx]
                if i != 0:
                    idx += 2*i
                    if idx >= length:
                        break
                    sr += s[idx]
        return sr
        