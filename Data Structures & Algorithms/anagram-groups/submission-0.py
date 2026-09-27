class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            sorted_words = ''.join(sorted(word))
            if sorted_words in anagram_dict:
                anagram_dict[sorted_words].append(word)
            else:
                anagram_dict[sorted_words] = [word]

        return list(anagram_dict.values())

