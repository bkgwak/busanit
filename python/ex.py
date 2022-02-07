# \$ \\ \이스케이프 문자
food = 'python\'s favorite food is perl'
print(food)

# \n : 개행문자,줄을 바꾸어 줌 \r\f= 같은 의미지만 \n을 사용할 것
multiline = "Lite is too short\nyou need pyton"
print(multiline)

multiline = '''Lite is too short\n\n\nyou need pyton'''
print(multiline)

multiline = "Lite is too short\f\ryou need pyton"
print(multiline)

head = "python"
tail = " is fun!"
print(head + tail)

num1 = "100"
num2 = "200"
print(num1 + num2)

# ?! @앳 & 앰퍼센트 -틸드 * 아스트이스크
a = "-"
b = "a"
print(a*10)
print(b*10)

#파이썬은 0부터 숫자를 센다.
a = "Life is too short, you need python"
c = "123456-1234567"
# 'L' + 'i'
b = a[12:17]
d = b[0:6]
e = c[7:8]
print(b)
print(d)
print(e)

a = "20010331Rainy"
year = a[:4]
month = a[4:6]
day = a[6:8]
date = a[:8]
weather = a[8:]

print(date)
print(weather)

# %d : 포맷스트링
number = 10
day = "three"

print("%10s" % "five")
print("%10s" % 1234)
print("%10s" % 3.14)

# %d : 포맷스트링
number = 10
day = "three"
print("i eat %^10d apples." % number)
print("I eat %10s apple."%"five")
print("I ate %d apples. so I was sick for %s days." % (number, day))
print("%10s")

# "문자열".format()
print("I eat %d apples." % 3)
print("I eat %s apples." % "three")
print("I eat {0} apples." format (3))
print("I eat {0} apples." format ("three"))

def add(a,b):
    return a+b

add(3,4)


number = 10
day = "three"

print("I ate {0} apples. so I was sick for {1} days."format(number, day))
#number = 10
#day = "three"
print("{0:<10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:>10}".format("hi"))
