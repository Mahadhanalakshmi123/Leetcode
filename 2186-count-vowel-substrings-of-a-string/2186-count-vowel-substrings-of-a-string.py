class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        count = 0
        
        for i in range(len(word)):
            seen_vowels = set()
            for j in range(i, len(word)):
                if word[j] in vowels:
                    seen_vowels.add(word[j])
                    if len(seen_vowels) == 5:
                        count += 1
                else:
                    break
        
        return count
