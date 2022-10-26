# 题目：异或运算
# 0^0=0
# 0^1=1
# 1^0=1
# 1^1=0
import numpy as np
import matplotlib.pyplot as plt

# 输入数据--这里偏置定为1
X = np.array([[1, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [1, 1, 1, 1, 1, 1]])
# 标签--期望输出
Y = np.array([-1, 1, 1, -1])
# 权值初始化，1行6列，取-1到1的随机数
W = (np.random.random(6) - 0.5) * 2
print(W)
# 学习率
lr = 0.11
# 计算迭代次数
n = 0
# 神经网络输出
o = 0


def update():
    global X, Y, W, lr, n
    n += 1
    o = np.dot(X, W.T)
    W_C = lr * ((Y - o.T).dot(X)) / (X.shape[0])  # 权值改变数，这里除掉行数求平均值，因为行数多，权值改变就会很大。
    W = W + W_C


for i in range(1000):
    update()  # 更新权值

o = np.dot(X, W.T)
print("执行一千次后的输出结果：", o)  # 看下执行一千次之后的输出

# 用图形表示出来
# 正样本
x1 = [0, 1]
y1 = [1, 0]
# 负样本
x2 = [0, 1]
y2 = [0, 1]


def calculate(x, root):
    a = W[5]
    b = W[2] + x * W[4]
    c = W[0] + x * W[1] + x * x * W[3]
    if root == 1:  # 第一个根
        return (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
    if root == 2:  # 第二个根
        return (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)


xdata = np.linspace(-1, 2)

plt.figure()
plt.plot(xdata, calculate(xdata, 1), 'r')  # 用红色
plt.plot(xdata, calculate(xdata, 2), 'r')  # 用红色
plt.plot(x1, y1, 'bo')  # 用蓝色
plt.plot(x2, y2, 'yo')  # 用黄色
plt.show()
