# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

hn=[2,5,10,15,17,20,23,25,30,50,100,200,300]
pre=[]
rec=[]
f1=[]
with open("hidden_N_result.txt","r") as hnf:
    for line in hnf.readlines():
        terms=line.replace(")","").replace("(","").split(",")
        pre.append(float(terms[2]))
        rec.append(float(terms[3]))
        f1.append(float(terms[4]))

fig=plt.figure(1)


plt.plot(hn[:-3], pre[:-3], 'ro-', linewidth='1.0', markersize=8, label='precision')
plt.plot(hn[:-3], rec[:-3], 'kd-', linewidth='1.0', markersize=8, label='recall')
plt.plot(hn[:-3], f1[:-3], 'b>-', linewidth='1.0', markersize=8, label='F-Score')

plt.ylim([0.0, 1.1])
plt.xlabel("Hidden Unit Number=[2,5,10,30,50,100,200,300]")
plt.legend(loc='best',fontsize=15)
plt.title('Hiddent Unit experiment ')



fig.set_size_inches(10.5, 10.5, forward=True)
plt.show()
fig.savefig('HiddenUnitNo.png')
#plt.close()