import numpy as np

transfer=[{
    '青绿':1,
    '乌黑':2,
    '浅白':3
},{
    '蜷缩':1,
    '稍蜷':2,
    '硬挺':3
},{
    '浊响':1,
    '沉闷':2,
    '清脆':3
},{
    '清晰':1,
    '稍糊':2,
    '模糊':3
},{
    '凹陷':1,
    '稍凹':2,
    '平坦':3
},{
    '硬滑':1,
    '软粘':2,
},{
    '是':1,
    '否':0
}
]

wmData=[]
classify=[]
learningrate=0.1
#读取数据
with open('watermelon.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        data=line.strip('\n').split(',')
        if data[0]!='编号':
            #python这个range循环，相当于是i>=1 && i<10?
            for i in range(1,10):
                if i <= 6:
                    data[i]=transfer[i-1][data[i]]
                elif i==9:
                    data[i]=transfer[-1][data[i]]
                else:
                    data[i]=float(data[i])
            wmData.append(data[1:9])
            classify.append(data[9])
#建立模型
wmData=np.mat(wmData)
classify=np.array(classify).reshape(17,1)
w=np.mat([1,1,1,1,1,1,1,1],dtype=float)
yhat = 1/(1+np.exp(-np.dot(wmData,w.T)))
loss = classify-yhat
#使用梯度下降
i=0
#python和C++一样，在或关系中，一旦检测到前条件成立，后条件就不会检测
while(i<1):
    w+=learningrate*np.dot(loss.T,wmData)
    yhat = 1 / (1 + np.exp(-np.dot(wmData, w.T)))
    loss = classify - yhat
    i+=1
print(w)
print(loss)
for item in yhat:
    if item>0.5:
        print("1")
    else:
        print("0")



