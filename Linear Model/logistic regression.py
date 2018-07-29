import numpy as np

transfe=[{
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

with open('watermelon.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        data=line.strip('\n').split(',')
        if data[0]!='编号':


