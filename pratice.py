import re
import random



# 1
# num = input("수를 입력하세요: ")

# if num.isdigit():
#     if int(num) % 3 == 0:
#         print('3의 배수 입니다.')
#     else:
#         print('3의 배수가 아닙니다.')
# else:
#     print('정수가 아닙니다.')


# 2

# number = input('수를 입력하세요:')
#
# print('짝수' if int(number) % 2 == 0 else'홀수')

# 3

# s = '/usr/local/bin/python'
# print(s.rsplit('/', 1))

# 4
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

# regx = re.compile('<.*?>')
# s = re.sub(regx, ' ', s)
# print(s)

# 5

# 6

# list = [1, 2, 3, 4, 5, 6, 7]
# s, c = 0, 0
#
# for i in list:
#     if(i%3 == 0):
#         c+=1
#         s+=i
# print("3의 배수의 개수: {0} \n3의 배수의 합: {1}".format(c, s))

# 7
# prices = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
# price = 67879
#
# for i in prices:
#     print(str(i) + "원 :" + str(price//i) + "개")
#     price -= i*(price//i)

# 8
# count = 0
# list = []
# print("5개의 정수를 입력하세요 (평균이 나와용)")
# while count < 5:
#     list.append(int(input('')))
#     count += 1
#
# print(sum(list)/len(list))

# 9

# string = "JAVA"
#
# def reverse(s):
#     return s[::-1]
#
# print(reverse(string))

# 10

# 11

# def _sum(*args):
#     return sum(args)
#
# print(_sum(1, 2, 3, 4))

# 12

# regx = re.compile('.?[3|6|9]')
# result = [x for x in range(1, 100) if regx.match(str(x))]
#
# for i in result :
#     print(str(i) + " " + "짝" * (str(i).count('3') + str(i).count('6') + str(i).count('9')))

# 13
# num = input("숫자를 입력하세요: ")
#
# result = [x for x in range(1, int(num)+1) if x%2 == int(num)%2]
#
# print("결과값: " + format(sum(result), "d"))

# 14

while(True):
    game_count = 1
    goal = random.randrange(1, 101)
    print("수를 결정하였습니다. 맞추어 보세요")
    max = 100
    min = 1
    print(str(min) + "-" + str(max))

    while(True):
        number = input(str(game_count) + '>>')

        if int(number) == goal:
            print("맞았습니다.")
            break

        elif int(number) > goal:
            print("더 낮게")
            max = int(number)
            game_count += 1
        else:
            print("더 높게")
            min = int(number)
            game_count += 1

        print(str(min) + "-" + str(max))

    restart = input('다시 하시겠습니까(y/n)>>')
    if (restart.lower() != 'y'):
        break

