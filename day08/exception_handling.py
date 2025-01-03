# 예외 처리
# 예외 처리란, 특정 오류 상황이 발생했을 때,
# 프로그램을 종료시키지 않고 대응 지침대로 진행 후
# 프로그램을 계속 실행시키도록 하는 구문이다.
def divide(value, target):
    result = None
    # value를 target으로 나누는 함수
    try: # 오류가 발생할 수 있는 코드를 작성하는 공간
        result = value / target # 오류가 발생할 수 있는 코드
    except ZeroDivisionError as e:        
        # 해당 예외 발생 시 실행할 코드
        print("0으로 나눌 수 없습니다.")
    except Exception as e:
        print(e) # 그외 다른 오류가 발생했을 때
        # 발생한 오류를 출력
    finally: # 에러 발생 여부와 무관하게 항상 실행하는 코드
        # result = result or False
        pass

    return result

if __name__ == "__main__":
    val = 10
    targ = "0"
    result = divide(val, targ)
    print(result)