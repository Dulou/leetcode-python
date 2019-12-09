class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        flag = 0
        minLen = min(len(v1), len(v2))
        if len(v2) > len(v1):
            for i in range(len(v1), len(v2)):
                if int(v2[i]) > 0:
                    flag = -1
                    break
        else:
            for i in range(len(v2), len(v1)):
                if int(v1[i]) > 0:
                    flag = 1
                    break
        
        for i in range(minLen):
            if int(v2[i]) > int(v1[i]):
                return -1
            elif int(v2[i]) < int(v1[i]):
                return 1
        
        return flag
