# 딕셔너리(dictionary) 메서드
# 딕셔너리에 담긴 데이터를 다루기 위한
# 여러가지 메서드가 존재한다.

if __name__ == "__main__":
    # 모든 키를 반환하는 keys()
    dict1 = {
        "name": "홍길동",
        "age": 30
    }
    # keys = dict1.keys()
    # print(set(keys))

    # 모든 값을 반환하는 values()
    # values = dict1.values()
    # print(tuple(values))

    # ★모든 키-값 쌍을 튜플로 반환하는 items()
    # for key, value in dict1.items():
    #     print(f"key: {key}\nvalue:{value}\n")
    
    # 딕셔너리 병합에 쓰이는 update()
    new_info = {
        "grade": "A",
        "major": "프로그래밍학과"
    }
    dict1.update(new_info)
    print(dict1)
    




