# 두 개의 숫자를 입력받아서
# 1. add    더한 결과를 반환하는 함수
# 2. multi  곱한 결과를 반환하는 함수
# 3. divide 나눗셈한 결과를 반환하는 함수
def add(num1, num2):
    result = num1 + num2
    return result

def multi(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

if __name__ == "__main__":
    print("add(10, 30)", add(10, 30), sep="\t") # 40
    print("multi(11, 11)", multi(11, 11), sep="\t") # 121
    print("divide(30, 10)", divide(30, 10), sep="\t") # 3.0
    
    # positional argument
    # 함수를 호출할 때 매개변수의 이름없이 그 순서로 값(인수)을
    # 함수의 매개변수에 전달하는 방식
    add(10, 20)

    # 매개변수의 이름을 지정하여 인수를 전달하는 방식
    add(num2=20, num1=15)


