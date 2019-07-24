class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): 
            return []
        
        res = list()
        cur_contained = dict()
        for letter in p: #build dictionary with what we want to find
            if letter in cur_contained.keys():
                cur_contained[letter] -= 1
            else:
                cur_contained[letter] = -1

        for i in range(len(p)):
            if s[i] in cur_contained.keys():
                cur_contained[s[i]] += 1
                if cur_contained[s[i]] == 0:
                    del cur_contained[s[i]]
            else:
                cur_contained[s[i]] = 1
        if len(cur_contained.keys()) == 0:
            res.append(0)
        
        for i in range(len(s) - len(p)): #count the number of subarrays that are anagrams by checking if dictionary keys are empty
            if s[i] in cur_contained.keys(): #remove the first element in subarray
                cur_contained[s[i]] -= 1
                if cur_contained[s[i]] == 0:
                    del cur_contained[s[i]]
            else:
                cur_contained[s[i]] = -1 

            if s[i + len(p)] in cur_contained.keys(): #add next element
                cur_contained[s[i + len(p)]] += 1
                if cur_contained[s[i + len(p)]] == 0:
                    del cur_contained[s[i + len(p)]]
            else:
                cur_contained[s[i + len(p)]] = 1
            
            if len(cur_contained.keys()) == 0: #add to result
                res.append(i+1)
        return res 
            
#optimal using sliding window 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = list()
        if len(p) > len(s):
            return res
        p_letters = dict()
        n = len(p)
        for letter in p:
            if letter in p_letters:
                p_letters[letter] += 1
            else:
        
                p_letters[letter] = 1
        counter = len(p_letters)
        begin = end = 0

        while end < len(s):
            c = s[end]
            if c in p_letters:
                p_letters[c] -= 1
                if p_letters[c] == 0:
                    counter -= 1
            end += 1

            while counter == 0:
                c = s[begin]
                if c in p_letters:
                    p_letters[c] += 1
                    if p_letters[c] > 0:
                        counter += 1
                if end - begin == n:
                    res.append(begin)
                begin += 1
        
        return res



