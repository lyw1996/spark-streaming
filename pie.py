import matplotlib.pyplot as plt
labels=["family","others","with classmates","with friends","with children","couple","alone"]
sizes = [15,7,2,32,7,23,14]
colors = ['red',"yellow","blue","green","pink","purple","orange"]
explode = (0.05,0,0,0,0,0,0)
patches,l_text,p_text =plt.pie(sizes,explode=explode,labels=labels,colors=colors,
labeldistance=1.1,autopct="%2.0f%%",shadow=False,startangle=90,pctdistance=0.6)
for i in l_text:
    i.set_size =30
for t in p_text:
    t.set_size =20
plt.axis("equal")
plt.legend(loc="upper left",bbox_to_anchor=(-0.1,1))
plt.grid()
plt.show()