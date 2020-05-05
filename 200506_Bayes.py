# -*- coding: utf-8 -*-
"""
    贝叶斯分类器和贝叶斯网络
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    贝叶斯分类器
    :copyright: (c) 2020 by the angus.
"""
from matplotlib.colors import ListedColormap
from sklearn import naive_bayes
from sklearn import datasets
from sklearn.model_selection import StratifiedShuffleSplit
import  matplotlib.pyplot as plt
import numpy as np


def show_iris():
    '''
    结合类信息，在二维空间，以不同颜色绘制各样本点，以直观认识不同类别的分布。
    :return: None
    '''
    iris = datasets.load_iris()
    X = iris.data
    y =iris.target
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
    cmap_bold = ListedColormap(['darkorange', 'c', 'darkblue'])
    plt.scatter(X[:,0],X[:,1],c=y, cmap=cmap_bold,
           edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class distribution",loc='center')

    plt.show()

def test_GaussianNB(*data):
    '''
    测试 GaussianNB 的用法
    :param data: 可变参数。它是一个元组，这里要求其元素依次为：训练样本集、测试样本集、训练样本的标记、测试样本的标记
    :return: None
    '''
    X_train,X_test,y_train,y_test=data
    cls=naive_bayes.GaussianNB()
    cls.fit(X_train,y_train)
    #print('Training Score: %.2f' % cls.score(X_train,y_train))
    #print('Testing Score: %.2f' % cls.score(X_test, y_test))
    return 1 - cls.score(X_test, y_test)
    
    
def test_MultinomialNB(*data):
    '''
    测试 MultinomialNB 的用法
    :param data: 可变参数。它是一个元组，这里要求其元素依次为：训练样本集、测试样本集、训练样本的标记、测试样本的标记
    :return: None
    '''
    X_train,X_test,y_train,y_test=data
    cls=naive_bayes.MultinomialNB()
    cls.fit(X_train,y_train)
    #print('Training Score: %.2f' % cls.score(X_train,y_train))
    #print('Testing Score: %.2f' % cls.score(X_test, y_test))
    return 1 - cls.score(X_test, y_test)
def visiable(clf,X,y):
    h = .02
    
    cmap_light = ListedColormap(['orange', 'cyan', 'cornflowerblue'])
    cmap_bold = ListedColormap(['darkorange', 'c', 'darkblue'])
    
    
    #(1) 利用上述所有样本生成最终的决策树模型，完成上述工作。
    clf = clf
    clf.fit(X, y)
    
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = np.array(X)[:, 0].min() - 1, np.array(X)[:, 0].max() + 1
    y_min, y_max = np.array(X)[:, 1].min() - 1, np.array(X)[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    
    # Plot also the training points
    plt.scatter(np.array(X)[:, 0], np.array(X)[:, 1],cmap=cmap_bold,
                c=np.squeeze(y),edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("%s" % clf)
    
    plt.show()
    
    
    
    


if __name__=='__main__':

    #show_iris()
    #  加载鸢尾花数据集，保留原始数据集的前2个特征；
    iris = datasets.load_iris()
    X =iris.data[:,0:2]
    y = iris.target[:]
    
    #将其分层随机打乱，均分成m=5等份。拿出任意1份作为测试集、剩余4份作为训练集，得到5个版本的训练集、测试集组合进行学习
    sss = StratifiedShuffleSplit(n_splits=5, test_size=.25, random_state=0) 
    
    print("\n+++++贝叶斯分类模型+++++\n")
    i = 1
    score = []
    for train_index, test_index in sss.split(X,y):
        print("############第%d折#############" % i)
        i += 1
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        error = test_MultinomialNB(X_train,X_test,y_train,y_test)
        print('Testing Error: %.2f' % error)
        score.append(error)
    print('\nAverage Testing Error: %.2f' % np.array(score).mean())
    


    print("\n++++高斯朴素贝叶斯分类模型的学习、评价与使用++++++\n")
    i = 1
    score = []
    for train_index, test_index in sss.split(X,y):
        print("############第%d折#############" % i)
        i += 1
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        
        error = test_GaussianNB(X_train,X_test,y_train,y_test)
        print('Testing Error: %.2f' % error)
        score.append(error)
    print('\nAverage Testing Error: %.2f' % np.array(score).mean())
    visiable(naive_bayes.GaussianNB(),X,y)
