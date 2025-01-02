# 리스트 컴프리헨션(List Comprehension)
# for문을 한 줄로 간단히 작성하여
# 직전에 배운 map과 filter를 쉽게 적용,
# 로직에 따라 새로운 리스트를 쉽게 만들어내는
# 문법 기술을 의미한다.
# [e for e in range(10)] -> [0, 1, 2,..., 9]

if __name__ == "__main__":
    # 대괄호[] 가장 앞에 오는 내용은
    # 새로운 리스트를 구성할 요소의 값이 위치하며
    # 이는 앞에서 배운 map의 람다식 반환값과
    # 동일하다고 볼 수 있다.
    # arr = [e**2 for e in range(10)]
    # print(arr)

    # filter를 리스트 컴프리헨션에 적용하는 방법
    # 아래 코드를 해석해보면
    # 순서는 1. 원본 이터러블 객체의 요소를 가져옴.
    # 2. filter(if문) 적용
    # 3. map(로직) 적용
    # for e in range(10) 0부터 9까지의 숫자를 반복해서 e에 담는데
    # if e % 2 == 0 그렇게 e에 담긴 값이 짝수인 경우에만
    # e ** 2 제곱하여 새로운 리스트에 담아라
    arr = [e ** 2 for e in range(10) if e % 2 == 0]
    # arr = list(map(lambda x: x**2, list(filter(lambda x: x%2==0, range(10)))))
    print(arr)