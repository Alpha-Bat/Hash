def solution(participant, completion):
    par = {}
    com = {}
    for i in completion :
        if com.get(i) == None :
            com[i] = 1
        else :
            com[i] += 1
    for j in participant :
        if par.get(j) == None :
            par[j] = 1
        else :
            par[j] += 1
    for k in par :
        if par.get(k) != com.get(k) :
            answer = k
            break
    return answer
