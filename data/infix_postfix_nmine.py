from stack import Stack
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

def infix_to_postfix(prob, opStack, outStack): #매개변수 3개를 우선 받는다
    # prob: 방금 토큰화를 진행한 리스트   opStack:스택
    # outStack: 후위 표기법으로 저장할 리스트
    for i in prob:
        if i=="*" or i=="/" or i=="(":
            opStack.push(i) #우선순위가 높은 *,/ 연산자가 나오면 스택에 그대로 넣기
        elif i=="+" or i=="-":
            # 우선순위가 낮은 것 들어오면 top을 확인한다
            if opStack.len_stack()==0:
                opStack.push(i) #안에 아무것도 없으면 일단 이 연산자들을 넣는다 (처음이니깐)
            else: #opStack안에 무언가가 있는 경우
                for j in range(opStack.len_stack()): #안에 있는 개수만큼 반복
                    if opStack.top()=="*" or opStack.top()=="/":
                        # 맨 위가 *이거나 / 이면
                        outStack.append(opStack.top())
                        #후위표기법으로 저장할 리스트에 opStack의 가장 위 *나 /를 넣어준다
                        opStack.pop()
                        #제거해준다 이미 넣었기 때문
                    opStack.push(i)
                    #마지막 남은 걸 넣어주기 위한 코드
        elif i==")":
            while(opStack.top()!="("):
                #닫는 괄호가 나오면 여는괄호가 나올 때까지 다 pop
                outStack.append(opStack.top())
                # 그 전까지는 나오는 다른 것들은 다 append
                opStack.pop()
            opStack.pop() #마지막에 남는 여는 괄호( 없애야한다

        else: #연산자가 아닌 경우 outStack에 추가
            outStack.append(i)
    while(opStack.len_stack()!=0): #opStack에 값이 없는 것이 아니면 반복
        outStack.append(opStack.top())  #후위 연산에 opStack에 있는 맨 위의 것을 넣기
        opStack.pop()# 이 while문은 공부가 조금 필요할듯

def compute_postfix(outStack):
    temp=Stack()

    for i in outStack:
        if(i!="+"and i!="-" and i!="*" and i!="/"): #연산자가 아니면 임시 스택에 넣음
            temp.push(i)
        else:
            operand1=temp.top()
            temp.pop()
            operand2=temp.top()
            temp.pop()
            if(i=="+"):
                temp.push(operand2+operand1)
            elif(i=="-"):
                temp.push(operand2-operand1)
            elif (i == "*"):
                temp.push(operand2*operand1)
            elif (i == "/"):
                temp.push(operand2/operand1)
        return temp.top()



