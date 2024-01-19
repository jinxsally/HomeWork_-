x,y,z=eval(input())
if x>y :
    t =y
    y = x
    x= t
if x>z :
    t=z
    z = x
    x= t
if y>z :
    t=z
    z = y
    y= t
print(x,y,z)