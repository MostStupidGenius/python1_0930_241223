# 함수 내에서 반복문을 사용하여
# 특별한 기능을 만들어보자.

# 목표: 반복할 횟수를 지정하여
# 0부터 해당 숫자까지 1의 등차를 가지는
# 등차수열(리스트)을 반환하는 함수 작성
def make_seq(number): # number: 반복할 횟수
    # 반환할 값을 미리 초기화해둔다.
    result = []
    
    # 전달받은 값을 활용하여 로직을 작성한다.
    for i in range(number+1): # 반복할 횟수까지 받으려면 +1을 해야 한다.
        # 0부터 number까지의 값이 담길 i를
        # result 리스트에 순차적으로 담는다.
        result.append(i)
    # 등차수열이 모두 담긴 result를 함수를 사용한 위치로
    # 반환해준다.
    return result # 반환할 내용을 미리 만들어둔다.

# 목표: 전달받은 숫자까지 0부터 순차적으로 숫자를 확인하여
# 짝수인 경우에만 리스트에 담아서 반환하는 함수 작성
# + i가 반복 횟수가 100을 넘어가면 조기종료
def make_even_list(number):
    result = []
    for i in range(number+1):
        if i > 100:
            # 가장 가까운 while/for문을 탈출(조기종료)하는
            # 키워드
            break
        # i의 값이 2로 나눴을 때 그 나머지가 0이라면
        # 짝수라는 의미이다.
        if i % 2 == 0: # i가 짝수라면
            result.append(i)
            continue # 가장 가까운 반복문의다음 반복으로 이동
        # 홀수라면
        else:
            # 그 값을 출력
            print(i)
            continue
        print("for문 안쪽의 continue 이후 코드는 실행되지 않는다.")
    return result

if __name__ == "__main__":
    # arr = make_seq(10)
    # print(arr)
    arr = make_even_list(1200)
    print(arr)