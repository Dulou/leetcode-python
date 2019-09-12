class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        dict = {}
        for word in words:
            word_pre = ''
            for s in word:
                word_pre += table[ord(s)-ord('a')]
            if word_pre not in dict:
                dict[word_pre] = 0
        return len(dict)