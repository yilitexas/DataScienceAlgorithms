import math
import numpy as np

fileString=input("Enter names of the files dataset input-partition output-partition\n")

fileStringArray=fileString.split()

dataset1=fileStringArray[0]
partition2=fileStringArray[1]
partition3=fileStringArray[2]

input1=open(dataset1,"r")

dataset=input1.readlines()

input1.close()

input2=open(partition2,"r")

partition=input2.readlines()

input2.close()

firstLine=dataset[0].split()

m=int(firstLine[0])

n=int(firstLine[1])

#print(m)
#print(n)

inputMatrix=np.zeros((m,n))

def convertStringNumber(array1):
	len1=len(array1)
	tempStr1=array1[0]
	tempStr2=""
	tempStr3=""
	flag1=True
	flag2=True
	location=0
	location2=0
	
	for i in range(1,len1):
		if ((flag1==True) and (array1[i]!=tempStr1)):
			location=i
			flag1=False
			tempStr2=array1[i]
			#print(location)
			#print(tempStr2)
	for j in range((location+1),len1):
		if ((flag2==True) and (array1[j]!=tempStr1) and (array1[j]!=tempStr2)):
			location2=j
			flag2=False
			tempStr3=array1[j]

	indexArray=[]
	if (tempStr1!=""):
		indexArray.append(tempStr1)
	if (tempStr2!=""):
		indexArray.append(tempStr2)
	if (tempStr3!=""):
		indexArray.append(tempStr3)

	#print(indexArray)
	len2=len(indexArray)
	readArray=[]
	index1=0
	for i in range(len2):
		readArray.append(index1)
		index1=index1+1

	newArray=[]
	for i in range(len1):
		for j in range(len2):
			if (array1[i]==indexArray[j]):
				newArray.append(readArray[j])

	#print(newArray)

	return newArray	


for i in range(n):
	nArray=[]
	for j in range(m):
		temp1=dataset[(j+1)].split()
		#print(temp1)
		nArray.append(temp1[i])
	#print(nArray)
	tempArray=convertStringNumber(nArray)
	#print(tempArray)
	for j in range(m):
		inputMatrix[j][i]=int(tempArray[j])


#print(inputMatrix)

def entropy(array1):
	len1=len(array1)

	if (len1==0):
		e=0.0

	else:
		count0=0
		for i in range(len1):
			if (array1[i]==0):
				count0=count0+1

		count1=len1-count0

		if ((count0==0) or (count1==0)):
			e=0.0
		else:
	
			num1=float(count0)/len1
			num2=float(count1)/len1

		
			e=num1*(math.log(1/num1)/math.log(2))+num2*(math.log(1/num2)/math.log(2))

	return e

def maximumGain(inputMatrix1):

	maxGain=0.0
	position=0

	m=len(inputMatrix1)

	if (m>0):
		n=len(inputMatrix1[0])

		readout=[]

		for i in range(m):
			readout.append(inputMatrix1[i][n-1])

		#print(readout)


		e_s=entropy(readout)
		#print("e_s is: "+str(e_s))

		gainMatrix=[]

		for i in range(n-1):
			count0=0
			count1=0
			count2=0
			temp0=[]
			temp1=[]
			temp2=[]

			for j in range(m):
		
				#print(inputMatrix1[j][i])
		
				if (inputMatrix1[j][i]==0):
					temp0.append(inputMatrix1[j][n-1])
					count0=count0+1
			
				elif (inputMatrix1[j][i]==1):
					temp1.append(inputMatrix1[j][n-1])
					count1=count1+1

				elif (inputMatrix1[j][i]==2):
					temp2.append(inputMatrix1[j][n-1])
					count2=count2+1

			#print(temp0)
			#print(temp1)
			#print(temp2)
			e0=entropy(temp0)
			e1=entropy(temp1)
			e2=entropy(temp2)

			sum=float(count0+count1+count2)

			e_attribute=(count0/sum)*e0+(count1/sum)*e1+(count2/sum)*e2

			gain=e_s-e_attribute

			gainMatrix.append(gain)

		#print("gainMatrix is: ")
		#print(gainMatrix)

		for i in range(n-1):
			if (gainMatrix[i]>maxGain):
				maxGain=gainMatrix[i]
				position=i

	return (position,maxGain)

returnValue=maximumGain(inputMatrix)
position1=returnValue[0]
#print(position1)

def splitMatrix(inputMatrix1,position2):
	count_0=0
	count_1=0
	count_2=0

	set0=[]
	set1=[]
	set2=[]

	m=len(inputMatrix1)
	n=len(inputMatrix1[0])

	for i in range(m):
		if (inputMatrix1[i][position2]==0):
			count_0=count_0+1
			set0.append(i)
		elif (inputMatrix1[i][position2]==1):
			count_1=count_1+1
			set1.append(i)
		elif (inputMatrix1[i][position2]==2):
			count_2=count_2+1
			set2.append(i)


	#print(count_0)
	#print(count_1)
	#print(count_2)

	#print(set0)
	#print(set1)
	#print(set2)

	
	return (set0,set1,set2,count_0,count_1,count_2)

newReturnValue=splitMatrix(inputMatrix,position1)

set_0=newReturnValue[0]
set_1=newReturnValue[1]
set_2=newReturnValue[2]
count0=newReturnValue[3]
count1=newReturnValue[4]
count2=newReturnValue[5]

len_par=len(partition)

if (len_par==3):
	name=[]
	line0=partition[0].split()
	name.append(line0[0])
	targetSet_0=[]
	for i in range(len(line0)-1):
		targetSet_0.append(int(line0[i+1])-1)
	line1=partition[1].split()
	name.append(line1[0])
	targetSet_1=[]
	for i in range(len(line1)-1):
		targetSet_1.append(int(line1[i+1])-1)
	line2=partition[2].split()
	name.append(line2[0])
	targetSet_2=[]
	for i in range(len(line2)-1):
		targetSet_2.append(int(line2[i+1])-1)
elif (len_par==2):
	name=[]
	line0=partition[0].split()
	name.append(line0[0])
	targetSet_0=[]
	for i in range(len(line0)-1):
		targetSet_0.append(int(line0[i+1])-1)
	line1=partition[1].split()
	name.append(line1[0])
	targetSet_1=[]
	for i in range(len(line1)-1):
		targetSet_1.append(int(line1[i+1])-1)
	targetSet_2=[]
elif (len_par==1):
	name=[]
	line0=partition[0].split()
	name.append(line0[0])
	targetSet_0=[]
	for i in range(len(line0)-1):
		targetSet_0.append(int(line0[i+1])-1)
	targetSet_1=[]
	targetSet_2=[]
else:
	print("The partition-2.txt file was wrong!")

#print(set_0)
#print(set_1)
#print(set_2)
#print(targetSet_0)
#print(targetSet_1)
#print(targetSet_2)

flag=False

if (set_0==targetSet_0):
	if (set_1==targetSet_1):
		if (set_2==targetSet_2):
			flag=True
	elif (set_1==targetSet_2):
		if (set_2==targetSet_1):
			flag=True
elif (set_0==targetSet_1):
	if (set_1==targetSet_0):
		if (set_2==targetSet_2):
			flag=True
	elif (set_1==targetSet_2):
		if (set_2==targetSet_0):
			flag=True
elif (set_0==targetSet_2):
	if (set_1==targetSet_0):
		if (set_2==targetSet_1):
			flag=True
	elif (set_1==targetSet_1):
		if (set_2==targetSet_0):
			flag=True

#print(flag)

def extractMatrix(array1):
	lenArray=len(array1)
	submatrix=np.zeros((lenArray,n))

	for i in range(lenArray):
		temp1=array1[i]
		for j in range(n):
			submatrix[i][j]=inputMatrix[temp1][j]

	return submatrix


if (flag==False):
	print("The partition-2.txt file was wrong!")
else:
	submatrix0=extractMatrix(targetSet_0)
	lenSub0=len(submatrix0)

	submatrix1=extractMatrix(targetSet_1)
	lenSub1=len(submatrix1)

	submatrix2=extractMatrix(targetSet_2)
	lenSub2=len(submatrix2)

	returnValue0=maximumGain(submatrix0)
	sub_position0=returnValue0[0]
	sub_maxGain0=returnValue0[1]

	returnValue1=maximumGain(submatrix1)
	sub_position1=returnValue1[0]
	sub_maxGain1=returnValue1[1]

	returnValue2=maximumGain(submatrix2)
	sub_position2=returnValue2[0]
	sub_maxGain2=returnValue2[1]

	f0=sub_maxGain0*(lenSub0/float(m))
	f1=sub_maxGain1*(lenSub1/float(m))
	f2=sub_maxGain2*(lenSub2/float(m))

	newGainMatrix=[]
	newGainMatrix.append(f0)
	newGainMatrix.append(f1)
	newGainMatrix.append(f2)

	#print(newGainMatrix)

	newAttrMatrix=[]
	newAttrMatrix.append(sub_position0)
	newAttrMatrix.append(sub_position1)
	newAttrMatrix.append(sub_position2)

	#print(newAttrMatrix)

	newIndex=0.0
	setNumber=0

	for i in range(3):
		if (newGainMatrix[i]>newIndex):
			newIndex=newGainMatrix[i]
			setNumber=i

	#print(setNumber)
	#print(newAttrMatrix[setNumber])


	def splitMatrix2(inputMatrix1,inputArray1,position2):
		count_0=0
		count_1=0
		count_2=0

		set0=[]
		set1=[]
		set2=[]

		m=len(inputMatrix1)
		n=len(inputMatrix1[0])

		newMatrix=np.zeros((m,(n+1)))

		for i in range(m):
			newMatrix[i][0]=inputArray1[i]
			for j in range(n):
				newMatrix[i][j+1]=inputMatrix1[i][j]

		#print(newMatrix)

		for i in range(m):
			if (newMatrix[i][position2+1]==0):
				count_0=count_0+1
				set0.append(newMatrix[i][0])
			elif (newMatrix[i][position2+1]==1):
				count_1=count_1+1
				set1.append(newMatrix[i][0])
			elif (newMatrix[i][position2+1]==2):
				count_2=count_2+1
				set2.append(newMatrix[i][0])


		#print(count_0)
		#print(count_1)
		#print(count_2)

		#print(set0)
		#print(set1)
		#print(set2)

		return (set0,set1,set2,count_0,count_1,count_2)


	if (setNumber==0):
		value0=splitMatrix2(submatrix0,targetSet_0,newAttrMatrix[0])
		list00=value0[0]
		list01=value0[1]
		list02=value0[2]
		str00=""
		str01=""
		str02=""
		id00=""
		id01=""
		id02=""
		if (len(list00)>0):
			str00="X_1 "
			id00="X_1"
			for j in range(len(list00)):
				str00=str00+str(int(list00[j])+1)+" "
			str00=str00+"\n"
		if (len(list01)>0):
			str01="X_2 "
			id01="X_2"
			for j in range(len(list01)):
				str01=str01+str(int(list01[j])+1)+" "
			str01=str01+"\n"
		if (len(list02)>0):
			str02="X_3 "
			id02="X_3"
			for j in range(len(list02)):
				str02=str02+str(int(list02[j])+1)+" "
			str02=str02+"\n"

		Tstr=str00+str01+str02
		if (len_par==3):
			Tstr=Tstr+partition[1]+partition[2]
		elif (len_par==2):
			Tstr=Tstr+partition[1]
		print("Partition "+str(name[0])+" was replaced with partitions "+id00+" "+id01+" "+id02+" using Feature "+str(newAttrMatrix[0]+1))
	elif (setNumber==1):
		value1=splitMatrix2(submatrix1,targetSet_1,newAttrMatrix[1])
		list10=value1[0]
		list11=value1[1]
		list12=value1[2]
		str10=""
		str11=""
		str12=""
		id10=""
		id11=""
		id12=""
		if (len(list10)>0):
			str10="Y_1 "
			id10="Y_1"
			for j in range(len(list10)):
				str10=str10+str(int(list10[j])+1)+" "
			str10=str10+"\n"
		if (len(list11)>0):
			str11="Y_2 "
			id11="Y_2"
			for j in range(len(list11)):
				str11=str11+str(int(list11[j])+1)+" "
			str11=str11+"\n"
		if (len(list12)>0):
			str12="Y_3 "
			id12="Y_3"
			for j in range(len(list12)):
				str12=str12+str(int(list12[j])+1)+" "
			str12=str12+"\n"

		Tstr=str10+str11+str12
		if (len_par==3):
			Tstr=partition[0]+Tstr+partition[2]
		elif (len_par==2):
			Tstr=partition[0]+Tstr
		print("Partition "+str(name[1])+" was replaced with partitions "+id10+" "+id11+" "+id12+" using Feature "+str(newAttrMatrix[1]+1))
	elif (setNumber==2):
		value2=splitMatrix2(submatrix2,targetSet_2,newAttrMatrix[2])
		list20=value2[0]
		list21=value2[1]
		list22=value2[2]
		str20=""
		str21=""
		str22=""
		id20=""
		id21=""
		id22=""
		if (len(list20)>0):
			str20="Z_1 "
			id20="Z_1"
			for j in range(len(list20)):
				str20=str20+str(int(list20[j])+1)+" "
			str20=str20+"\n"
		if (len(list21)>0):
			str21="Z_2 "
			id21="Z_2"
			for j in range(len(list21)):
				str21=str21+str(int(list21[j])+1)+" "
			str21=str21+"\n"
		if (len(list22)>0):
			str22="Z_3 "
			id22="Z_3"
			for j in range(len(list22)):
				str22=str22+str(int(list22[j])+1)+" "
			str22=str22+"\n"

		Tstr=partition[0]+partition[1]+str20+str21+str22
		print("Partition "+str(name[2])+" was replaced with partitions "+id20+" "+id21+" "+id22+" using Feature "+str(newAttrMatrix[2]+1))

	
	#print(Tstr)

	output1=open(partition3,"w")

	output1.write(Tstr)

	output1.close()




