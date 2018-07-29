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
#定义计算信息增益（即互信息）的函数
def calculate(mData,classify,feature,Ent,isseries):
    if isseries==True:
        print("连续特征")
    else:
        num_type=len(transfer[feature])
        count = len(wmData)
        totalEnt = 0
        for j in transfer[feature]:
            i = 0
            first=0
            second=0
            EntDv=0
            for index,data in enumerate(mData):
                if data[feature]==transfer[feature][j]:
                    i+=1
                    if classify[index]==0:
                        second+=1
                    else:
                        first+=1
            EntDv=-((first/i)*np.log2(first/i)+(second/i)*np.log2(second/i))
            rate = i/count
            totalEnt+=rate*EntDv
        Gain = Ent-totalEnt
        print(Gain)



calculate(wmData,classify,0,0.998,False)