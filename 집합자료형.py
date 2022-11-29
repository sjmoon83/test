somelist = ['문넝운', '문준서', '문이서', '문성진', '김수용']
print(somelist)
print(somelist[2])
print(somelist[-2])
print('1번째부터 3번째까지 출력')
print(somelist[1:3])
print('1부터 마지막까지')
print(somelist[1:])

length = len(somelist)
print('홀수 번째만 출력')
print(somelist[1:length:2])
print('짝수 번째만 출력')
print(somelist[0:length:2])
print('3의 배수만 출력')
print(somelist[0:length:3])

tuple01 = (10, 20, 30)
tuple01 = tuple01 + (40,)
print('print tuple :', tuple01)

tuple02 = 10, 20 , 30, 40 # 단순 콤마 ㅇㄴ결

mylist = [10,20,30,40]

tuple03 = tuple(mylist)

if tuple02 == tuple03 :
    print("component equal")
else :
    print("component not equal")

exp04 = [10,20,30]  # 리스트로 생성
print(type(exp04))
exp05 = (40,50,60)  # 튜플로 생성
print(type(exp05))

print('+ 연산자는 2개의 튜플을 합치는 역할을 합니다.')
exp06 = tuple(exp04) + exp05 # exp04를 tuple type으로 치환
print(exp06)
print(type(exp06))

print('* 연산자는 튜플을 지정한 정수 만큼 반복시키는 역할을 합니다.')
exp07 = exp04 * 3
print(exp07)

print('튜플을 사용하면 변수들을 swap 시킬 수 있습니다.')
a, b = 11, 22
a, b = b, a

print('a=', a, ', b=', b)

# 튜플도 슬라이싱 가능

tuple08 = (11, 22, 33, 44, 55, 66)
print(tuple08[1:3])
print(tuple08[3:])

dictionary = {'김유신':50, '윤봉길':40, '김구':60}
print('사전 내역 : ', dictionary)
other = {'김벙신':50, '윤영길':40, '김구워':60}  # {}만 쓰면 dictionary 적용이 되는 듯.
print('사전 내역 : ', other)

print('\nkeys() 메소드는 사전의 key 목록을 보여 줍니다.')
for key in dictionary.keys():
    print(key)

print('\nvalues() 메소드는 사전의 values 목록을 보여 줍니다.')
for value in dictionary.values():
    print(value)

print('\nkeys()를 이용한 value 검색하기')
for key in dictionary.keys():
    print('{}의 나이는 {}입니다.'.format(key, dictionary[key]))

print('\nitems() 메소드는 key와 value로 이루어진 쌍(pair)을 보여 줍니다.')
for key, value in dictionary.items():
    print('{}의 나이는 {}입니다.'.format(key, value))

print('\nin은 키의 존재 여부를 확인해 줍니다.')
findkey = '유관순'
if findkey in dictionary :
    print(findkey + '(은)는 존재 합니다.')
else:
    print(findkey + '(은)는 존재하지 않습니다.')

print('\npop()를 이용한 데이터 끄집어 내기')
# 팝업된 정보의 value가 result에 대입된다.
result = dictionary.pop('김구')
print('pop 이후의 사전 내용 : ', dictionary)
print('pop된 내용 : ', result)

print('\nclear() 메소드는 사전의 내용을 모두 비웁니다.')
dictionary.clear()
print('사전 내역 : ', dictionary)