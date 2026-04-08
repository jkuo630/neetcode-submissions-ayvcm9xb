class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # map -> key = sorted anagram -> value = word itself 
        # output = go thru the map and list all the diff lists 

        word_dict = {}

        for word in strs:
            key = sorted(word)
            keyWord = "".join(key)
            if keyWord in word_dict:
                word_dict[keyWord].append(word)
            else:
                word_dict[keyWord] = []
                word_dict[keyWord].append(word)
        
        ans = []
        for lst in word_dict.values():
            ans.append(lst)
        
        return ans

        