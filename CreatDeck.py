import os
import random

path = 'english-vocabulary/'
book = {'1':'1 初中-乱序.txt','2':'2 高中-乱序.txt','3':'3 四级-乱序.txt','4':'4 六级-乱序.txt','5':'托福.txt','6':'考研.txt','7':'SAT.txt'}

def main(vac=4,num=10):
	vac = str(input("请输入词汇表：1初中2高中3四级4六级5托福6考研7SAT:"))
	num = int(input("请输入要选择的单词个数:"))
	count = 0 
	dict = {}
	with open(os.path.join(path,book[vac]), encoding='UTF-8') as file:
		for line in file:
			dict[count] = line.split('\t')[0]
			count += 1
	# Create a List for random numbers:
	L1 = random.sample(range(len(dict)),num)
	L2 = ''
	for i in L1:
		L2 = L2 + ',' +dict[i]

	print('请写一篇{}个词的英文文章，包含以下单词：{}。并翻译成中文'.format(num*20,L2[1:]))

if __name__ == '__main__':
	main()
