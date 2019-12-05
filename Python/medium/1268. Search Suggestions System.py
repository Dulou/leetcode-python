class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        products_len = len(products)
        
        start = 0
        for i in range(len(searchWord)):
            tmp = searchWord[:i+1]
            res_tmp = []
            flag = 0
            num = 0
            
            for j in range(start, products_len):
                if num == 3:
                    break
                if products[j][:i+1] == tmp:
                    if not flag:
                        start = j
                        flag = 1
                    num += 1
                    res_tmp.append(products[j])
            
            res.append(res_tmp)
        return res    
            