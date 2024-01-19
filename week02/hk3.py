
#采用DFS，找出所有的情况
a = {1:'人',2:'狼',3:'羊',4:'菜'}#，使用字典1234分别代表人狼羊菜
#操作的函数

def f1(l =[]):#只有人过河
    l[1] =0
def f2(l =[]):#人和狼一起过河
    l[2] =0
def f3(l =[]):#人和羊一起过河
    l[3] =0
def f4(l =[]):#人和菜一起过河
    l[4] =0

def f11(l =[]):#只有人返回
    l[1] =1
def f22(l =[]):#人和狼一起返回
    l[2] =1
def f33(l =[]):#人和羊一起返回
    l[3] =1
def f44(l =[]):#人和菜一起返回
    l[4] =1


#分析原岸的状态，只能为10种
left = [['狼',1],['羊',1],['菜',1]]
right = [['狼',0],['羊',0],['菜',0]]#保存两岸的状态
l = len(left)#计算可行性的个数
count = 0#计算步数
number = -1

def judge(left):#判断能不能共存
    if left[1][1]==1 and left[0][1] + left[2][1] == 1:#判断羊能不能与其他两个共存
        return False
    else:
        return True
def left_to_right():
    global number
    global count
    for i in range(l):
        if left[i][1]==1 and i!=number:#判断能不能从左岸到右岸
            left[i][1] -= 1#进行移动操作
            if judge(left):#如果可以进行移动
                right[i][1]+=1
                number = i
                print("%s,left -> right"%left[i][0])
                count+=1#步数加一
                break#停止
            else:#不能移动就加回来
                left[i][1] += 1
                continue
        else:
            continue

def right_to_left():#另一方案是对称的
    global number
    global count
    if judge(right) == False:#只有不能共存的时候才需要从右岸移动到左岸
        for j in range(l):
            if right[j][1] == 1 and  j!=number:#不能刚刚移过来又再移过去
                right[j][1]-=1
                left[j][1]+=1
                number = j
                print("%s,right->left"%right[j][0])
                count+=1
                break
    else:
        if right[0][1]+right[1][1]+right[2][1]==3:
            print('over')
        else:
            print('right->left')
            count+=1

def sucess(right):
     if right[0][1]+right[1][1]+right[2][1]==3:
         return True
     else:
         return False

while 1:
    left_to_right()
    right_to_left()
    if sucess(right):
        print('程序需要%d步'%count)
        break









