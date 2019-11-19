class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            l = S.split('@')
            l[0] = l[0][0].lower() + '*****' + l[0][-1].lower()
            for i in range(1, len(l)):
                l[i] = l[i].lower()
            return '@'.join(l)
        else:
            store = ''
            for s in S:
                if s == '+' or s == '-' or s == '(' or s == ')' or s == ' ':
                    continue
                store += s
            if len(store) == 13:
                return '+***-***-***-' + store[-4:]
            if len(store) == 12:
                return '+**-***-***-' + store[-4:]
            if len(store) == 11:
                return '+*-***-***-' + store[-4:]
            return '***-***-' + store[-4:]