#HW4
#name-Shreeya Garg
#roll no-2018415
#section-B
#group-8

import matplotlib.pyplot as plt
from math import sin
from math import cos
plt.figure(figsize=(10,10))
plt.ion()
plt.axis('equal')
def multiply(A,B):
	s=[]
	for i in range(len(A)):
		s.append([])
		for j in range(len(B[0])): # since number of rows of A=number of columns of B
			s[i].append(0) #initialize the list
	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(B)):
				s[i][j]+=A[i][k]*B[k][j]
	return s
object=input()
if object.lower()=="disc":
	nume=input()
	num=nume.split()
	x1=float(num[0]) # x coordinate of disc
	y1=float(num[1]) #y coordinate of disc
	r=float(num[2]) #radius of the disc

	#to print the disc given its center and radius.we print the circle by its  parameteric equation.
	X=[]
	Y=[] # x1 and y1 are starting coordinates
	thetadeg=0
	skip=4

	# we change theta by 5 degree each time and get the corresponding coordinates
	while thetadeg<=360:
		thetarad=0.017453*thetadeg
		a=x1+r*cos(thetarad)
		b=y1+r*sin(thetarad)
		X.append(a)
		Y.append(b)
		thetadeg+=skip
	plt.plot(X,Y)
	plt.show()
	var=1
	while var>0:
		val=input()
		if val.lower()=="quit":
			break
		val=val.split()
		
		#scaling operation
		if val[0].lower()=='s':
			scalx=float(val[1])
			scaly=float(val[2])
			matrix=[[scalx,0,0],[0,scaly,0],[0,0,1]] # matrix used to scale
			Z=[]
			for i in range(len(X)):
				Z.append(1)
			matrix2=[X,Y,Z]
			matrix2=multiply(matrix,matrix2)
			X=matrix2[0]
			Y=matrix2[1]
			plt.plot(X,Y)
			plt.show()
		# rotation operation
		if val[0].lower()=='r':
			thetadeg=float(val[1])
			theta=0.0174533*thetadeg
			cosine=cos(theta)
			sine=sin(theta)
			matrix=[[cosine,-sine,0],[sine,cosine,0],[0,0,1]]
			for i in range(len(X)):
				matrix2=[[X[i]],[Y[i]],[0]]
				s=multiply(matrix,matrix2)
				X[i]=s[0][0]
				Y[i]=s[1][0]
			print(X)
			print(Y)
			plt.plot(X,Y)
			plt.show()
		#translation
		if val[0].lower()=="t":
			dx=float(val[1])
			dy=float(val[2])
			matrix=[[1,0,dx],[0,1,dy],[0,0,1]]
			for i in range(len(X)):
				mat2=[[X[i]],[Y[i]],[1]]
				C=multiply(matrix,mat2)
				X[i]=C[0][0]
				Y[i]=C[1][0]
			print(X)
			print(Y)
			plt.plot(X,Y)
			plt.show()
if object.lower()=="polygon":
	X=list(map(float,input().split()))	# x coordinate list
	Y=list(map(float,input().split()))  #y coordinate list
	X.append(X[0])
	Y.append(Y[0])
	plt.plot(X,Y)
	plt.show()
	var=1
	while var>0:
		val=input()
		if val.lower()=="quit":
			break
		val=val.split()
		
		#scaling operation
		if val[0].lower()=='s':
			scalx=float(val[1])
			scaly=float(val[2])
			matrix=[[scalx,0,0],[0,scaly,0],[0,0,1]] # matrix used to scale
			Z=[]
			for i in range(len(X)):
				Z.append(1)
			X.append(X[0])
			Y.append(Y[0])
			Z.append(Z[0])
			matrix2=[X,Y,Z]
			matrix2=multiply(matrix,matrix2)
			X=matrix2[0]
			Y=matrix2[1]
			plt.plot(X,Y)
			plt.show()
		# rotation operation
		if val[0].lower()=='r':
			thetadeg=float(val[1])
			theta=0.0174533*thetadeg
			cosine=cos(theta)
			sine=sin(theta)
			matrix=[[cosine,-sine,0],[sine,cosine,0],[0,0,1]]
			Z=[]
			for i in range(len(X)):
				Z.append(1)
			X.append(X[0])
			Y.append(Y[0])
			Z.append(Z[0])
			matrix2=[X,Y,Z]
			matrix2=multiply(matrix,matrix2)
			X=matrix2[0]
			Y=matrix2[1]
			plt.plot(X,Y)
			plt.show()
		#translation
		if val[0].lower()=="t":
			dx=float(val[1])
			dy=float(val[2])
			matrix=[[1,0,dx],[0,1,dy],[0,0,1]]
			Z=[]
			for i in range(len(X)):
				Z.append(1)
			X.append(X[0])
			Y.append(Y[0])
			Z.append(Z[0])
			matrix2=[X,Y,Z]
			matrix2=multiply(matrix,matrix2)
			X=matrix2[0]
			Y=matrix2[1]
			plt.plot(X,Y)
			plt.show()
plt.show()