class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        
        """
            HIGH LEVEL:
                Brute Force:
                    - chek all possible combinations that sum up to zero
                    - have four nested loops to make up all combos
                    - update count if combinations sums up to zero.
                Time: O(n^4)
                Space: O(1)
                
                Optimized:
                    - have two nested loops:
                        - first nested loop creates all sum combos between A & B
                            - store those sum combos to a sumAB where key is sum and value is the number of times that sum occurs.
                            - second nested loop traverses through combos between C & D
                        - make a temp_sum and see if it's counterpart is in hashmapAB
                        - if it is, update count with frequencies of counterpart
        
        """
        
        count = 0
        # sumAB = {-1: 1, 0: 2, 1: 1}
        sumAB = {}
        
        # first aggregate sum combos between A and B
        for i in range(len(A)):
            for j in range(len(B)):
                total =  A[i] + B[j]
                if total not in sumAB:
                    sumAB[total] = 0
                sumAB[total] += 1

        # loop through CD combo and check if counterpart is in sumAB dictionary        
        for i in range(len(C)):
            for j in range(len(D)):
                totalCD = C[i] + D[j]
                counterpart = -totalCD #counterpart of totalCD
                if counterpart in sumAB:
                    count += sumAB[counterpart]
                    
                    
                    
        return count