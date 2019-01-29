#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 感知机算法实现，利用Iris数据

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import random

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['label'] = iris.target

df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'label']

plt.scatter(df[:50]['sepal length'], df[:50]['sepal width'], label='0')
plt.scatter(df[50:100]['sepal length'], df[50:100]['sepal width'], label='1')
plt.xlabel('sepal length')
plt.ylabel('sepal width')

data = np.array(df.iloc[:100, [0, 1, -1]])
X, y = data[:,0:2], data[:,-1]
y = np.array([1 if i ==1 else -1 for i in y])

# 数据线性可分，二分类数据
# 此处为一元一次线性方程

class Model:
    def __init__(self):
        self.w = np.zeros(len(data[0]) - 1, dtype=np.float32)
        self.b = 0
        self.l_rate = 0.01 # 学习率
        self.clf = None

    def sign(self, x, w, b):
        y = np.dot(w, x) + b
        return y

    def sign_gram(self, y, i, G, a, b):
        tmp = 0
        for j in range(len(a)):
            tmp += a[j] * y[j] * G[i, j]
        return (tmp + b)

    # 随机梯度下降法
    def fit(self, X_train, y_train, max_iter=1000):
        is_wrong = True
        for i in range(max_iter):
            wrong_count = 0
            for d in range(len(X_train)):
                X = X_train[d]
                y = y_train[d]
                # 对于误分类数据有 y(w*x+b)<=0成立
                if y * self.sign(X, self.w, self.b) <=0:
                    self.w = self.w + self.l_rate * np.dot(y, X)
                    self.b = self.b + self.l_rate * y
                    wrong_count += 1
            if wrong_count == 0:
                break
        return '感知机模型!'

    # 使用scikit-learn的感知机
    def fit_sklearn(self, X_train, y_train):
        self.clf = Perceptron(fit_intercept=False, max_iter=1000, shuffle=False)
        self.clf.fit(X_train, y_train)

    # 对偶形式的感知机
    def fit_gram(self, X_train, y_train, max_iter=1000):
        # 生成gram矩阵
        l = len(X_train)
        G = np.matmul(X_train, X_train.T)
        a = [0 for i in range(l)]
        b = 0
        for iter in range(max_iter):
            wrong_count = 0
            for i in range(l):
                if y_train[i] * self.sign_gram(y_train, i, G, a, b) <= 0:
                    a[i] = a[i] + self.l_rate
                    b = b + self.l_rate*y_train[i]
                    wrong_count += 1
            if wrong_count == 0:
                break

        for i in range(l):
            self.w += a[i] * X_train[i] *y_train[i]
        self.b = b
        return 

    def score(self):
        pass

p1 = Model()
p1.fit_gram(X, y, max_iter=1000) # 学习模型
#perceptron.fit_sklearn(X, y)

#p2 = Model()
#p2.fit(X, y, max_iter=1000)

x_point = np.linspace(4, 7, 10)
y_ = -(p1.w[0] * x_point + p1.b) / p1.w[1]
plt.plot(x_point, y_)

#y_ = -(p2.w[0] * x_point + p2.b) / p2.w[1]
#plt.plot(x_point, y_)

plt.legend()
plt.show()


