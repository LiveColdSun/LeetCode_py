class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longestlength = 0
        stemp = ''
        for item in s:
        	if item not in stemp:
        		stemp += item	
        	else:
        		if longestlength < len(stemp):
        			longestlength = len(stemp)
        		stemp = stemp[stemp.find(item)+1:]+item	
        if longestlength < len(stemp):
        	longestlength = len(stemp)
       	return longestlength
