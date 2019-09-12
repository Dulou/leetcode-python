"""
Brute Force Methods
"""
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split()
        for i in range(len(sentence)):
            for dict_word in dict:
                if len(sentence[i]) >= len(dict_word) and sentence[i][:len(dict_word)] == dict_word:
                    sentence[i] = dict_word

        return ' '.join(sentence)

"""
Create a Word Tree
Failed! Memory Limit Exceed!
"""
class WordTreeNode():
    def __init__(self, s, isLeaf=False):
        self.val = s
        self.ChildrenNode = {}
        self.isLeaf = isLeaf
    def append(self, s):
        if s in self.ChildrenNode:
            return self.ChildrenNode[s]
        tmp = WordTreeNode(s)
        self.ChildrenNode[s] = tmp
        return tmp
    def setleaf(self):
        self.isLeaf = True

class Solution2(object):
    def replaceWords(self, dict, sentence):
        root = WordTreeNode('')
        for word in dict:
            tmp = root
            for s in word:
                tmp = tmp.append(s)
                if tmp.isLeaf:
                    break
            tmp.setleaf()

        res = ''
        for sen_word in sentence.split():
            tmp = root
            for i in range(len(sen_word)):
                if sen_word[i] in tmp.ChildrenNode:
                    tmp = tmp.ChildrenNode[sen_word[i]]
                else:
                    res += ' ' + sen_word
                    break
                if tmp.isLeaf:
                    res += ' ' + sen_word[:i+1]
                    break
                # for example, "rf" in dict but there is a "r" in sentence
                elif i == len(sen_word)-1:
                    res += ' ' + sen_word

        return res[1:]

"""
Use Dict to Replace Tree above
"""
class Solution3(object):
    def replaceWords(self, dict, sentence):
        root = {}
        for word in dict:
            tmp = root
            for s in word:
                if s not in tmp:
                    tmp[s] = {}
                tmp = tmp[s]
                if '#' in tmp:
                    break
            tmp['#'] = True  # Leaf symbol

        res = []   # use string may cause Memory Limit Exceed
        for sen_word in sentence.split():
            tmp = root
            len_word = len(sen_word)
            for i in range(len_word):
                if sen_word[i] in tmp:
                    tmp = tmp[sen_word[i]]
                else:
                    res.append(sen_word)
                    break
                if '#' in tmp:
                    res.append(sen_word[:i+1])
                    break
                # for example, "rf" in dict but there is a "r" in sentence
                elif i == len_word-1:
                    res.append(sen_word)

        return ' '.join(res)

