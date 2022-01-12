# token화
# 식의 각 기호를 쪼개야하므로 이 함수를 필요로 한다. ex) "2" "+" "3"
def get_token_list(expr):
    # 여기서 expr= 입력받을 수식을 말하는 매개변수
    temp=[] #빈 리스트
    result=[] #결과를 저장할 리스트
    num=str()

    for i in expr:
        if i=="+"or i=="-" or i=="*" or i=="/" or i=="(" or i==")":
            # 만약 연산자가 다음에 나온다면
            for j in temp: #temp에 있는 것을 일단 num에 넣어준다 일단 수를 넣어줘야한다 비울 것이기 때문
                num+=j
            if num!="": #공백이 들어가는 것을 방지하기 위한 것
                result.append(float(num))
            result.append(i)
            temp=[] #비운다
            num=""
        else:
            temp.append(i)
            #이렇게 하는 이유는 입력받는 숫자가 두자리수, 혹은 세자리 수 일 수도 있기 때문에
            # 연산자가 나오지 않을 때 append해주는 것을 통해 이 경우를 해결할 수 있다.
    for k in temp: #expr에 있는 것이 숫자만 남아 temp에 무언가가 담겨있는 상태
        num+=k  #temp에 있는 것들을 num이라는 문자열에 담기
    result.append(float(num))
    return result