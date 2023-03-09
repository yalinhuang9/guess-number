import random
r = random.randint(1, 100)
count = 0
while True:
    u = int(input('請猜一個1-100的數字: '))
    count += 1 # count = count + 1
    if r == u:
        print('終於猜對了！')
        print('這是你猜的第', count, '次')
        break
    elif r < u:
        print('比答案大')
    elif r > u:
        print('比答案小')
    print('這是你猜的第', count, '次')