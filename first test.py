print('이제시작인가')
print('연습중')

print(3*5)

str1 = '100'
str2 = '200'
str3 = '12.345'

int1 = int(str1)
int2 = int(str2)
float1 = float(str3)

print (int1 == str)

sum = int1 + int2
print ('출력1 : ', sum)

## 호구조사
name = input('이름 입력 : ')
print('이름 : %s' %(name))
age = int(input('나이 입력 : '))
print('나이 : %d' % (age))


## 커피팔기 1
coffee = 3 #판매 가능한 거피 개수
print("우리 매장에 커피 {}잔이 있습니다.".format(coffee))
money = int(input("돈을 넣어주세요 : ")) # 3000
print("{}를 입금하셨습니다.".format(money))

## 커피팔기 2

coffee = 3 # 판매 가능한 커피 수
price = 2000

print("우리 매장에 커피 {}잔이 있습니다.".format(coffee))

money = int(input("돈을 넣어주세요 : ")) #3000
print("{}원을 입금하였습니다.".format(money))


## 커피팔기 3

price = 2000 # 커피의 단가
change = money - price
print("거스름돈은 {}원이며, 커피 {}잔을 판매 합니다.".format(change, 1))
print("남은 커피의 양은 {}잔입니다.\n".format(coffee-1))