# finding the sequence(sorting) of letters in new alien language

def aleinLanguage(words):
    adj_list = { c:set() for w in words for c in w }  # here dict is needed, why check by making list
    for i in range(len(words)-1):
        min_len = min(len(words[i]), len(words[i+1]))
        
        for j in range(min_len):
            if words[i][j] != words[i+1][j]:
                adj_list[words[i][j]].add(words[i+1][j])

    return adj_list


words = ["wrt","wrf","er","ett","rftt"]
print(aleinLanguage(words))