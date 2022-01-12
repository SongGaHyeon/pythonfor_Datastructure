from stack import Stack
def parChecker(parSeq):
    S=Stack()
    for sym in parSeq:
        if sym=="(":
            S.push(sym)
        else:
            if len()==0:
                return False
            else:
                S.pop()
    if len()==0:
        return True
    else:
        return False
