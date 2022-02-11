import json
import matplotlib.pyplot as plt
import numpy as np


f=open('./src/message_1.json')
msgs=json.load(f)['messages']

simon, flavie = 0, 0
x=['simon','flavie']



for i in range(len(msgs)):
#     if 'content' in msgs[i].keys():
#         print(msgs[i]['content'])

# compter qui à envoyer le plus de messages
    if 'sender_name' in msgs[i].keys():
        if msgs[i]['sender_name'] =="Simon Duperray":
            simon+=1
        else:
            flavie+=1
        
    else:
        pass
y=[simon,flavie]

fig, ax = plt.subplots()

ax.stem(x, y)

# ax.set(xlim=(0, 2))

plt.show()

# print(x)
# print(y)