score = eval(input())
if score <60:
    print('不合格')
elif score>=60 and score<75:
    print('合格')
elif score>=75 and score<90:
    print('良好')
else:
    print('优秀')