# case 1 打印1-100偶数之和
def case1():
    print('case 1')
    i=0
    sum=0
    while i<=100:
       sum += i
       i += 2
       print(i)
    return print(sum)
case1()

# case 2 打印100内7的倍数和
def case2():
    print('case 2')
    i=0
    sum=0
    while i<=100:
        i += 7
        if i <100:
            sum += i
            print(i)
    return print(sum)
case2()

# case 3 求1000内水仙花数
def case3():
    print('case 3')
    def weishu(a):
        a_num = []
        while 0 < a:
            a_last = int(a % 10)
            a_num.insert(0, a_last)
            a = (a - a_last) / 10
        return a_num
    putin = 100
    while 99 < putin < 1000:
        num = 0
        for i in weishu(putin):
            num = num + i ** 3
            if putin == num:
                print(putin)
        putin += 1
case3()

# case 4 判断输入的数是不是质数
def case4():
    print('case 4')
    put = int(34)           # 输入一个整数
    middle = int(put / 2 + 1)
    flag = True
    for i in range(2,middle):
        if put%i==0:
            flag = False
            break           # 优化程序，跳过不必要的步骤
    if flag:
        print(put, '是质数')
    else:
        print(put, '不是质数')
case4()

# case 5 打印99乘法表
def acse5():
    print('case 5')
    i = 0
    while i <9:
        i += 1
        j = 1
        while j <= i:
            print(i,'*',j,'=',i*j,end='\t')
            j += 1
        print()
acse5()
