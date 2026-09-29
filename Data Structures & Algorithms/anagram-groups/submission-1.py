from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
        
        # mydict = {}

        # for i in range(len(strs)):
        #     x = "".join(sorted(strs[i]))
        #     if x in mydict:
        #         mydict[x].append(strs[i])
        #     else:
        #         mydict[x] = [(strs[i])]
        
        # return list(mydict.values())
                    



        