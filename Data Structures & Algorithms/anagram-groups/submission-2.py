class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            sortedWords = ' '.join(sorted(word))
            if sortedWords in anagrams:
                anagrams[sortedWords].append(word)
            else:
                anagrams[sortedWords] = [word]
        return list(anagrams.values())