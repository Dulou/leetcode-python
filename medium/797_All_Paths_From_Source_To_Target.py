class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(res, point, path):
            if point == len(graph) - 1:
                res.append(path)
                return
            else:
                for i in graph[point]:
                    dfs(res, i, path+[i])
        
        res = []
        dfs(res, 0, [0])
        return res
        