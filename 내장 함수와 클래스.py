wordInfo = {'세탁기': 50, '선풍기': 30, '청소기': 40, '냉장고': 60}

myxticks = sorted(wordInfo, key=wordInfo.get, reverse=True)
print(myxticks)

reverse_key = sorted(wordInfo.keys(), reverse=True)
print(reverse_key)

chartdata = sorted(wordInfo.values(), reverse=True)
print(chartdata)


def nolambda(x, y):
    return 3 * x + 2 * y


x, y = 3, 5

result = nolambda(x, y)
print('일반 함수 방식 : %d' % (result))

yeslambda = lambda x, y: 3 * x + 2 * y
result = yeslambda(x, y)
print('람다 방식 01 : %d' % (result))

result = yeslambda(5, 7)
print('람다 방식 02 : %d' % (result))


class Calculate:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):  # 클래스 내의 더하기 함수
        result = self.first + self.second
        return '더하기 : %d' % result

    def sub(self):
        result = self.first - self.second
        return '빼기 : %d' % result

    def mul(self):
        result = self.first * self.second
        return '곱하기 : %d' % result

    def div(self):
        if self.second == 0:  # 0일 경우 5로 대체하기
            self.second = 5
        result = self.first / self.second
        return '나누기 : %.3f' % result


calc = Calculate(14, 0)  # 인스턴스 생성

print(calc.add())  # 함수를 호출
print(calc.sub())
print(calc.mul())
print(calc.div())
