def list_test(my_list):
    print("함수 내에서의 my_list 주소값:", id(my_list))
    my_list=[1,2,3,4]
    print("함수 내에서의 my_list값 출력:", my_list)
    print("함수 내에서의 my_list 주소값:",id(my_list))
    return

# my_list 타입은 list 타입으로, 변경가능객체임
my_list=[100,200,300,400]
print("함수 호출 전 my_list의 주소값:",id(my_list))
list_test(my_list)
print("함수 호출 후 my_list의 주소값:",id(my_list))
print("함수 호출 전 my_list의 값:",my_list)



