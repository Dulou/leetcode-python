class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        for item in cpdomains:
            tmp = item.split()
            num = int(tmp[0])
            domains = tmp[1].split('.')
            domain = domains.pop()
            dict[domain] = dict.get(domain, 0) + num
            while len(domains) > 0:
                domain = '.'.join([domains.pop(), domain])
                dict[domain] = dict.get(domain, 0) + num
        
        res = []
        for item in dict:
            res.append(' '.join([str(dict[item]), item]))
        return res