#神经网络的自己实现和tensorflow实现
import numpy as np

#文本处理函数
def text2vec(data):
    str=list(data.strip().split(','))
    x=[]
    for i in str:
        x.append(float(i))
    return x
def sigmoid(x):
    return 1/(1+np.exp(-x))

#1标准BP算法

#参数矩阵
#三个隐层神经元，8个输入神经元
w1=np.mat(np.zeros([8,3]))
#三个隐层单元，1个输出神经元
w2=np.mat(np.zeros([3,1]))
#阈值theta
theta=0
#学习率
learning=0.01
#误差值
error=1000
#读取数据集
with open('watermalonedataset',mode='r',encoding='UTF-8') as file:
    lines=file.readlines()
    while(error>0.01):
        for data in lines:
            zerodata=text2vec(data)
            x=np.mat(zerodata[0:8])
            #计算初始预测值，即前向传播，多层前馈神经网络
            x1=sigmoid((np.dot(x,w1)))
            yhat=sigmoid(np.dot(x1,w2))
            y=zerodata[-1]
            #定义损失函数，这里使用均方误差
            error=(1/2)*np.square((yhat-y))
            #标准BP算法
            #首先调整隐层到输出层的参数w2
            g=np.array(yhat*(1-yhat)*(y-yhat),yhat*(1-yhat)*(y-yhat),yhat*(1-yhat)*(y-yhat))
            w2=w2-(learning*np.dot(x1,g)).T#乘以梯度下降量
            print(w2)
            w1=w1-learning*(np.dot(w2.T,g)*x1*(1-x1))*x#乘以梯度下降量
    print(w1)
    print(w2)
    print(error)
#2.累积BP算法

with open('watermalonedataset',mode='r',encoding='UTF-8') as file:
    lines=file.readlines()
    while(error>0.01):
        count=0
        for data in lines:
            count+=1
            zerodata=text2vec(data)
            x=np.mat(zerodata[0:8])
            #计算初始预测值，即前向传播，多层前馈神经网络
            x1=sigmoid((np.dot(x,w1)))
            yhat=sigmoid(np.dot(x1,w2))
            y=zerodata[-1]
            #定义损失函数，这里使用均方误差
            error=(1/2)*np.square((yhat-y))
            E=(E+error)/count
        #累计BP算法，得到总的误差平均值之后，再统一更新一次w参数
        g=np.array(yhat*(1-yhat)*(y-yhat),yhat*(1-yhat)*(y-yhat),yhat*(1-yhat)*(y-yhat))
        w2=w2-(learning*np.dot(x1,g)).T#乘以梯度下降量
        print(w2)
        w1=w1-learning*(np.dot(w2.T,g)*x1*(1-x1))*x#乘以梯度下降量




