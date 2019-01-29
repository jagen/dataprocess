#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 最小二乘法学习

import numpy as np
import scipy as sp
from scipy.optimize import leastsq
import matplotlib.pyplot as plt


# 目标函数
def real_fun(x):
    return np.sin(2 * np.pi * x)

# 多项式
def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)

# 损失函数
def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret

# 十个点
x = np.linspace(0, 1, 10)
x_points = np.linspace(0, 1, 10000)

# 加上正太分布噪声的目标函数的值
y_ = real_fun(x)
y = [np.random.normal(0, 0.1) + y1 for y1 in y_]

regularization = 0.0001

# 带有惩罚函数的正则化的损失函数
def residuals_func_regularization(p, x, y):
    ret = fit_func(p, x) - y
    ret = np.append(ret, np.sqrt(0.5*regularization *np.square(p)))
    return ret

def fitting(M = 0):
    '''
    m 为多项式的次数
    '''
    # 随机初始化多项式参数
    p_init = np.random.rand(M + 1)
    # 最小二乘法
    p_lsq = leastsq(residuals_func, p_init, args=(x,y))
    print('Fitting Parameters:', p_lsq[0])

    p_lsq_regularization = leastsq(residuals_func_regularization, p_init, args=(x, y))
    print('Fitting regularization Parameters:', p_lsq_regularization[0])

    # 可视化
    plt.plot(x_points, real_fun(x_points), label='real')
    plt.plot(x_points, fit_func(p_lsq[0], x_points), label='fitted curve')
    plt.plot(x_points, fit_func(p_lsq_regularization[0], x_points), label='regularization')
    plt.plot(x, y, 'bo', label = 'noise')
    plt.legend()
    plt.show()
    return p_lsq

p_lsq_9 = fitting(M=9)