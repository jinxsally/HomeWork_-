
#使用蒙特卡洛法求解pi值
#比丰投针法
import numpy as np
import math
import time
# def throwNeedles(numNeedles):
#     inCircle = 0
#     for Needles in range(1,numNeedles + 1):
#         x = np.random.random()
#         y = np.random.random()
#         if math.sqrt((x*x + y*y)) <=1:#判断是不是在圆内
#             inCircle += 1
#     return 4*(inCircle/numNeedles)#第一象限的面积仅是pi/4，因此需要乘以4
# def getEst(numNeedles,numTrials):
#     estimates = []
#     for t in range(numTrials):
#         piGuess = throwNeedles(numNeedles)
#         estimates.append(piGuess)
#     curEst = sum(estimates)/len(estimates)
#     return curEst
# def estPi(precision,numTrials):
#     numNeedles = 1000
#     curEst = 0
#     while abs(curEst - math.pi)>precision:
#         curEst = getEst(numNeedles,numTrials)
#         numNeedles *= 2
#     return curEst
# precision = math.pow(10,-3)
# start_time = time.time()
# print(estPi(precision,100))
# end_time = time.time()
# run_time = end_time - start_time
# print(run_time)

#比丰投针粗略版
def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1,numNeedles + 1):
        x = np.random.random()
        y = np.random.random()
        if math.sqrt((x*x + y*y)) <=1:#判断是不是在圆内
            inCircle += 1
    return 4*(inCircle/numNeedles)
=======
#使用蒙特卡洛法求解pi值
#比丰投针法
import numpy as np
import math
import time
# def throwNeedles(numNeedles):
#     inCircle = 0
#     for Needles in range(1,numNeedles + 1):
#         x = np.random.random()
#         y = np.random.random()
#         if math.sqrt((x*x + y*y)) <=1:#判断是不是在圆内
#             inCircle += 1
#     return 4*(inCircle/numNeedles)#第一象限的面积仅是pi/4，因此需要乘以4
# def getEst(numNeedles,numTrials):
#     estimates = []
#     for t in range(numTrials):
#         piGuess = throwNeedles(numNeedles)
#         estimates.append(piGuess)
#     curEst = sum(estimates)/len(estimates)
#     return curEst
# def estPi(precision,numTrials):
#     numNeedles = 1000
#     curEst = 0
#     while abs(curEst - math.pi)>precision:
#         curEst = getEst(numNeedles,numTrials)
#         numNeedles *= 2
#     return curEst
# precision = math.pow(10,-3)
# start_time = time.time()
# print(estPi(precision,100))
# end_time = time.time()
# run_time = end_time - start_time
# print(run_time)

#比丰投针粗略版
def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1,numNeedles + 1):
        x = np.random.random()
        y = np.random.random()
        if math.sqrt((x*x + y*y)) <=1:#判断是不是在圆内
            inCircle += 1
    return 4*(inCircle/numNeedles)
print(throwNeedles(100000000))