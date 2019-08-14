import numpy as np
def predict(dic):
	list1=[dic[key] for key in dic.keys()]
	label1=np.argmax(np.array(list1[1:5]))
	label2=np.argmax(np.array(list1[5:9]))
	label3=np.argmax(np.array(list1[9:13]))
	dict1={0:"Action",1:"Romance",2:"Drama",3:"Horror"}
	dict2={0:"Action",1:"Drama",2:"Horror",3:"Romance"}
	dict3={0:"Action",1:"Romance",2:"Drama",3:"Horror"}
	genre1=dict1[label1]
	genre2=dict2[label2]
	genre3=dict3[label3]
	if genre1==genre2 and genre2==genre3:
		return genre1
	if genre1==genre2:
		return genre1
	if genre2==genre3:
		return genre2
	if genre1==genre3:
		return genre3
	return genre3
