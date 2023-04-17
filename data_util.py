
# coding=utf-8

import os
import getConfig
import jieba
#结巴是国内的一个分词python库，分词效果非常不错。pip3 install jieba安装

gConfig = {}

gConfig=getConfig.get_config()

conv_path = gConfig['resource_data']
 
if not os.path.exists(conv_path):
	
	exit()
# 将训练集的数据识别读取并存入一个List中，大概分为以下几个步骤
# a、打开文件
# b、读取文件中的内容，并对文件的数据进行初步处理
# c、找出我们想要的数据存储下来
convs = []  # 用于存储对话的列表
with open(conv_path,encoding='utf-8') as f:
	# 存储一次完整对话
	one_conv = []
	for line in f:
		# 去除换行符，并将原文件中已经分词的标记去掉，重新用结巴分词.
		line = line.strip('\n').replace('/', '')
		if line == '':
			continue
		if line[0] == gConfig['e']:
			if one_conv:
				convs.append(one_conv)
			one_conv = []
		elif line[0] == gConfig['m']:
			# 将一次完整的对话存储下来
			one_conv.append(line.split(' ')[1])

# 把对话分成问与答两个部分
seq = []        

for conv in convs:
	if len(conv) == 1:
		continue
	# 因为默认是一问一答的，所以需要进行数据的粗裁剪，对话行数要是偶数的
	if len(conv) % 2 != 0:
		conv = conv[:-1]
	for i in range(len(conv)):
		if i % 2 == 0:
			# 使用jieba分词器进行分词
			conv[i]=" ".join(jieba.cut(conv[i]))
			conv[i+1]=" ".join(jieba.cut(conv[i+1]))
			# 因为i是从0开始的，因此偶数行为发问的语句，奇数行为回答的语句
			seq.append(conv[i]+'\t'+conv[i+1])

seq_train = open(gConfig['seq_data'],'w', encoding='utf-8')

for i in range(len(seq)):
   seq_train.write(seq[i]+'\n')
 
   if i % 1000 == 0:
      print(len(range(len(seq))), '处理进度：', i)
 
seq_train.close()



