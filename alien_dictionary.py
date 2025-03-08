# finding the sequence(sorting) of letters in new alien language

def aleinLanguage(words):
    adj_list = { c:set() for w in words for c in w }  # here dict is needed, why check by making list
    for i in range(len(words)-1):
        min_len = min(len(words[i]), len(words[i+1]))
        for j in range(min_len):
            if words[i][j] != words[i+1][j]:
                adj_list[words[i][j]].add(words[i+1][j])
                break
    print(adj_list)
    
    # now, we need to implement the dfs in the whole graph(adjacency list)
    result = []
    visit = {}
    # here we have to check if the node being visited is in current path or not so that loop is detected

    def dfs(c):
        if c in visit:
            return visit[c]     # if true then loop is detected
        
        visit[c] = True
        for nei in adj_list[c]:
            dfs(nei)
        # at last we have to mark this as FALSE
        visit[c] = False
        result.append(c)  

    for c in adj_list:
        if dfs(c):
            return ""
    result.reverse()
    return "".join(result)


# words = ["wrt","wrf","er","ett","rftt"]
words = ["A", "BA", "BC", "C"]
print(aleinLanguage(words))