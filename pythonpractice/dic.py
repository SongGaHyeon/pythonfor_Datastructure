#딕셔너리도 call by reference
def change(dic):

    dic["몸무게"]=42

dic={"name":"송가현", "age":14, "height":167}
print(dic)
print(dic["name"])

change(dic)
print(dic)