class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("동물은 울음소리를 낸다.")

# 부모 클래스로 Animal을 상속받는다.
class Dog(Animal):
    def speak(self):
        # 부모 클래스에서 정의된 내용을 그대로 실행하는 코드
        # return super().speak()

        # 해당 내용을 지우고 새로운 내용을 입력하면
        # 자식 클래스는 부모 클래스로부터 받은 메서드를
        # 재정의(override)하여 사용하게 된다.
        print(f"{self.name}은 멍멍 짖습니다.")
    
    def eat(self):
        # Dog 클래스에서만 정의된 메서드
        print(f"{self.name}은 개 사료를 먹습니다.")

# Cat 클래스 작성(Animal 클래스 상속)
class Cat(Animal):
    def __init__(self, name):
        # 부모 클래스의 기능을 받기 위해
        # super()라는 부모 클래스의 생성자를 호출하여야 한다.
        # 생략하더라도 부모 클래스의 기본생성자를 호출된다.
        super().__init__(name)

    # 부모로부터 받은 메서드 재정의
    def speak(self):
        # return super().speak()
        print(f"{self.name}은(는) 야옹 하고 웁니다.")

if __name__ == "__main__":
    # ba = Animal("바둑이")
    # ba.speak()

    doggy = Dog("바둑이2")
    # doggy.speak()

    catty = Cat("고일이")
    # catty.speak()

    # 리스트에 담기는 값은 Animal 타입이어야 한다.
    # 타입 힌트에는 강제성은 없지만, 
    # 이후 코드에서 자동완성 기능을 수행하는 데 도움이 된다.
    animals: list[Animal] = [doggy, catty]
    for animal in animals:
        animal.speak()
        # animal.eat() # Dog의 메서드는 Dog객체에 대해선 실행이 되지만
        # 다른 객체에서는 실행할 수 없다.
    # print(animals)
