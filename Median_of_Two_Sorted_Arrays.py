class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
    	if len(A)==0 and len(B)!=0:
    		return B[len(B)/2] if len(B)%2!=0 else (B[len(B)/2-1]+B[len(B)/2])/2.0
    	if len(B)==0 and len(A)!=0:
    		return A[len(A)/2] if len(A)%2!=0 else (A[len(A)/2-1]+A[len(A)/2])/2.0
    	if len(A)+len(B)==0:
    		return None

        k = (len(A)+len(B)+1)/2
        numofFirstPart = 0 # to store the num of first(smaller) part
        needtwoMedian = False
        if (len(A)+len(B)) %2 == 0 :
        	needtwoMedian = True # means that we need to get the meddle 2 nums to cal the median
        
        while (k-numofFirstPart)/2-1 >= 0 :
        	indexA = (k-numofFirstPart)/2-1 if len(A)>=(k-numofFirstPart)/2 else len(A)-1
        	indexB = (k-numofFirstPart)/2-1 if len(B)>=(k-numofFirstPart)/2 else len(B)-1

        	if A[indexA] < B[indexB]:
        		numofFirstPart += indexA + 1
        		if indexA != len(A)-1:
        			A = A[indexA+1:]
        		else :
        			A = []
        			return  (B[k-numofFirstPart]+B[k-numofFirstPart-1])/2.0 if needtwoMedian else B[k-numofFirstPart-1]
        	else :
        		numofFirstPart += indexB + 1
        		if indexB != len(B)-1:
        			B = B[indexB+1:]
        		else:
        			B = []
        			return  (A[k-numofFirstPart]+A[k-numofFirstPart-1])/2.0 if needtwoMedian else A[k-numofFirstPart-1]

        if not needtwoMedian:
        	return A[0] if A[0]<B[0] else B[0]
        else :
        	temp = (A[0]+B[0]) /2.0
        	if len(A)>1 :
        		if (A[0]+A[1])/2.0<temp:
        			temp = (A[0]+A[1])/2.0
        	if len(B)>1 :
        		if (B[0]+B[1])/2.0<temp:
        			temp = (B[0]+B[1])/2.0
        	return temp
