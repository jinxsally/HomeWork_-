
import math

n = float(input())
a = []#存储得到的二进制编码
c = []#存储得到整数部位的二进制编码
b = math.floor(n)
d = round(n - b,5)
#print(b,d)#检验
while b>0:
    c.append(b%2)
    b = math.floor(b/2)

for i in range(8):
    a.append(math.floor(d*2))
    if d*2 >=1:
        d = d*2 -1
    else:
        d = d*2
list.reverse(c)
s1 = " ".join(map(str,c))
s2 = " ".join(map(str,a))


def decimal_to_binary(decimal_number, precision=8):
    binary_result = ""

    # 处理小数部分
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part

    # 转换整数部分为二进制
    binary_result += bin(integer_part)[2:] + "."

    # 转换小数部分为二进制
    for _ in range(precision):
        fractional_part *= 2
        binary_digit = int(fractional_part)
        binary_result += str(binary_digit)
        fractional_part -= binary_digit

    return binary_result


# 输入十进制小数
decimal_number = float(input('输入十进制小数'))

# 调用函数进行转换，默认精度为8位
binary_result = decimal_to_binary(decimal_number)
print(f"十进制数 {decimal_number} 转换为二进制数为 {binary_result}")