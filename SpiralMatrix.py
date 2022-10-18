matrix=[[1,2,3],[4,5,6],[7,8,9]]
ans=[]
top,bot,lef,rig, dir=0, len(matrix)-1,0,len(matrix[0])-1,0
while left<=right and top<=bottom:
	if dir==0:
		for i in range(left,right+1)
			ans.append(matrix[top][i])
		dir =1
		top +=1
	elif dir ==1:
		for i in range (top, bottom+1):
			ans.append(matrix[i][right])
		dir=2
		right-=1
	elif dir==2:
		for i in range(right,left-1,-1):
			ans.append(matrix[bottom][i])
		dir=3
		bottom-=1
	else:
		for i in range(bottom,top-1,-1)
			ans.append(matrix[i][left])
		dir=0
		left+=1
print(ans)

