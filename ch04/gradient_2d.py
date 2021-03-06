#수치 미분으로 기울기를 구하기
#두 편미분을 동시에 계산
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성
    
    for idx in range(x.size):
        tmp_val = x[idx]
        
        # f(x+h) 계산
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)
        
        # f(x-h) 계산
        x[idx] = tmp_val - h 
        fxh2 = f(x) 
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원
        
    return grad

# 수치 미분
def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        
        return grad

# 함수
def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)

# 접선 구하는 함수
def tangent_line(f, x):
    d = numerical_gradient(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

#경사법에 의한 갱신 과정을 나타내는 함수, 학습률=0.01
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)

# init_x = np.array([-3.0, 4.0])    

# lr = 0.1
# step_num = 20
# x, x_history = gradient_descent(function_2, init_x, lr=lr, step_num=step_num)

# plt.plot( [-5, 5], [0,0], '--b')
# plt.plot( [0,0], [-5, 5], '--b')
# plt.plot(x_history[:,0], x_history[:,1], 'o')

# plt.xlim(-3.5, 3.5)
# plt.ylim(-4.5, 4.5)
# plt.xlabel("X0")
# plt.ylabel("X1")
# plt.show()


# # 그래프 그리기   
# if __name__ == '__main__':
#     x0 = np.arange(-2, 2.5, 0.25)
#     x1 = np.arange(-2, 2.5, 0.25)
#     X, Y = np.meshgrid(x0, x1)
    
#     X = X.flatten()
#     Y = Y.flatten()
    
#     grad = numerical_gradient(function_2, np.array([X, Y]) )
    
#     plt.figure()
#     plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")#,headwidth=10,scale=40,color="#444444")
#     plt.xlim([-2, 2])
#     plt.ylim([-2, 2])
#     plt.xlabel('x0')
#     plt.ylabel('x1')
#     plt.grid()
#     plt.legend()
#     plt.draw()
#     plt.show()

 
