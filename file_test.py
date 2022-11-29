
print('파일을 읽기 모드로 오픈한다.')
myfile01 = open('D:\sample.txt', 'rt', encoding='UTF-8')
linelists = myfile01.readlines()
myfile01.close()
total = 0 # 총점
for one in linelists :
    score = int(one)
    total += score
average = total / len(linelists) # 평균

print('파일을 쓰기 모드로 오픈한다')
myfile2 = open('D:\esult.txt', 'wt', encoding='UTF-8')
myfile2.write('총점 : ' + str(total) + '\n')
myfile2.write('평균 : ' + str(average))

myfile2.close()
print('작업 완료')