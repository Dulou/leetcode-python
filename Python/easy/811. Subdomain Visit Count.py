class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        
        for domain in cpdomains:
            num, name = domain.split(' ')
            num = int(num)
            
            name_split = name.split('.')
            for i in range(len(name_split)):
                tmp = '.'.join(name_split[i:])
                count[tmp] = count.get(tmp, 0) + num
        
        res = []
        for key in count:
            res.append(str(count[key]) + ' ' + key)
        return res
        