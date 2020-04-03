#case 1
num=int(input('请输入一个整数:'))
if (num%4==0 and num%100!=0)or num%400==0:
    print('闰年')
else:
    print('非闰年')

# case 2
def dog_age(age):
    age = float(age)
    if age <= 2 :
        age=age*10.5
    else:
        age=21+(age-2)*4
    return age
dog=dog_age(input('please input dog`s age:'))
print('age is ',dog)

# case 3
def  test_point(point):
    point = int(point)
    if point ==100:
        return print("BWM")
    elif 80<=point<=99:
        return print("iPhone")
    elif 60<=point<=79:
        return print("book")
    else:
        return print("nothing")
point = test_point(input('how is your test ? '))