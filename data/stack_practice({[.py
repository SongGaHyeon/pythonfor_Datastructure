# from stack import Stack
# def parChecker(parSeq):
#     S= Stack()
#     for  sym in parSeq:
#         if sym=="(" or sym=="{" or sym=="[":
#             S.push(sym)
#         else:
#             if S.top()=="(" and sym==")":
#                 S.pop()
#             elif S.top()=="{" and sym=="}":
#                 S.pop()
#             elif S.top()=="[" and sym=="]":
#                 S.pop()
#             else:
#                 return False
#
# 내가 생각했던것

from stack import Stack
S=Stack()
paren= input("괄호 입력:")
for p in paren:
    if p=="(" or p=="{" or p=="[":
        S.push(p)
    elif p==")":
        if S.top()=="(":
            S.pop()
        else:
            print(") False")
            exit(0)
    elif p=="}":
        if S.top()=="{":
            S.pop()
        else:
            print("} False")
            exit(0)
    elif p=="]":
        if S.top()=="[":
            S.pop()
        else:
            print("] False")
            exit(0)
if(S.len_stack()==0):
    print("True")
else:
    print("False")