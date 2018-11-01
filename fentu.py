import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mim
import matplotlib.ticker as ticker
import matplotlib
from pylab import mpl
import time
# font = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simhei.ttf', size=10)
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

def show():
	fig = plt.figure()  # 定义区域
	plt.rcParams["axes.unicode_minus"] = False
	ax1 = fig.add_subplot(2, 2, 1)  # 添加子图
	ax2 = fig.add_subplot(2, 2, 2)
	ax4 = fig.add_subplot(2, 2, 4)

	datas = pd.read_csv("F:\\result\Cost.csv")
	unrate = pd.read_csv("F:\\result\Day.csv")
	first_five = datas[0:]
	second_five = unrate[0:]
	ax1.plot(first_five["country"], first_five["averagecost"], c="red", marker="*")
	ax1.set_xlabel("Tourist attraction", size=10)
	ax1.set_ylabel("average cost", size=10)
	ax1.set_title("spending comparison")
	# ax1.axis([])
	# ax1.ion()
	ax4.plot(second_five["country"], second_five["average_travel_days"], c="blue", marker="o")
	ax4.set_xlabel("Tourist attraction", size=10)
	ax4.set_ylabel("average days", size=10)
	ax4.set_title("days comparison")
	# pic1 = mim.imread("/Users/liuyang/Desktop/Japan.png")
	ax2.yaxis.set_major_locator(ticker.NullLocator())
	ax2.xaxis.set_major_locator(ticker.NullLocator())
	# ax2.imshow(pic1)
	# plt.show()
	plt.ion()
	plt.pause(40)
	plt.close()
	# return

show()
show()
show()
show()
show()


