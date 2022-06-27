def solution(phone_book):
    plen = {}
    for pn in phone_book :
        if plen.get(len(pn)) == None :
            plen[len(pn)] = {pn:1}
        else :
            plen[len(pn)][pn] = 1
    for checklen in plen.keys():
        for targetlen, target in plen.items():
            if checklen < targetlen :
                for t in target:
                    if t[0:checklen] in plen[checklen].keys():
                        return False
    return True
